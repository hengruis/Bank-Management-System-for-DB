// Empty JS for your own code to be here
var chart1 = Highcharts.chart('container-savings-month', {
    data: {
        table: 'datatable-savings-month'
    },
    chart :{
        type: 'spline'
    },
    title: {
        text: '各支行业务储蓄总金额(月)'
    },
    yAxis: {
        allowDecimals: true,
        title: {
            text: '储蓄金'
        }
    },
    xAxis: {
        allowDecimals: false
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },
    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 1
        }
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' + this.point.y;
        }
    },
    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }
});

var chart2 = Highcharts.chart('container-loans-month', {
    data: {
        table: 'datatable-loans-month'
    },
    chart :{
        type: 'spline'
    },
    title: {
        text: '各支行业务贷款总金额(月)'
    },
    yAxis: {
        allowDecimals: true,
        title: {
            text: '贷款金额'
        }
    },
    xAxis: {
        allowDecimals: false
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },
    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 1
        }
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' + this.point.y;
        }
    },
    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }
});

var chart3 = Highcharts.chart('container-clients-month', {
    data: {
        table: 'datatable-clients-month'
    },
    chart :{
        type: 'spline'
    },
    title: {
        text: '各支行总用户数(月)'
    },
    yAxis: {
        allowDecimals: false,
        title: {
            text: '用户数'
        }
    },
    xAxis: {
        allowDecimals: false
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },
    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 1
        }
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' + this.point.y;
        }
    },
    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }
});

var chart4 = Highcharts.chart('container-savings-quarter', {
    data: {
        table: 'datatable-savings-quarter'
    },
    chart :{
        type: 'spline'
    },
    title: {
        text: '各支行业务储蓄总金额(季)'
    },
    yAxis: {
        allowDecimals: true,
        title: {
            text: '储蓄金'
        }
    },
    xAxis: {
        allowDecimals: false
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },
    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 1
        }
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' + this.point.y;
        }
    },
    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }
});

var chart5 = Highcharts.chart('container-loans-quarter', {
    data: {
        table: 'datatable-loans-quarter'
    },
    chart :{
        type: 'spline'
    },
    title: {
        text: '各支行业务贷款总金额(季)'
    },
    yAxis: {
        allowDecimals: true,
        title: {
            text: '贷款金额'
        }
    },
    xAxis: {
        allowDecimals: false
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },
    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 1
        }
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' + this.point.y;
        }
    },
    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }
});

var chart6 = Highcharts.chart('container-clients-quarter', {
    data: {
        table: 'datatable-clients-quarter'
    },
    chart :{
        type: 'spline'
    },
    title: {
        text: '各支行总用户数(季)'
    },
    yAxis: {
        allowDecimals: false,
        title: {
            text: '用户数'
        }
    },
    xAxis: {
        allowDecimals: false
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },
    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 1
        }
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' + this.point.y;
        }
    },
    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }
});

var chart7 = Highcharts.chart('container-savings-year', {
    data: {
        table: 'datatable-savings-year'
    },
    chart :{
        type: 'spline'
    },
    title: {
        text: '各支行业务储蓄总金额(年)'
    },
    yAxis: {
        allowDecimals: true,
        title: {
            text: '储蓄金'
        }
    },
    xAxis: {
        allowDecimals: false
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },
    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 1
        }
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' + this.point.y;
        }
    },
    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }
});

var chart8 = Highcharts.chart('container-loans-year', {
    data: {
        table: 'datatable-loans-year'
    },
    chart :{
        type: 'spline'
    },
    title: {
        text: '各支行业务贷款总金额(年)'
    },
    yAxis: {
        allowDecimals: true,
        title: {
            text: '贷款金额'
        }
    },
    xAxis: {
        allowDecimals: false
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },
    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 1
        }
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' + this.point.y;
        }
    },
    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }
});

var chart9 = Highcharts.chart('container-clients-year', {
    data: {
        table: 'datatable-clients-year'
    },
    chart :{
        type: 'spline'
    },
    title: {
        text: '各支行总用户数(年)'
    },
    yAxis: {
        allowDecimals: false,
        title: {
            text: '用户数'
        }
    },
    xAxis: {
        allowDecimals: false
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },
    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 1
        }
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' + this.point.y;
        }
    },
    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }
});
