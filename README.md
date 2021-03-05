# OxfordVisualisationHackathon
The repository contains datasets for use in the PCS seminar series' data visualisation hackathon, along with some example code.

## Getting started
Two different datasets are provided for the hackathon, both of which can be found in the `data` directory. The first contains some data on the carbon footprint of EGU and the second is a collection of meteorological observations collected at the University of Reading. Example scripts of how to load the data are stored in the `src` directory.

A description of each dataset and some questions you may wish to explore are detailed below. You are, of course, welcome to take your analysis in any direction you wish.

## The EGU dataset
The dataset `data/ProcessedEGU.csv` was compiled by Milan Kloewer as part of an investigation into the Carbon footprint of the European Geophysical Union's annual meeting in Vienna. I'd encourage you to come into the hackathon blind to his findings, however, if you later want to compare the conclusions you come to with Milan's you can find his analysis at https://github.com/milankl/CarbonFootprintEGU.

### The challenge
To get started we have provided a few initial questions below. It's up to you to then make an interesting (and hopegully beautiful!) plot over the next 45 minutes. 

1. Where are EGU attendees coming from?
2. Which nations/cities are responsible for the most emissions?
3. What would it take for EGU to become carbon neutral?
4. If EGU has a 'fixed' carbon budget, how many more 'overseas' visitors could be accomodated if Europe arrrived by rail?

### Dataset description
The dataset is a CSV with each row corresponding to data from some city. The columns are as follows:

1. City.
2. Country.
3. Number of attendees from this city.
4. Fraction - number of attendees from this city / total number of attendees from this country.
5. Longitude (x coordinate).
6. Latitude (y coordinate).
7. Distance to Vienna (location of EGU).
8. Total distance travelled by all the attendees from that city in a one way trip (i.e. item 3. $\times$ item 7.)
9. Total distance travelled in the return trip (i.e. item 8. $\times$ 2).
10. A realistic estimate CO_2 equivalent emssions, in tonnes, from attendees visiting Vienna.
11. An estimate of CO_2 equivalent emissions, in tonnes, if all attendees arrived via rail.
12. A realistic estimate of the total CO_2 emitted by attendees from that country (only one entry per country!)
13. An estimate of the total CO_2 emitted by attendees from that country if all attendees arrived via rail (only one entry per country!)

The file `src/LoadEGU.py` demonstrates how to load the dataset into python using pandas and xarray.

## The Reading dataset

## Plotting libraries
If using python your 'default' library is probably `matplotlib`. Other libraries such as `seaborn` and `bokeh` may also be of interest to you.

If you'd rather use something with more of a GUI, you should be able to open the CSV datasets in Excel. If you haven't come across it before, Tableau is another fun piece of software often used in data science. It's available for free to students, although you'll probably want to install it before the seminar!
