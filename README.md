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

The climate Flask app serves API JSON routes from the original sqlite database used. In a similar way connecting with SQLAlchemy in python uses SQL/ORM queries to serve the APIs based in the menu created. 

The following are example of the connection to the app.py in port 5000 from a local machine. It shows a menu with the possible API calls. For calling sumarize temperature data by date we use the format YYYY-MM-DD


### Routes

The following routes were created for the API response.
* `/`

  * Home page.

  * Lists all routes that are available.
  
  ![API Menu](https://github.com/luisantoniococa/Climate_and_precipitation_analysis_SQLAlchemy/blob/master/port5000%20welcome.png)

---
* `/api/v1.0/precipitation`

  * Converts the query results to a JSON representation of a Dictionary using `date` as the key and `prcp` as the value.
  
![API Recent](https://github.com/luisantoniococa/Climate_and_precipitation_analysis_SQLAlchemy/blob/master/recent%20Precipitations.png)
The figure above is an example of the an API call for the recent Precipitations, that includes precipitations a  year from the last data point.

---
* `/api/v1.0/stations`

  * Returns a JSON list of stations from the dataset.

* `/api/v1.0/tobs`

  * Queries for the dates and temperature observations from a year from the last data point.
  * Returns a JSON list of Temperature Observations (tobs) for the previous year.
  
--- 
* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculates `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculates the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
  * It uses the format YYYY-MM-DD for both dates search

![API Search by Date Start](https://github.com/luisantoniococa/Climate_and_precipitation_analysis_SQLAlchemy/blob/master/Precipitations%20by%20startdate.png)
As explained above this uses the the start date for the api call and shows all the data points from that selected date.

![API Search by Date](https://github.com/luisantoniococa/Climate_and_precipitation_analysis_SQLAlchemy/blob/master/Precipitations%20between%20dates.png)
We can see in orange the dates used in the api call for the start and in Purple for the end date, in this case we are obtaining 2 days total
- - -
