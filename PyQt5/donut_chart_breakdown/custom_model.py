# -*- coding: utf-8 -*-

from PyQt5 import QtCore

class CustomModel( QtCore.QAbstractTableModel ):

    def __init__( self, parent=None ):
        super().__init__( parent )

        self.column_count = 2
        self.row_count = 10
        self.data = [
            [ "Oil", 353295 ],
            [ "Coal", 188500 ],
            [ "Natural gas", 148680 ],
            [ "Peat", 94545 ],

            [ "Wood fuels", 319663 ],
            [ "Hydro power", 45875 ],
            [ "Wind power", 1060 ],

            [ "Nuclear energy", 238789 ],
            [ "Import energy", 37802 ],
            [ "Other", 32441 ]
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
