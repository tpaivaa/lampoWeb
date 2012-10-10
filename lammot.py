# -*- coding: iso-8859-15 -*-from pymongo.connection import Connection
from pymongo.connection import Connection
connection = Connection("10.10.10.55")
from datetime import timedelta, datetime 
lampotiladb = connection.Soittila_lampotilat
reledb = connection.Soittila_releet

def getsoile():
    html = '''<html><head>
                <!--Load the AJAX API-->
                <script type="text/javascript" src="https://www.google.com/jsapi"></script>
                <script type="text/javascript">
                    google.load('visualization', '1.0', {'packages':['corechart']});
                    google.setOnLoadCallback(drawChartAll);
                        function drawChart() {
                           var data = google.visualization.arrayToDataTable([
                            ['Day', 'Fat burn', 'Fitness'],
                            ['02.09.2012',11.43 ,49.23],
                            ['04.09.2012',10.59 ,45.35],
                            ['08.09.2012',4.57 ,60.42],
                            ['10.09.2012',6.27 ,58.16],
                            ['11.09.2012',5.26 ,60.41],
                            ['14.09.2012',38.51 ,15.58],
                            ['16.09.2012',69.10 ,9.46],
                            ['17.09.2012',11.12 ,34.21],
                            ['18.09.2012',13.33, 53.30],
                            ['22.09.2012',12.47 ,53.21],
                            ['24.09.2012',21.08 ,43.38],
                            ['27.09.2012',5.29 ,28.43]                            
                            ]);
                  
                            var options = {
                              title: 'Soile Performance',
                              isStacked: true,
                              vAxis: {title: "Duration minutes"},
                              hAxis: {title: 'Day'}
                            };
                  
                            var chart = new google.visualization.ColumnChart(document.getElementById('kulutus_chart_div'));
                            chart.draw(data, options);
                        }
                        function sykedrawChart() {
                           var sykedata = google.visualization.arrayToDataTable([
                            ['Day', 'Average', 'Max'],
                            ['02.09.2012',140 ,174],
                            ['04.09.2012',141 ,184],
                            ['08.09.2012',145 ,176],
                            ['10.09.2012',144 ,171],
                            ['11.09.2012',145 ,187],
                            ['14.09.2012',114 ,172],
                            ['16.09.2012',105 ,129],
                            ['17.09.2012',129 ,161],
                            ['18.09.2012',131, 170],
                            ['22.09.2012',134 ,183],
                            ['24.09.2012',130 ,198],
                            ['27.09.2012',145 ,172]                            
                            ]);
                  
                            var sykeoptions = {
                                title: 'Hartbeat',
                                vAxis: {title: "Heartbeat / minute"},
                                hAxis: {title: "Day"}
                            };
                  
                            var sykechart = new google.visualization.ComboChart(document.getElementById('syke_chart_div'));
                            sykechart.draw(sykedata, sykeoptions);
                        }
                        function kaloritdrawChart() {
                           var kaloritdata = google.visualization.arrayToDataTable([
                            ['Day', 'Consumed calories'],
                            ['02.09.2012',495],
                            ['04.09.2012',463],
                            ['08.09.2012',567],
                            ['10.09.2012',548],
                            ['11.09.2012',568],
                            ['14.09.2012',302],
                            ['16.09.2012',365],
                            ['17.09.2012',314],
                            ['18.09.2012',484],
                            ['22.09.2012',496],
                            ['24.09.2012',459],
                            ['27.09.2012',294]                            
                            ]);
                  
                            var kaloritoptions = {title: 'Calories',
                                vAxis: {title: "Calories"},
                                hAxis: {title: "Day"}};
                            var kaloritchart = new google.visualization.LineChart(document.getElementById('kalorit_chart_div'));
                            kaloritchart.draw(kaloritdata, kaloritoptions);
                        }
                        
                        
                        function drawChartAll(){
                        drawChart();
                        sykedrawChart();
                        kaloritdrawChart();
                        }
                </script>
                </head>

                <body>
                <div id="kulutus_chart_div" style="width: 1000px; height: 500px;"></div>
                <div id="syke_chart_div" style="width: 1000px; height: 500px;"></div>
                <div id="kalorit_chart_div" style="width: 1000px; height: 500px;"></div>
                </body></html>'''
    return html


def weekAgo():
    sevendaysfromnow = datetime.now() - timedelta(days=7) #past 7 days
    aika = sevendaysfromnow.strftime("%Y.%m.%d-%H:%M:%S")
    return aika

def weekTemps(room):
    chart_data = []
    start = weekAgo()
    end = datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
    ll = lampotiladb.Soittila_lampotilat.find({'anturi': room, 'date' : {'$gt': start}})
    
    for n in ll:
        stamp = datetime.fromtimestamp(n[str(u'stamp')]).strftime('%d.%m.%Y-%H:%M:%S')
        #chart_data[stamp] = n[u'lampotila']
        chart_data.append([stamp, n[u'lampotila']])
        
    chart_data.insert(0, ['Päivä', room ])
    return chart_data    
    
def getlampotila():
    khh_chart_data = weekTemps('khh')
    olohuone_chart_data = weekTemps('olohuone')
    ulkosauna_chart_data = weekTemps('Ulkosauna')
    html ='''<html>
  <head>
    <script type="text/javascript" src="scripts/jquery.js"></script>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChartAll);
      function drawChartkhh() {
        var khhdata = google.visualization.arrayToDataTable('''
    html += str(khh_chart_data)    
    html += ''');
    var khhoptions = {title: 'khh'};
    var khhchart = new google.visualization.AreaChart(document.getElementById('khh_chart_div'));
    khhchart.draw(khhdata, khhoptions);
      }
      function drawChartolohuone() {
        var olohuonedata = google.visualization.arrayToDataTable('''
    html += str(olohuone_chart_data)    
    html += ''');

        
        var olohuoneoptions = {title: 'olohuone'};
        var olohuonechart = new google.visualization.AreaChart(document.getElementById('olohuone_chart_div'));
        olohuonechart.draw(olohuonedata, olohuoneoptions); 
      }
      
      function drawChartulkosauna() {
        var ulkosaunadata = google.visualization.arrayToDataTable('''
    html += str(ulkosauna_chart_data)    
    html += ''');

        
        var ulkosaunaoptions = {title: 'Pihasauna'};
        var ulkosaunachart = new google.visualization.AreaChart(document.getElementById('ulkosauna_chart_div'));
        Ulkosaunachart.draw(ulkosaunadata, ulkosaunaoptions); 
      }
      
      
      function drawChartAll(){
      drawChartolohuone();
      drawChartkhh();
      drawChartulkosauna();
      }
    </script>
  </head>
  <body>
    <div id="khh_chart_div" style="width: 800px; height: 200px;"></div>
    <div id="olohuone_chart_div" style="width: 800px; height: 200px;"></div>
    <div id="ulkosauna_chart_div" style="width: 800px; height: 200px;"></div>
  </body>
</html>'''
    return html