# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtQuick, QtQml
import squircle

if __name__ == '__main__':
    app = QtGui.QGuiApplication( sys.argv )

    QtQml.qmlRegisterType( squircle.Squircle, "OpenGLUnderQML", 1, 0, "Squircle" )

    view = QtQuick.QQuickView()

    # Rendering in a thread introduces a slightly more complicated cleanup
    # so we ensure that no cleanup of graphics resources happen until the
    # application is shutting down.
    view.setPersistentOpenGLContext( True )
    view.setPersistentSceneGraph( True )

    view.setResizeMode( QtQuick.QQuickView.SizeRootObjectToView )
    view.setSource( QtCore.QUrl( "main.qml" ) )
    view.show()

    execReturn = app.exec()

    # As the render threads make use of our QGuiApplication object
    # to clean up gracefully, wait for them to finish before
    # QGuiApp is taken off the heap.
    for t in squircle.Squircle.threads:
        t.wait()
        t = None

    sys.exit( execReturn )
