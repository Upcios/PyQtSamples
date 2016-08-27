# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtWidgets, QtGui
import numpy
import math as M

class TextureUploader( QtCore.QObject ):
    texture_generated = QtCore.pyqtSignal( int, int, int, name="textureGenerated" )

    def __init__( self, format=None, shared=False ):
        super().__init__()

        self.profile = QtGui.QOpenGLVersionProfile()
        self.profile.setVersion( 2, 1 )

        self.palette = QtGui.QImage( "../../../Screenshots/palette.ppm" )
        self.image_width = 800
        self.image_height = 600
        self.timer = QtCore.QElapsedTimer()
        self.timer.start()
        self.iter = 60

        if format == None:
            self.format = QtGui.QSurfaceFormat()
            self.format.setVersion( 4, 5 )
            self.format.setSamples( 8 )
            self.format.setProfile( QtGui.QSurfaceFormat.CompatibilityProfile )
        else:
            self.format = format

        # If local context must be shared with another context, we will
        # create it later (see main.py).
        if not shared:
            self.context = QtGui.QOpenGLContext()
            self.context.setFormat( self.format )
            self.context.create()
        else:
            self.context = None

        self.surface = QtGui.QOffscreenSurface()
        self.surface.setFormat( self.format )
        self.surface.create()

        self.init = False

    @QtCore.pyqtSlot( QtGui.QOpenGLContext )
    def setSharedContext( self, other_context ):
        self.context = QtGui.QOpenGLContext()
        self.context.setShareContext( other_context )
        self.context.setFormat( self.format )
        self.context.create()

    def initRender( self ):
        if self.context != None and self.init == False:
            self.context.makeCurrent( self.surface )

            self.gl = self.context.versionFunctions( self.profile )
            self.gl.initializeOpenGLFunctions()

            self.fbo = QtGui.QOpenGLFramebufferObject( self.image_width, self.image_height )
            self.vao_offscreen = QtGui.QOpenGLVertexArrayObject( self )
            self.vao_offscreen.create()
            self.texture = QtGui.QOpenGLTexture( QtGui.QOpenGLTexture.Target1D )
            self.texture.setData( self.palette, QtGui.QOpenGLTexture.DontGenerateMipMaps )

            self.program = QtGui.QOpenGLShaderProgram( self )
            self.program.addShaderFromSourceFile( QtGui.QOpenGLShader.Vertex, 'simple_texture.vs' )
            self.program.addShaderFromSourceFile( QtGui.QOpenGLShader.Fragment, 'julia_texture.fs' )
            self.program.link()

            self.program.bind()
            self.matrix = QtGui.QMatrix4x4()
            self.matrix.ortho( 0, 1, 0, 1, 0, 1 )
            self.program.setUniformValue( "mvp", self.matrix )
            self.program.setUniformValue( "iter", self.iter )
            self.program.release()

            # offscreen render
            self.vao_offscreen.bind()
            self.vertices = [ 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0 ]
            self.vbo_vertices = self.setVertexBuffer( self.vertices, 3, self.program, "position" )
            self.tex = [ 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0 ]
            self.vbo_tex = self.setVertexBuffer( self.tex, 2, self.program, "texCoord" )
            self.vao_offscreen.release()

            self.init = True

    @QtCore.pyqtSlot()
    def render( self ):
        if self.context != None:
            if self.init == False:
                self.initRender()

            self.context.makeCurrent( self.surface )
            self.gl.glViewport( 0, 0, self.image_width, self.image_height )

            self.program.bind()
            t = self.timer.elapsed() / 1000.0
            cx = ( M.sin( M.cos( t / 10 ) * 10 ) + M.cos( t * 2.0 ) / 4.0 + M.sin( t * 3.0) / 6.0 ) * 0.8
            cy = ( M.cos( M.sin( t / 10 ) * 10 ) + M.sin( t * 2.0 ) / 4.0 + M.cos( t * 3.0) / 6.0 ) * 0.8
            self.program.setUniformValue( "c", cx, cy )

            self.texture.bind()
            self.fbo.bind()
            self.vao_offscreen.bind()
            self.gl.glDrawArrays( self.gl.GL_TRIANGLE_STRIP, 0, 4 )
            self.vao_offscreen.release()
            self.fbo.release()
            self.texture.release()
            self.program.release()

            self.texture_generated.emit( self.fbo.texture(), self.fbo.width(), self.fbo.height() )

    def setVertexBuffer( self, data_array, dim_vertex, program, shader_str ):
        vbo = QtGui.QOpenGLBuffer( QtGui.QOpenGLBuffer.VertexBuffer )
        vbo.create()
        vbo.bind()

        vertices = numpy.array( data_array, numpy.float32 )
        vbo.allocate( vertices, vertices.shape[0] * vertices.itemsize )

        attr_loc = program.attributeLocation( shader_str )
        program.enableAttributeArray( attr_loc )
        program.setAttributeBuffer( attr_loc, self.gl.GL_FLOAT, 0, dim_vertex )
        vbo.release()

        return vbo
