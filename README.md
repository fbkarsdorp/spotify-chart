# Spotify Charts

Simple script to get chart data from Spotify via https://spotifycharts.com 

# Examples

## As a module 

To retrieve charts for single dates or weeks, use the `charts.get_chart` function:

``` python
>>> import charts
...
>>> chart = charts.get_chart('2018-01-01', region='nl')
>>> chart.head()
   Position           Track Name          Artist  Streams  \
0         1        Blijf Bij Mij     Ronnie Flex   166369   
1         2  4/5 - From “Patser"     Ronnie Flex   144792   
2         3            Officieel   Broederliefde   121677   
3         4               Havana  Camila Cabello   107151   
4         5             rockstar     Post Malone    95755   

                                                 URL  
0  https://open.spotify.com/track/7EyvmcYx7WzeBi2...  
1  https://open.spotify.com/track/7cAxokBbnclXF6s...  
2  https://open.spotify.com/track/3e0gMtgOOLGPFLz...  
3  https://open.spotify.com/track/0ofbQMrRDsUaVKq...  
4  https://open.spotify.com/track/7wGoVu4Dady5GV0...  
```

To retrieve charts for a date range, use the `charts.get_charts` function:

``` python
>>> import charts
...
>>> chart = charts.get_charts('2018-01-01', '2018-02-01', freq='weekly', region='global')
>>> chart.head()
   Position                Track Name          Artist   Streams  \
0         1                  rockstar     Post Malone  29389063   
1         2                    Havana  Camila Cabello  25726393   
2         3  River (feat. Ed Sheeran)          Eminem  23547146   
3         4                 New Rules        Dua Lipa  20861932   
4         5                    Wolves    Selena Gomez  20579700   

                                                 URL       date  
0  https://open.spotify.com/track/7wGoVu4Dady5GV0... 2018-01-07  
1  https://open.spotify.com/track/0ofbQMrRDsUaVKq... 2018-01-07  
2  https://open.spotify.com/track/5UEnHoDYpsxlfzW... 2018-01-07  
3  https://open.spotify.com/track/2ekn2ttSfGqwhha... 2018-01-07  
4  https://open.spotify.com/track/7EmGUiUaOSGDnUU... 2018-01-07  
```

## From the Commandline

``` shell
usage: charts.py [-h] --start_date START_DATE --outfile OUTFILE
                 [--end_date END_DATE] [--region REGION]
                 [--freq {daily,weekly}] [--chart {top200,viral}]

optional arguments:
  -h, --help            show this help message and exit
  --start_date START_DATE
                        A date defining the start day for the chart.
  --outfile OUTFILE     Save the results in this file.
  --end_date END_DATE   A date defining the end day for the chart.
  --region REGION       A region defined for the chart.
  --freq {daily,weekly}
                        Use timestamps on a weekly or daily frequency.
  --chart {top200,viral}
                        The type of chart to retrieve.
```
