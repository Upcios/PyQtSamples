# -*- coding: utf-8 -*-

from PyQt5 import QtCore

class CustomModel( QtCore.QAbstractTableModel ):

    def __init__( self, parent=None ):
        super().__init__( parent )

        self.column_count = 15
        self.row_count = 4
        self.data = [
            [ 19, 68, 115, 153, 217, 265, 302, 360, 419, 458, 502, 558, 616, 657, 700 ],
            [ 73, 62, 14, 45, 39, 53, 52, 4, 72, 66, 78, 14, 53, 80, 24 ],
            [ 16, 58, 111, 165, 207, 255, 312, 364, 416, 466, 515, 553, 606, 661, 704 ],
            [ 92, 76, 18, 16, 61, 68, 81, 48, 8, 4, 0, 54, 22, 95, 7 ]
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
