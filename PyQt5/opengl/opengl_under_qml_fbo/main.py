# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtQuick, QtQml
import squircle

if __name__ == '__main__':
    app = QtGui.QGuiApplication( sys.argv )

    QtQml.qmlRegisterType( squircle.Squircle, "OpenGLUnderQML", 1, 0, "Squircle" )

    view = QtQuick.QQuickView()
    view.setResizeMode( QtQuick.QQuickView.SizeRootObjectToView )
    view.setSource( QtCore.QUrl( "main.qml" ) )
    view.show()

    sys.exit( app.exec_() )
