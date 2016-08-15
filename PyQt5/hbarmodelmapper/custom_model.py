# -*- coding: utf-8 -*-

from PyQt5 import QtCore

class CustomModel( QtCore.QAbstractTableModel ):

    def __init__( self, parent=None ):
        super().__init__( parent )

        self.column_count = 7
        self.row_count = 3
        self.data = [
            [ "Bob", 2, 2, 3, 4, 5, 6 ],
            [ "Susan", 5, 1, 2, 4, 1, 7 ],
            [ "James", 3, 5, 8, 13, 5, 8 ]
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

    def headerData( self, section, orientation, role ):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.data[ 0 ][ section ]
            else:
                return self.data[ section ][ 0 ]
        elif role == QtCore.Qt.EditRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.data[ 0 ][ section ]
            else:
                return self.data[ section ][ 0 ]
        elif role == QtCore.Qt.BackgroundRole:
            return QtGui.QColor( QtCore.Qt.white )
        return QtCore.QVariant()
