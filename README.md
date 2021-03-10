# OxfordVisualisationHackathon
The repository contains datasets for use in the PCS seminar series' data visualisation hackathon, along with some example code.

## Getting started
Two different datasets are provided for the hackathon, both of which can be found in the `data` directory. The first contains some data on the carbon footprint of AGU and the second is a collection of meteorological observations collected at the University of Reading. Example scripts of how to load the data are stored in the `src` directory.

A description of each dataset and some questions you may wish to explore are detailed below. You are, of course, welcome to take your analysis in any direction you wish.

## The AGU dataset
The dataset `data/ProcessedAGU.csv` was compiled by Milan Kloewer as part of an investigation into the Carbon footprint of the American Geophysical Union's annual meeting in San Francisco. I'd encourage you to come into the hackathon blind to his findings, however, if you later want to compare the conclusions you come to with Milan's you can find his analysis at https://github.com/milankl/CarbonFootprintAGU.

### The challenge
To get started we have provided a few initial questions below. It's up to you to then make an interesting (and hopefully beautiful!) plot over the next 40 minutes. You are also, of course, welcome to explore other ideas.

1. Where are AGU attendees coming from?
2. Which nations/cities are responsible for the most emissions?
3. What would it take for AGU to become carbon neutral?

### Dataset description
The dataset is a CSV with each row corresponding to data from some city. The columns are as follows:

0. Number of attendees from this city
1. Country
2. State (for Australia, Brazil, Canada and USA)
3. City
4. Latitude
5. Longitude
6. Distance to San Fransisco

The file `src/LoadAGU.py` demonstrates how to load the dataset into python using `pandas` and the inbuilt `csv` module. If you want to investigate the emissions from AGU attendees, then please find Milan's script for his method here: https://github.com/milankl/CarbonFootprintAGU/blob/master/scripts/calculate_emissions.py

## The Reading dataset
The dataset data/reading_data.csv contains historical weather data, downloaded from the Reading University meteorological weather station (found here: https://metdata.reading.ac.uk/cgi-bin/climate_extract.cgi). 

### The challenge
As above, we have provided a few questions below to get you started, but please feel free to investigate anything from the data that may interest you or others, and will generate a good plot in the next 40 minutes.

1. Did the weather over the first British lockdown (March 2020 - June 2020) differ from the climatalogical mean?
2. How does soil temperature correlate with atmospheric warming? Are different depths affected differently?
3. How is climate change affecting cloud cover?

### Dataset description
The Reading dataset is a CSV file. The top row gives the column description, then each subsequent row represents a day, starting from 01 Jan 1970 until 01 March 2021. The columns are as follows:

0. Year
1. Month
2. Day
3. Day of the week
4. Barometer temperature (degC)
5. Weather station pressure (mb)
6. Mean sea level pressure (mb)
7. Dry bulb temperature (degC at 9am)
8. Wet bulb temperature (degC at 9am)
9. Dew point temperature (degC at 9am)
10. Relative humidity (% at 9am)
11. Maximum temperature (degC)
12. Minimun temperature (degC)
13. Soil minimum temperature (degC)
14. Daily mean temperature (degC)
15. 5cm soil temperature (degC)
16. 10cm soil temperature (degC)
17. 20cm soil temperature (degC)
18. 30cm soil temperature (degC)
19. 50cm soil temperature (degC)
20. 100cm soil temperature (degC)
21. Cloud cover (oktas)
22. Wind direction (deg/10)
23. Wind speed (m/s)
24. Max 3 sec gust (m/s)
25. Rainfall (mm, over 24 hours from 9am)
26. Total snow depth (cm)
27. Fresh snow depth (cm)
28. State of ground (code here: http://www.met.reading.ac.uk/~sws09a/var_codes.html#sog%20code)
29. State of ground (code here: http://www.met.reading.ac.uk/~sws09a/var_codes.html#sogs%20code)
30. Sunshine duration (hours)

Missing data is represented with an 'x'. There are more data variables available here if you would like to investigate something different: https://metdata.reading.ac.uk/cgi-bin/climate_extract.cgi. Simply choose your dates and variables desired. 

The file `src/LoadReading.py` demonstrates how to load the dataset into python using `pandas` and the inbuilt `csv` module.

## Plotting libraries
If using python your 'default' library is probably `matplotlib`. Other libraries such as `seaborn` and `bokeh` may also be of interest to you. The `cartopy` library could also be useful if you're plotting maps etc.

If you'd rather use something with more of a GUI, you should be able to open the CSV datasets in Excel. If you haven't come across it before, Tableau is another fun piece of software often used in data science. It's available for free to students, although you'll probably want to install it before the seminar!

## Acknowledgements
Many thanks to Milan Kloewer for allowing us to use the AGU dataset from his https://github.com/milankl/CarbonFootprintAGU repository. The Reading dataset was compiled and published by the University of Reading's meteorological observatory. It is presented here for educational purposes.
