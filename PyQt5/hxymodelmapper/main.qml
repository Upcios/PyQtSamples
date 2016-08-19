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
            HXYModelMapper {
                model: myModel
                xRow: 0
                yRow: 1
            }
        }

        LineSeries {
            name: "Line 2"
            HXYModelMapper {
                model: myModel
                xRow: 2
                yRow: 3
            }
        }
    }
}
