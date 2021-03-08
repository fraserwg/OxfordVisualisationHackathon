# OxfordVisualisationHackathon
The repository contains datasets for use in the PCS seminar series' data visualisation hackathon, along with some example code.

## Getting started
Two different datasets are provided for the hackathon, both of which can be found in the `data` directory. The first contains some data on the carbon footprint of AGU and the second is a collection of meteorological observations collected at the University of Reading. Example scripts of how to load the data are stored in the `src` directory.

A description of each dataset and some questions you may wish to explore are detailed below. You are, of course, welcome to take your analysis in any direction you wish.

## The AGU dataset
The dataset `data/ProcessedAGU.csv` was compiled by Milan Kloewer as part of an investigation into the Carbon footprint of the American Geophysical Union's annual meeting in San Francisco. I'd encourage you to come into the hackathon blind to his findings, however, if you later want to compare the conclusions you come to with Milan's you can find his analysis at https://github.com/milankl/CarbonFootprintAGU.

### The challenge
To get started we have provided a few initial questions below. It's up to you to then make an interesting (and hopefully beautiful!) plot over the next 40 minutes. 

1. Where are AGU attendees coming from?
2. Which nations/cities are responsible for the most emissions?
3. What would it take for AGU to become carbon neutral?

### Dataset description
The dataset is a CSV with each row corresponding to data from some city. The columns are as follows:

1. Number of attendees from this city
2. Country
3. State (for Australia, Brazil, Canada and USA)
4. City
5. Latitude
6. Longitude
7. Distance to San Fransisco

The file `src/LoadAGU.py` demonstrates how to load the dataset into python using `pandas` and the inbuilt `csv` module.

## The Reading dataset
The dataset data/reading_data.csv contains historical weather data, downloaded from the Reading University meteorological weather station (found here: https://metdata.reading.ac.uk/cgi-bin/climate_extract.cgi). 

### The challenge
As above, we have provided a few questions below to get you started, but please feel free to investigate anything from the data that may interest you or others, and will generate a good plot in the next 40 minutes.

1. Did the weather over the first British lockdown (March 2020 - June 2020) differ from the climatalogical mean?
2. How does soil temperature correlate with atmospheric warming? Are different depths affected differently?
3. How is climate change affecting cloud cover?

### Dataset description
The Reading dataset is a CSV file. The top row gives the column description, then each subsequent row represents a day, starting from 01 Jan 1970 until 01 March 2021. The columns are as follows:

1. Year
2. Month
3. Day
4. Day of the week
5. Barometer temperature (degC)
6. Weather station pressure (mb)
7. Mean sea level pressure (mb)
8. Dry bulb temperature (degC at 9am)
9. Wet bulb temperature (degC at 9am)
10. Dew point temperature (degC at 9am)
11. Relative humidity (% at 9am)
12. Maximum temperature (degC)
13. Minimun temperature (degC)
14. Soil minimum temperature (degC)
15. Daily mean temperature (degC)
16. 5cm soil temperature (degC)
17. 10cm soil temperature (degC)
18. 20cm soil temperature (degC)
19. 30cm soil temperature (degC)
20. 50cm soil temperature (degC)
21. 100cm soil temperature (degC)
22. Cloud cover (oktas)
23. Wind direction (deg/10)
24. Wind speed (m/s)
25. Max 3 sec gust (m/s)
26. Rainfall (mm, over 24 hours from 9am)
27. Total snow depth (cm)
28. Fresh snow depth (cm)
29. State of ground (code here: http://www.met.reading.ac.uk/~sws09a/var_codes.html#sog%20code)
30. State of ground (code here: http://www.met.reading.ac.uk/~sws09a/var_codes.html#sogs%20code)
31. Sunshine duration (hours)

Missing data is represented with an 'x'. There are more data variables available here if you would like to investigate something different: https://metdata.reading.ac.uk/cgi-bin/climate_extract.cgi. Simply choose your dates and variables desired. 

The file `src/LoadReading.py` demonstrates how to load the dataset into python using `pandas` and the inbuilt `csv` module.

## Plotting libraries
If using python your 'default' library is probably `matplotlib`. Other libraries such as `seaborn` and `bokeh` may also be of interest to you. The `cartopy` library could also be useful if you're plotting maps etc.

If you'd rather use something with more of a GUI, you should be able to open the CSV datasets in Excel. If you haven't come across it before, Tableau is another fun piece of software often used in data science. It's available for free to students, although you'll probably want to install it before the seminar!

## Acknowledgements
Many thanks to Milan Kloewer for allowing us to use the AGU dataset from his https://github.com/milankl/CarbonFootprintAGU repository.
