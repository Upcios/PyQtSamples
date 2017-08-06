# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtWidgets, QtQuick, QtQml
import text_balloon

if __name__ == '__main__':
    app = QtWidgets.QApplication( sys.argv )

    view = QtQuick.QQuickView()

    QtQml.qmlRegisterType(text_balloon.TextBalloon, "Custom", 1, 0, "TextBalloon")

    view.setSource( QtCore.QUrl( "main.qml" ) )
    view.show()

    sys.exit( app.exec_() )
