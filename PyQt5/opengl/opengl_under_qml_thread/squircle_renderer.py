# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtQuick

class SquircleRenderer( QtCore.QObject ):
    def __init__( self ):
        super().__init__()

        self.profile = QtGui.QOpenGLVersionProfile()
        self.profile.setVersion( 2, 1 )
        self.gl = None
        self.viewportSize = QtCore.QSize()
        self.t = 0.0
        self.program = None
        self.window = None

    def setT( self, t ):
        self.t = t

    def setViewportSize( self, size ):
        self.viewportSize = size

    def setWindow( self, window ):
        self.window = window

    def initialize( self ):
        if self.window != None:
            self.gl = self.window.openglContext().versionFunctions( self.profile )

            self.program = QtGui.QOpenGLShaderProgram()
            self.program.addCacheableShaderFromSourceCode( QtGui.QOpenGLShader.Vertex, "attribute highp vec4 vertices;varying highp vec2 coords;void main() { gl_Position = vertices; coords = vertices.xy;}" )
            self.program.addCacheableShaderFromSourceCode( QtGui.QOpenGLShader.Fragment, "uniform lowp float t; varying highp vec2 coords; void main() { lowp float i = 1. - (pow(abs(coords.x), 4.) + pow(abs(coords.y), 4.)); i = smoothstep(t - 0.8, t + 0.8, i); i = floor(i * 20.) / 20.; gl_FragColor = vec4(coords * .5 + .5, i, i);}" )
            self.program.bindAttributeLocation( "vertices", 0 )
            self.program.link()

    def render( self ):
        if self.program == None:
            self.initialize()
        self.gl.glClearColor( 0, 0, 0, 1 )
        self.gl.glClear( self.gl.GL_COLOR_BUFFER_BIT )
        self.gl.glDisable( self.gl.GL_DEPTH_TEST )

        values = [ [ -1.0, -1.0 ], [ 1.0, -1.0 ], [ -1.0, 1.0 ], [ 1.0, 1.0 ] ]

        self.program.bind()
        self.program.enableAttributeArray( 0 )
        self.program.setAttributeArray( 0, values )
        self.program.setUniformValue( "t", self.t )

        self.gl.glEnable( self.gl.GL_BLEND )
        self.gl.glBlendFunc( self.gl.GL_SRC_ALPHA, self.gl.GL_ONE )

        self.gl.glDrawArrays( self.gl.GL_TRIANGLE_STRIP, 0, 4 )

        self.program.disableAttributeArray( 0 )
        self.program.release()
