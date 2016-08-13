# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtChart

class CustomModel( QtCore.QAbstractTableModel ):

    def __init__( self, parent=None ):
        super().__init__( parent )

        self.column_count = 4
        self.row_count = 15
        self.data = [
            [ 19, 73, 16, 92 ],
            [ 68, 62, 58, 76 ],
            [ 115, 14, 111, 18 ],
            [ 153, 45, 165, 16 ],
            [ 217, 39, 207, 61 ],
            [ 265, 53, 255, 68 ],
            [ 302, 52, 312, 81 ],
            [ 360, 4, 364, 48 ],
            [ 419, 72, 416, 8 ],
            [ 458, 66, 466, 4 ],
            [ 502, 78, 515, 0 ],
            [ 558, 14, 553, 54 ],
            [ 616, 53, 606, 22 ],
            [ 657, 80, 661, 95 ],
            [ 700, 24, 704, 7 ]
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
