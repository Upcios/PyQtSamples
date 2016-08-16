# -*- coding: utf-8 -*-

from PyQt5 import QtCore

class CustomModel( QtCore.QAbstractTableModel ):

    def __init__( self, parent=None ):
        super().__init__( parent )

        self.column_count = 5
        self.row_count = 5#6
        self.data = [
            #[ "Jan", "Feb", "Mar", "Apr", "May" ],
            [ 3, 5, 3.2, 3.8, 4 ],
            [ 4, 6, 5, 5, 5 ],
            [ 5.1, 7.5, 5.7, 6.4, 5.2 ],
            [ 6.2, 8.6, 8, 7, 7 ],
            [ 8.5, 11.8, 9.2, 8, 7 ]
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
