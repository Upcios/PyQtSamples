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

        PieSeries {
            id: pieSeries

            HPieModelMapper {
                model: myModel
                labelsRow: 0
                valuesRow: 1
            }
        }
    }
}
