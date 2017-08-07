# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtQuick
import squircle_renderer

class Squircle( QtQuick.QQuickItem ):
    tChanged = QtCore.pyqtSignal()

    def __init__( self, parent=None ):
        super().__init__( parent )

        self.renderer = None
        self._t = 0.0

        self.windowChanged.connect( self.handleWindowChanged )

    @QtCore.pyqtProperty( float, notify=tChanged )
    def t( self ):
        return self._t

    @t.setter
    def t( self, value ):
        if self._t == value:
            return
        self._t = value
        self.tChanged.emit()
        if self.window():
            self.window().update()

    def sync( self ):
        if self.renderer == None:
            self.renderer = squircle_renderer.SquircleRenderer()
            self.window().beforeRendering.connect( self.renderer.render, QtCore.Qt.DirectConnection )
        self.renderer.setViewportSize( self.window().size() * self.window().devicePixelRatio() )
        self.renderer.setT( self.t )
        self.renderer.setWindow( self.window() )

    def cleanup( self ):
        if self.renderer != None:
            self.renderer = None

    def handleWindowChanged( self, win ):
        if win:
            win.beforeSynchronizing.connect( self.sync, QtCore.Qt.DirectConnection )
            win.sceneGraphInvalidated.connect( self.cleanup, QtCore.Qt.DirectConnection )
            win.setClearBeforeRendering( False )
