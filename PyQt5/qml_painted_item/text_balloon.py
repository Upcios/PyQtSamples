# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtQuick

class TextBalloon( QtQuick.QQuickPaintedItem ):
    rightAlignedChanged = QtCore.pyqtSignal()

    def __init__( self, parent=None ):
        super().__init__( parent )

        self._rightAligned = False

    @QtCore.pyqtProperty( bool, notify=rightAlignedChanged )
    def rightAligned( self ):
        return self._right_aligned

    @rightAligned.setter
    def rightAligned( self, value ):
        self._right_aligned = value
        self.rightAlignedChanged.emit()

    def boundingRect( self ):
        return QtCore.QRectF( 0, 0, self.width(), self.height() )

    def paint( self, painter ):
        brush = QtGui.QBrush( QtGui.QColor( "#007430" ) )

        painter.setBrush( brush )
        painter.setPen( QtCore.Qt.NoPen )
        painter.setRenderHint( QtGui.QPainter.Antialiasing )

        painter.drawRoundedRect( 0, 0, self.boundingRect().width(), self.boundingRect().height() - 10, 10, 10 )

        if self.rightAligned:
            points = []
            points.append( QtCore.QPointF( self.boundingRect().width() - 10.0, self.boundingRect().height() - 10.0 ) )
            points.append( QtCore.QPointF( self.boundingRect().width() - 20.0, self.boundingRect().height() ) )
            points.append( QtCore.QPointF( self.boundingRect().width() - 30.0, self.boundingRect().height() - 10.0 ) )
            #needle = QtCore.Qt.QPolygon(points)
            painter.drawConvexPolygon( QtGui.QPolygonF(points) )
        else:
            points = []
            points.append( QtCore.QPointF( 10.0, self.boundingRect().height() - 10.0 ) )
            points.append( QtCore.QPointF( 20.0, self.boundingRect().height() ) )
            points.append( QtCore.QPointF( 30.0, self.boundingRect().height() - 10.0 ) )
            painter.drawConvexPolygon( QtGui.QPolygonF(points) )
