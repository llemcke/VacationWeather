# VacationWeather
Webapp that allows user to check multiple locations for historical weather data for planning a vacation 

**June 13th:**
First step to pull data from API is done. 
Calculating averages of weather data for past 5 years is done.
Issues so far: 
-Calls for checks are expensive. One week check for one location is 8 calls* 5 years... 40 calls per location.
Ideas to mitigate issues:
-Create test API to store some data for testing 
-Stop making calls and hardcode in data for now since the API calls have proven to work so far.

**July 25th:**
Pulling data from API is fully working and have changed the file to be a class for easy function calling.->api_calls
Connecting to database, creating tables, new data entries and searching data is working as intended -> db_script
Created a front end using Bootstrap, not fully functional but all inputs are present. ->index.html
Created a javascript to work with the front end of the web application. So far only is used for the "add" button but will be used more for managing the front end. ->formData.js
Created a Flask file to manage the backend. So far is being used to host, but will be used to interact with the database, as well as process data and send outputs to the formData file. ->app.py
**Fixed Issues**:
-Designed database to store API call data to decrease amount of API calls required.
**Current Issues**:
-Need to fix the date selector (was previously working)
-Need to get inputs to Flask file
**How to fix issues**:
-Debug and find what messed up date selector
-Work with <form> tag and POST and GET methods
**Challenges during this section**:
Had to learn how to use Bootstrap as well as set up a flask file to host 
Difficult time trying to interact backend with front end. I believe that working with the <form> tag and GET and POST methods is the fix I need. I was debating how to go about getting info from the front end to the back end and after research came up with 3 solutions: 1. Use js2py to translate javascript code to python and call functions from formData. 2. Use ajax to do the same thing, 3. Focus on mostly using flask to grab and process inputs and outputs.


