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

        BarSeries {
            id: mySeries
            axisX: BarCategoryAxis { categories: ["2007", "2008", "2009", "2010", "2011", "2012" ] }
            HBarModelMapper {
                model: myModel
                firstBarSetRow: 0
                lastBarSetRow: 2
                firstColumn: 1

            }
        }
    }
}
