# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
import numpy

class MyOpenGLWindow( QtGui.QOpenGLWindow ):
    def __init__( self ):
        super().__init__()
        self.profile = QtGui.QOpenGLVersionProfile()
        self.profile.setVersion( 2, 1 )

    def initializeGL( self ):
        self.gl = self.context().versionFunctions( self.profile )
        self.vao = QtGui.QOpenGLVertexArrayObject( self )
        self.vao.create()

        self.program = QtGui.QOpenGLShaderProgram( self )
        self.program.addShaderFromSourceFile( QtGui.QOpenGLShader.Vertex, 'simple.vs' )
        self.program.addShaderFromSourceFile( QtGui.QOpenGLShader.Fragment, 'simple.fs' )
        self.program.link()

        self.vao.bind()
        self.vertices = [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 1.0, 0.0]
        self.vbo_vertices = self.setVertexBuffer( self.vertices, 3, self.program, "position" )
        self.colors = [1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0]
        self.vbo_colors = self.setVertexBuffer( self.colors, 4, self.program, "color" )
        self.vao.release()

        self.program.bind()
        self.matrix = QtGui.QMatrix4x4()
        self.matrix.ortho( 0, 1, 0, 1, 0, 1 )
        self.program.setUniformValue( "mvp", self.matrix )
        self.program.release()

    def paintGL( self ):
        self.program.bind()

        self.vao.bind()
        self.gl.glDrawArrays( self.gl.GL_TRIANGLES, 0, 3 )
        self.vao.release()

        self.program.release()

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

if __name__ == '__main__':
    app = QtWidgets.QApplication( sys.argv )

    window = MyOpenGLWindow()
    window.resize( 800, 600 )
    window.show()

    app.exec_()

