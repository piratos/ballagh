/**
 * Created by piratos on 12/29/14.
 */

function plot_status_stat(baseConfig, data_status){
    var statusd = {
        title: {
            text: ''
        },
        series: [{
            name: 'pourcentage',
            type: 'pie',
            data: data_status
        }]};
    data_status = statusd
    $('#status_container').highcharts(
                $.extend(baseConfig, data_status)
            );

}

function plot_type_stat(baseConfig, data_type){

    var typed = {
        title: {
            text: ''
        },
        series: [{
            name: 'النسبة',
            type: 'pie',
            data: data_type
        }]};
    data_type = typed
    $('#type_container').highcharts(
                $.extend(baseConfig, data_type)
            );

}

function getdata(){
    var sdata;
             $.ajax({
        url: '/reports/vstat',
        type: 'get',
        dataType: 'json',
        async: false,
        success: function(data) {
            sdata = data;
        }
         });
    var typer = sdata[1];
    var status = sdata[2];
    var gov = sdata[3];
    var govData = []
    for (var i = 0; i<gov.length;i++){
        var g = {};
        g["hc-key"] = gov[i][0];
        g["value"] = gov[i][1];
        govData.push(g);
    }
    console.log(govData);


var baseConfig = {
    credits: {
        enabled: false
    },
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage}%</b>',
        percentageDecimals: 1
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                color: '#000000',
                connectorColor: '#000000',
                formatter: function() {
                    return '<b>'+ this.point.name +'</b>: '+ this.y;
                }
            }
        }
    }
};
    plot_type_stat(baseConfig, typer);
    plot_status_stat(baseConfig, status);
    drawmap(govData);
}