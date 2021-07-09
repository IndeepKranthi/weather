# weather
Weather Data

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
