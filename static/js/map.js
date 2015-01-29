/**
 * Created by piratos on 12/29/14.
 */
function drawmap(data) {

    // Initiate the chart
    $('#container').highcharts('Map', {

        title : {
            text : 'البلاغات حسب الولايات'
        },

        subtitle : {
            text : 'Source map: <a href="/static/js/tn-all.js">Tunisia</a>'
        },

        mapNavigation: {
            enabled: true,
            buttonOptions: {
                verticalAlign: 'bottom'
            }
        },

        colorAxis: {
            min: 0
        },

        series : [{
            data : data,
            mapData: Highcharts.maps['countries/tn/tn-all'],
            joinBy: 'hc-key',
            name: 'Random data',
            states: {
                hover: {
                    color: '#BADA55'
                }
            },
            dataLabels: {
                enabled: true,
                format: '{point.name}'
            }
        }]
    });
}
drawmap();
