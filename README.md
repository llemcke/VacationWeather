# VacationWeather
Flask webapp that allows user to check multiple locations for historical weather data for planning a vacation. Uses Flask, Python, HTML, CSS, Bootstrap, MySQL, JavaScript, and various python libraries.
[Try out the finished project](https://vacationweather.llemcke.repl.co/)

**Important notes:**
Using a database to store information as a weather object has proven to be very efficient in saving API call costs, as well as time.

**For 1 Location:**
- New Entry into existing table (New API call): 3.4 seconds
- New Table and Entry(New API Call): 3.5 seconds
- Search and pull data from database (No API call): 0.3 seconds
- 
**For 2 Locations:**
  - New Table and Entry(New API Call): 6.8 seconds
  - Search and pull data from database (No API call): 0.6 seconds.
  Approx. 1/10th of the time.

**Further ideas for future:**
As the database grows with every user entry, the time for calculation will be reduced in comparison to API calls, however could increase slightly due to amount of entries and tables in the database. A future improvement I will look to make is to design the database to make searching more efficient. This could be something such as a table the stores the top 10 or 15 locations searched, and search there before searching the main locations table. I could also add a counter to each location table and have it clear entries that are below a certain threshold after a certain number of entries have been made. 

**June 13th:**
First step to pull data from API is done. 
Calculating averages of weather data for past 5 years is done.
Issues so far: 
- Calls for checks are expensive. One week check for one location is 8 calls* 5 years... 40 calls per location.
Ideas to mitigate issues:
- Create test API to store some data for testing 
- Stop making calls and hardcode in data for now since the API calls have proven to work so far.

**July 25th:**
Pulling data from API is fully working and have changed the file to be a class for easy function calling.->api_calls
Connecting to database, creating tables, new data entries and searching data is working as intended -> db_script
Created a front end using Bootstrap, not fully functional but all inputs are present. ->index.html
Created a javascript to work with the front end of the web application. So far only is used for the "add" button but will be used more for managing the front end. ->formData.js
Created a Flask file to manage the backend. So far is being used to host, but will be used to interact with the database, as well as process data and send outputs to the formData file. ->app.py

**Fixed Issues**:
- Designed database to store API call data to decrease amount of API calls required.

**Current Issues**:
- Need to fix the date selector (was previously working)
- Need to get inputs to Flask file

**How to fix issues**:
- Debug and find what messed up date selector
- Work with form tag and POST and GET methods

**Challenges during this section**:
- Had to learn how to use Bootstrap as well as set up a flask file to host 
- Difficult time trying to interact backend with front end. I believe that working with the form tag and GET and POST methods is the fix I need. I was debating how to go about getting info from the front end to the back end and after research came up with 3 solutions: 1. Use js2py to translate javascript code to python and call functions from formData. 2. Use ajax to do the same thing, 3. Focus on mostly using flask to grab and process inputs and outputs.

**August 10th:**
Created a new html doc to handle the results page after user selects inputs. Designed a ranking system to rank locations based off of user preferences. The biggest element is temperature, since that is what most people look for when planning a vacation. If user selects avoid precipitation, the rankings are heavily affected the more precipitation that location historically has during the selected week.

I have noticed when testing that when data is pulled from the database, it is a lot quicker than when data is pulled from the API. At the end of the project I will compare time difference.

**Changes**
- Decided to change the form inputs and scrap the rain and snow radio buttons and wind checkbox. Now it is just a single checkbox that says "avoid precipitation" This should simplify user choice and they can view the rain and snowfall in the results anyways. 
- Weather Object now has "rankings" attribute, to store the rank value in the object. 
- Weather Object also now has rain and snow as floats to make it more accurate
- no longer need javascript file since flask handles the entire backend now

**Fixed issues**
- Date selector has been fixed
- Flask file now takes all inputs. Used the calculate button as a "submit" button and added post method and action to form tag

**Current issues**
- There are no current issues I have that are unintended

**Next steps**
- Implement a geographic location API to help validate data and keep database queries consistent.
- data validation for entire form
- Make result cards more appealing and accurate using icons

**Challenges during this sections**
- Trying to rank all the locations, and then sort the array to pass to front end. I decided to add a ranking attribute to the Weather object to store its ranking for the current use. Another idea was to just rank locations based off of the temperature and target temperature selected by the user, but I wanted to implement a ranking system with precipitation as well.
- It took me a while to figure out using flask as a backend, but once I understood passing variables, it became much easier.


**August 24th**
The last section of this project I added the finishing touches and used Repl.it to upload the project, and I'm using a ping bot to keep the web app up and running. As this is a project, this is the easiest free method to display this project as a web application. 

**Changes**
- Implemented Geoapify for autocompletion of locations
- Added Data validation
- Uploaded to repl.it and used a ping bot to keep it online
- Changed the form, no longer using snow, rain, neither, and wind radio button and check boxes. Instead one checkbox "avoid precipitation" is being used when ranking the locations.

**Fixes**
- Some locations were not working with the database because of special characters and although I replaced all commas and blank spaces with underscores, I missed dashes. Now using a python library to convert special characters into regualr ones, this bug does not occur.
- Any unintended inputs will make the user re-input to avoid errors.
