# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtQuick
import squircle_renderer

class SquircleInFboRenderer( QtQuick.QQuickFramebufferObject.Renderer ):
    def __init__( self ):
        super().__init__()

        self.squircle = squircle_renderer.SquircleRenderer()
        self.squircle.initialize()

    def render( self ):
        self.squircle.render()
        self.update()

    def createFrameBufferObject( self, size ):
        format = QtGui.QOpenGLFramebufferObjectFormat()
        format.setAttachment( QtGui.QOpenGLFramebufferObject.CombinedDepthStencil )
        format.setSamples( 4 )
        return QtGui.QOpenGLFramebufferObject( size, format )

class Squircle( QtQuick.QQuickFramebufferObject ):
    tChanged = QtCore.pyqtSignal()

    def __init__( self, parent=None ):
        super().__init__( parent )

        self.renderer = None

    @QtCore.pyqtProperty( float, notify=tChanged )
    def t( self ):
        if self.renderer == None:
            return 0.0
        else:
            return self.renderer.squircle.t

    @t.setter
    def t( self, value ):
        if self.renderer == None or self.renderer.squircle.t == value:
            return
        self.renderer.squircle.setT( value )
        self.tChanged.emit()
        if self.window():
            self.window().update()

    def createRenderer( self ):
        self.renderer = SquircleInFboRenderer()
        self.renderer.squircle.setWindow( self.window() )
        return self.renderer
