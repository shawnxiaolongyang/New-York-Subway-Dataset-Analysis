from pandas import *
from ggplot import *
import pandasql
import pandas
import time  
from datetime import datetime,date



pandas.options.mode.chained_assignment = None
turnstile_weather = pandas.read_csv('C:\Users\yxl\Desktop\urnstile_weather_v2.csv')


turnstile_weather.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)
    
p = """
select
DATEn
from turnstile_weather   
"""
a = pandasql.sqldf(p, locals())
b = [0]*(len(a))
c = [0]*(len(a))
i=1
print a['daten']
for i in range(len(a)):
    b[i] = time.strptime(a['daten'][i],"%Y-%m-%d")
    b[i] = date(b[i].tm_year,b[i].tm_mon,b[i].tm_mday)
    if b[i].weekday()==0:
        c[i]='sunday'
    if b[i].weekday()==1:
        c[i]='monday'
    if b[i].weekday()==2:
        c[i]='tuesday'
    if b[i].weekday()==3:
        c[i]='wednesday'
    if b[i].weekday()==4:
        c[i]='thursday'
    if b[i].weekday()==5:
        c[i]='friday'
    if b[i].weekday()==6:
        c[i]='saturday'
c[0]='weekday'

        
    
turnstile_weather['weekday'] = c
    
    
    
q = """
select
weekday,UNIT,sum(exitsn_hourly)
from turnstile_weather  
group by weekday,UNIT;  

"""
turnstile_weather = pandasql.sqldf(q, locals())
print ggplot(turnstile_weather,aes(x = 'weekday', y = 'sum(exitsn_hourly)'))+geom_bar(stat = "identity")+ggtitle('Ridership by day of week')

   
    

     
    
