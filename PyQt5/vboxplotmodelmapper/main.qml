import QtQuick 2.3
import QtCharts 2.1

Rectangle {
    width: 800
    height: 600

    ChartView {
        anchors.fill: parent
        antialiasing: true
        theme: ChartView.ChartThemeBrownSand
        animationOptions: ChartView.AllAnimations
        title: "Chart"

        BoxPlotSeries {
            name: "Income"
            axisX: BarCategoryAxis { categories: ["Jan", "Feb", "Mar", "Apr", "May" ] }
            VBoxPlotModelMapper {
                model: myModel
                firstBoxSetColumn: 0
                lastBoxSetColumn: 4
                firstRow: 0//1
            }
        }
    }
}
