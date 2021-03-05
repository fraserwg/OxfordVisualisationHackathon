# OxfordVisualisationHackathon
The repository contains datasets for use in the PCS seminar series' data visualisation hackathon, along with some example code.

## Getting started
Two different datasets are provided for the hackathon, both of which can be found in the `data` directory. The first contains some data on the carbon footprint of AGU and the second is a collection of meteorological observations collected at the University of Reading. Example scripts of how to load the data are stored in the `src` directory.

A description of each dataset and some questions you may wish to explore are detailed below. You are, of course, welcome to take your analysis in any direction you wish.

## The AGU dataset
The dataset `data/ProcessedAGU.csv` was compiled by Milan Kloewer as part of an investigation into the Carbon footprint of the American Geophysical Union's annual meeting in San Francisco. I'd encourage you to come into the hackathon blind to his findings, however, if you later want to compare the conclusions you come to with Milan's you can find his analysis at https://github.com/milankl/CarbonFootprintAGU.

### The challenge
To get started we have provided a few initial questions below. It's up to you to then make an interesting (and hopegully beautiful!) plot over the next 45 minutes. 

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

The file `src/LoadAGU.py` demonstrates how to load the dataset into python using pandas and xarray.

## The Reading dataset

## Plotting libraries
If using python your 'default' library is probably `matplotlib`. Other libraries such as `seaborn` and `bokeh` may also be of interest to you.

If you'd rather use something with more of a GUI, you should be able to open the CSV datasets in Excel. If you haven't come across it before, Tableau is another fun piece of software often used in data science. It's available for free to students, although you'll probably want to install it before the seminar!
