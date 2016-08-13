import QtQuick 2.3
import QtCharts 2.1

Rectangle {
    width: 800
    height: 600

    ChartView {
        anchors.fill: parent
        antialiasing: true
        animationOptions: ChartView.AllAnimations
        title: "Chart"

        LineSeries {
            name: "Line 1"
            VXYModelMapper {
                model: myModel
                xColumn: 0
                yColumn: 1
            }
        }

        LineSeries {
            name: "Line 2"
            VXYModelMapper {
                model: myModel
                xColumn: 2
                yColumn: 3
            }
        }
    }
}
