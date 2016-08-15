# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtWidgets, QtQuick
import custom_model

if __name__ == '__main__':
    app = QtWidgets.QApplication( sys.argv )

    view = QtQuick.QQuickView()#main_window.MainWindow()

    my_model = custom_model.CustomModel()

    view.rootContext().setContextProperty( 'myModel', my_model )
    view.setSource( QtCore.QUrl( "main.qml" ) )
    view.show()

    sys.exit( app.exec_() )
