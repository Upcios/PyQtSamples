# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtQuick
from PyQt5.QtQuick import QSGImageNode, QSGNode
import squircle_renderer

class RenderThread( QtCore.QThread ):
    textureReady = QtCore.pyqtSignal( int, QtCore.QSize )

    def __init__( self, size ):
        super().__init__()

        self.surface = None
        self.context = None
        self.render_fbo = None
        self.display_fbo = None
        self.renderer = None
        self.size = size

        Squircle.threads.append( self )

    def renderNext( self ):
        self.context.makeCurrent( self.surface )

        if not self.render_fbo:
            # Initialize the buffers and renderer
            format = QtGui.QOpenGLFramebufferObjectFormat()
            format.setAttachment( QtGui.QOpenGLFramebufferObject.CombinedDepthStencil )
            self.render_fbo = QtGui.QOpenGLFramebufferObject( self.size, self.format )
            self.display_fbo = QtGui.QOpenGLFramebufferObject( self.size, self.format )
            self.renderer = squircle_renderer.SquircleRenderer()
            self.renderer.initialize()

        self.render_fbo.bind()
        self.context.functions().glViewport( 0, 0, self.size.width(), self.size.height() )

        self.renderer.render()

        # We need to flush the contents to the FBO before posting
        # the texture to the other thread, otherwise, we might
        # get unexpected results.
        self.context.functions().glFlush()

        self.render_fbo.bindDefault()
        QtCore.Qt.qSwap( self.render_fbo, self.display_fbo )

        self.textureReady.emit( self.display_fbo.texture(), self.size )

    def shutDown( self ):
        self.context.makeCurrent( self.surface )
        self.render_fbo = None
        self.display_fbo = None
        self.renderer = None
        self.context.doneCurrent()
        self.context = None

         # schedule this to be deleted only after we're done cleaning up
        self.surface.deleteLater()

        # Stop event processing, move the thread to GUI and make sure it is deleted.
        self.exit()
        self.moveToThread( QtGui.QGuiApplication.instance().thread() )

class TextureNode( QtCore.QObject, QSGImageNode ):
    textureInUse = QtCore.pyqtSignal()
    pendingNewTexture = QtCore.pyqtSignal()

    def __init__( self, window ):
        super().__init__()

        self.id = 0
        self.size = QtCore.QSize()
        self.mutex = QtCore.QMutex()
        self.window = window
        # Our texture node must have a texture, so use the default 0 texture.
        self.texture = self.window.createTextureFromId( 0, QtCore.QSize( 1, 1 ) )
        self.setTexture( self.texture )
        self.setFiltering( QtQuick.QSGTexture.Linear )

    # This function gets called on the FBO rendering thread and will store the
    # texture id and size and schedule an update on the window.
    def newTexture( self, id, size ):
        self.mutex.lock()
        self.id = id
        self.size = size
        self.mutex.unlock()

        # We cannot call QQuickWindow::update directly here, as this is only allowed
        # from the rendering thread or GUI thread.
        self.pendingNewTexture.emit()

    # Before the scene graph starts to render, we update to the pending texture
    def prepareNode( self ):
        self.mutex.lock()
        newId = self.id
        size = self.size
        self.id = 0
        self.mutex.unlock()
        if newId:
            self.texture = None
            # note: include QQuickWindow::TextureHasAlphaChannel if the rendered content
            # has alpha.
            self.texture = self.window.createTextureFromId( newId, size )
            self.setTexture( self.texture )

            self.markDirty( QtQuick.QSGNode.DirtyMaterial )

            # This will notify the rendering thread that the texture is now being rendered
            # and it can start rendering to the other one.
            self.textureInUse.emit()

class Squircle( QtQuick.QQuickItem ):
    tChanged = QtCore.pyqtSignal()

    threads = []

    def __init__( self, parent=None ):
        super().__init__( parent )

        self.setFlag( self.ItemHasContents, True )
        self.render_thread = RenderThread( QtCore.QSize( 512, 512 ) )

    @QtCore.pyqtProperty( float, notify=tChanged )
    def t( self ):
        if self.render_thread.renderer == None:
            return 0.0
        else:
            return self.render_thread.renderer.t

    @t.setter
    def t( self, value ):
        if self.render_thread.renderer == None or self.render_thread.renderer.t == value:
            return
        self.render_thread.renderer.setT( value )
        self.tChanged.emit()
        if self.window():
            self.window().update()

    QtCore.pyqtSlot()
    def ready( self ):
        self.render_thread.surface = QtGui.QOffscreenSurface()
        self.render_thread.surface.setFormat( self.render_thread.context.format() )
        self.render_thread.surface.create()

        self.render_thread.moveToThread( self.render_thread )

        self.window().sceneGraphInvalidated.connect( self.render_thread.shutDown, QtCore.Qt.QueuedConnection )

        self.render_thread.start()
        self.update()

    def updatePaintNode( self, old_node, data ):
        node = old_node

        if self.render_thread.context == None:
            current = self.window().openglContext()
            # Some GL implementations requres that the currently bound context is
            # made non-current before we set up sharing, so we doneCurrent here
            # and makeCurrent down below while setting up our own context.
            current.doneCurrent()

            self.render_thread.context = QtGui.QOpenGLContext()
            self.render_thread.context.setFormat( current.format() )
            self.render_thread.context.setShareContext( current )
            self.render_thread.context.create()
            self.render_thread.context.moveToThread( self.render_thread )

            current.makeCurrent( self.window() )

            #self.ready()
            #QtCore.QMetaObject.invokeMethod( self, "ready" )
            return None

        if old_node == None:
            node = TextureNode( self.window() )

            self.render_thread.textureReady.connect( node.newTexture, QtCore.Qt.DirectConnection )
            node.pendingNewTexture.connect( self.window().update, QtCore.Qt.QueuedConnection )
            self.window().beforeRendering.connect( node.prepareNode, QtCore.Qt.DirectConnection )
            node.textureInUse.connect( self.render_thread.renderNext, QtCore.Qt.QueuedConnection )

            # Get the production of FBO textures started..
            QtCore.QMetaObject.invokeMethod( self.render_thread, "renderNext", QtCore.Qt.QueuedConnection )

        node.setRect( self.boundingRect() )
        print(type(node))
        return node
