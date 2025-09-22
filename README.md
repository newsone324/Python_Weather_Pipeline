# Weather Data Pipeline (Python and SQLite)

### Overview:
This project **extracts** data from the free OpenWeather API, **transforms** it using pandas, and **loads** it into a data base for any further analysis.
It demonstrates skills needed for data engineering -- Databases, building ETL Pipelines, and integrating API's


### Features
- Extracts live data from some of the top cities in the US (Boston, New York, San Fransisco, Los Angeles, Seattle, Chicago, Miami, Las Vegas, Denver, Minneapolis).
- Transforms data -> added Farenheit and Celsius, time stamps, and rounded decimals for easier viewing).
- Loads the data into a regional SQL database.
- Basic queries for analysis (Top windiest cities, hottest cities)

### Sample Output!
<img width="1139" height="757" alt="image" src="https://github.com/user-attachments/assets/ff26bba8-55b9-42b4-b790-0d91907373b1" />


### Future Improvements
- Add a simple UI or dashboard using Streamlit.
- Automate the pipeline
- Try storing data in PostgreSQL 