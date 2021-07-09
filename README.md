# weather
**Weather.py** - # Python file to weather from Detroit,Michigan & Seattle every day for 1 week.

**Public Rest API** - # http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=17bc6cb91f7c417995725713210907&q=Detroit&format=json&date=2021-06-29&enddate=2021-06-30&tp=24Time

**S3 Bucket** - # weatherdataa (access to public)

**DDL for Specturm table** - (external table)
CREATE EXTERNAL TABLE schemaname.weather_pxf(
date_time Date,
maxtempC int,
mintempC int,
totalSnow_cm int,
sunHour numeric,
uvIndex int,
moon_illumination int,
moonrise varchar(10),
moonset varchar(10),
sunrise varchar(10),
sunset varchar(10),
DewPointC int,
FeelsLikeC int, 
HeatIndexC int,
WindChillC int,
WindGustKmph int,
cloudcover int,
humidity int,
precipMM numeric, 
pressure int,
tempC int,
visibility int,
winddirDegree int,
windspeedKmph int,
location varchar(24)
) 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' 
STORED AS TEXTFILE 
LOCATION 's3://weatherdataa/*' TABLE PROPERTIES ('skip.header.line.count'='1');

**DDL for Redshift table** - (internal table)
CREATE TABLE schemaname.Weather(
date_time Date,
maxtempC int,
mintempC int,
totalSnow_cm int,
sunHour numeric,
uvIndex int,
moon_illumination int,
moonrise varchar(10),
moonset varchar(10),
sunrise varchar(10),
sunset varchar(10),
DewPointC int,
FeelsLikeC int, 
HeatIndexC int,
WindChillC int,
WindGustKmph int,
cloudcover int,
humidity int,
precipMM numeric, 
pressure int,
tempC int,
visibility int,
winddirDegree int,
windspeedKmph int,
location varchar(24)
) 
WITH (APPENDONLY=TRUE,
    COMPRESSTYPE = ZLIB,
    COMPRESSLEVEL = 5)
DISTRIBUTED RANDOMLY;

**COPY COMMAND TO LOAD DATA FROM s3 to redshift table**
COPY schemaname.weather from 's3://weatherdataa/*'
credentials 'aws_iam_role=arn:aws:iam::*********:role/*******' delimiter '\054' BZIP2   (\054 is comma delimiter)


df_month - # initialize df_month to store return data
hourly_df - # hourly data; temperature for each hour of the day

Used boto3 for accessing S3 from python

#Values
frequency=24                                     #  day frequency
start_date = '29-JUN-2021'						# start_date to retrieve from a month
end_date = '09-JUL-2021'						# to what date 
api_key = '17bc6cb91f7c417995725713210907'     # Key to access api
location_list = ['Detroit','Seattle']    # cities.

Given Access_key_id & aws_secret_access_key

#Captured Weather History Data for a month into Data Frame

# Given location and dates between for 2 cities
