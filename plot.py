from pandas import *
from ggplot import *
import pandas


 

   
pandas.options.mode.chained_assignment = None
turnstile_weather = pandas.read_csv('C:\Users\yxl\Desktop\urnstile_weather_v2.csv')
print turnstile_weather['ENTRIESn_hourly']
#ggplot(aes(x = 'ENTRIESn_hourly'), data = turnstile_weather)
#qplot(x='ENTRIESn_hourly', data=turnstile_weather, geom="histogram")
#ggplot(turnstile_weather,aes('rain','ENTRIESn_hourly'))+geom_point()+geom_line()
print ggplot(aes(x = 'ENTRIESn_hourly'), data = turnstile_weather[turnstile_weather['rain']==0])  + geom_histogram(binwidth = 2000) +scale_x_continuous(limits=(0,35000))+ggtitle('Ridership in rainy day')
print ggplot(aes(x = 'ENTRIESn_hourly'), data = turnstile_weather[turnstile_weather['rain']==1])  + geom_histogram(binwidth = 2000) +scale_x_continuous(limits=(0,35000))+ggtitle('Ridership in no rain day')
    
 
