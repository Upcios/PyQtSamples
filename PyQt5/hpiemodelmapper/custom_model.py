# -*- coding: utf-8 -*-

from PyQt5 import QtCore

class CustomModel( QtCore.QAbstractTableModel ):

    def __init__( self, parent=None ):
        super().__init__( parent )

        self.column_count = 5
        self.row_count = 2
        self.data = [
            [ "Volkswagen", "Toyota", "Ford", "Skoda", "Volvo" ],
            [ 13.5, 10.9, 8.6, 8.2, 6.8 ]
        ]

    def rowCount( self, parent ):
        return len( self.data )

    def columnCount( self, parent ):
        return self.column_count

    def data( self, index, role ):
        if role == QtCore.Qt.DisplayRole:
            return self.data[ index.row() ][ index.column() ]
        elif role == QtCore.Qt.EditRole:
            return self.data[ index.row() ][ index.column() ]
        elif role == QtCore.Qt.BackgroundRole:
            return QtGui.QColor( QtCore.Qt.white )
        return QtCore.QVariant()
