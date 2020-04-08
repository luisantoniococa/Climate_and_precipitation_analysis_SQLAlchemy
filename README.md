# Climate and Precipitation analysis with SQLAlchemy
### Overview 
This project has 2 parts. First an analysis with Python and SQLAlchemy for data exploration for a climate database. Second, an app that serves an api endpoint with data summaries. Additionaly it creates a search based in a selected date that returns a summary of temperatures for those dates by day.
All of the following analysis also includes, SQLite, SQLAlchemy ORM queries, Pandas, and Matplotlib.

### Climate/Precipitation Analysis and Exploration

The first part of the project uses SQLAlchemy to create a connection (create_engine) to an sqlite database and perfrom queries to answer business questions.  

#### This is the example of a query that answers a specific question in the notebook

+ What are the most active stations? (i.e. what stations have the most rows)? It showcase the stations in descending order
![Station Example](https://github.com/luisantoniococa/Climate_and_precipitation_analysis_SQLAlchemy/blob/master/Descending%20order%20by%20station.png)

+ A query to get a summary of the temperature MIN, MAX, AVG and the station by date. 

![Summary Examples](https://github.com/luisantoniococa/Climate_and_precipitation_analysis_SQLAlchemy/blob/master/Temperature%20avg%20max%20and%20min.png)

#### The analysis also takes some of the created queries and plots the results

+ The plot shows the measured precipitation in the y axis and the dates in the x axis per day.

![Precipitation per Date](https://github.com/luisantoniococa/Climate_and_precipitation_analysis_SQLAlchemy/blob/master/Precipitations.png)

+ The plot below shows an histogram with 12 bins for the temperatures frequency. It can be observed that the data is skewed rigth.

![Temperatures recorded Histogram](https://github.com/luisantoniococa/Climate_and_precipitation_analysis_SQLAlchemy/blob/master/Temperature_frequency.png)

- - -

## Climate App / API server

The climate Flask app serves API routes from the original sqlite database used. In a similar way connecting with SQLAlchemy in python uses SQL/ORM queries to serve the APIs based in the menu created. 

The following is an example of the connection to the app.py in port 5000 from a local machine. It shows a menu with the possible API calls. For calling sumarize temperature data by date we use the format YYYY-MM-DD


### Routes

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * query for the dates and temperature observations from a year from the last data point.
  * Return a JSON list of Temperature Observations (tobs) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

## Hints

* You will need to join the station and measurement tables for some of the analysis queries.

* Use Flask `jsonify` to convert your API data into a valid JSON response object.

- - -

### Optional: Other Recommended Analyses

* The following are optional challenge queries. These are highly recommended to attempt, but not required for the homework.

### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

* You may either use SQLAlchemy or pandas's `read_csv()` to perform this portion.

* Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.

* Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?

### Temperature Analysis II

* The starter notebook contains a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d` and return the minimum, average, and maximum temperatures for that range of dates.

* Use the `calc_temps` function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").

* Plot the min, avg, and max temperature from your previous query as a bar chart.

  * Use the average temperature as the bar height.

  * Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr).

    ![temperature](Images/temperature.png)

### Daily Rainfall Average

* Calculate the rainfall per weather station using the previous year's matching dates.

* Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.

* You are provided with a function called `daily_normals` that will calculate the daily normals for a specific date. This date string will be in the format `%m-%d`. Be sure to use all historic tobs that match that date string.

* Create a list of dates for your trip in the format `%m-%d`. Use the `daily_normals` function to calculate the normals for each date string and append the results to a list.

* Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.

* Use Pandas to plot an area plot (`stacked=False`) for the daily normals.

  ![daily-normals](Images/daily-normals.png)
