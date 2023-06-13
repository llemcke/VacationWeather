# VacationWeather
Webapp that allows user to check multiple locations for historical weather data for planning a vacation 

June 13th:
First step to pull data from API is done. 
Calculating averages of weather data for past 5 years is done.
Issues so far: 
-Calls for checks are expensive. One week check for one location is 8 calls* 5 years... 40 calls per location.
Ideas to mitigate issues:
-Create test API to store some data for testing 
-Stop making calls and hardcode in data for now since the API calls have proven to work so far.
