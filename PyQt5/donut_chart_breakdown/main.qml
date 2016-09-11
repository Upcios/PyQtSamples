import QtQuick 2.7
import QtCharts 2.1

Rectangle {
    width: 800
    height: 600

    Component.onCompleted: chart.recalculateAngles()

    ChartView {
        id: chart
        anchors.fill: parent
        antialiasing: true
        animationOptions: ChartView.AllAnimations
        title: "Total consumption of energy in Finland 2010"
        legend.alignment: Qt.AlignRight


        function recalculateAngles()
        {
            var angle = 0.0
            for ( var i = 0; i < 3; i++ )
            {
                if ( i == 0 )
                {
                    serie0.startAngle = angle
                    angle += mainSerie.at(i).percentage * 360.0
                    serie0.endAngle = angle
                }
                else if ( i == 1 )
                {
                    serie1.startAngle = angle
                    angle += mainSerie.at(i).percentage * 360.0
                    serie1.endAngle = angle
                }
                else if ( i == 2 )
                {
                    serie2.startAngle = angle
                    angle += mainSerie.at(i).percentage * 360.0
                    serie2.endAngle = angle
                }
            }
            update()
        }

        PieSeries {
            id: mainSerie
            size: 0.7
            visible: false

            PieSlice {
                id: slice0
                value: serie0.sum
                label: serie0.name+" "+parseFloat(percentage * 100.0).toFixed(2)+"%"
                color: "red"
                labelVisible: true
                labelColor: "white"
                labelPosition: PieSlice.LabelInsideHorizontal
                labelFont.family: "Arial"
                labelFont.pixelSize: 12
            }

            PieSlice {
                id: slice1
                value: serie1.sum
                label: serie1.name+" "+parseFloat(percentage * 100.0).toFixed(2)+"%"
                color: "darkGreen"
                labelVisible: true
                labelColor: "white"
                labelPosition: PieSlice.LabelInsideHorizontal
                labelFont.family: "Arial"
                labelFont.pixelSize: 12
            }

            PieSlice {
                id: slice2
                value: serie2.sum
                label: serie2.name+" "+parseFloat(percentage * 100.0).toFixed(2)+"%"
                color: "darkBlue"
                labelVisible: true
                labelColor: "white"
                labelPosition: PieSlice.LabelInsideHorizontal
                labelFont.family: "Arial"
                labelFont.pixelSize: 12
            }
        }

        PieSeries {
            id: serie0
            name: "Fossil fuels"
            size: 0.8
            holeSize: 0.7
            onSliceAdded: {
                slice.color = Qt.lighter(slice0.color, 1.5)
                slice.labelFont.family = "Arial"
                slice.labelFont.pixelSize = 12
                slice.labelVisible = true
//                if ( count == model0.rowCount )
//                {
//                    for (var i = 0; i < count; i++ )
//                        serie0.at(i).label = serie0.at(i).label+" "+parseFloat(serie0.at(i).percentage * 100.0).toFixed(2)+"%"
//                }
            }

            VPieModelMapper {
                id: model0
                model: myModel
                labelsColumn: 0
                valuesColumn: 1
                firstRow: 0
                rowCount: 4
            }
        }

        PieSeries {
            id: serie1
            name: "Renewables"
            size: 0.8
            holeSize: 0.7
            onSliceAdded: {
                slice.color = Qt.lighter(slice1.color, 1.5)
                slice.labelFont.family = "Arial"
                slice.labelFont.pixelSize = 12
                slice.labelVisible = true
//                if ( count == model1.rowCount )
//                {
//                    for (var i = 0; i < count; i++ )
//                        serie1.at(i).label = serie1.at(i).label+" "+parseFloat(serie1.at(i).percentage * 100.0).toFixed(2)+"%"
//                }
            }

            VPieModelMapper {
                id: model1
                model: myModel
                labelsColumn: 0
                valuesColumn: 1
                firstRow: 4
                rowCount: 3
            }
        }

        PieSeries {
            id: serie2
            name: "Others"
            size: 0.8
            holeSize: 0.7
            onSliceAdded: {
                slice.color = Qt.lighter(slice2.color, 1.5)
                slice.labelFont.family = "Arial"
                slice.labelFont.pixelSize = 12
                slice.labelVisible = true
//                if ( count == model2.rowCount )
//                {
//                    for (var i = 0; i < count; i++ )
//                        serie2.at(i).label = serie2.at(i).label+" "+parseFloat(serie2.at(i).percentage * 100.0).toFixed(2)+"%"
//                }
            }

            VPieModelMapper {
                id: model2
                model: myModel
                labelsColumn: 0
                valuesColumn: 1
                firstRow: 7
                rowCount: 3
            }
        }
    }
}
