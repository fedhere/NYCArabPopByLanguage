# NYCArabPopByLanguage
Determining the population of Arab people by language spoken

The Arab population is classified as Caucasian in the Census and [American Community Survey](https://www.census.gov/programs-surveys/acs/) (ACS) datasets. This makes it hard to track the population and population changes geographically, which in turns makes it hard to distribute resources and plan outreach.

A proxy for ethnicity is language heritage. The Arab-American Faminly Support Center ([AAFSC](http://www.aafscny.org/)) serves a diverse Arab, Middles Eastern, and South Asian (AMESA) community which communicates in many languages including Arabic, Hindi, Bengali, Panjabi, Urdu, Pakistan, Tibetan, Nepali. 

The [American Community Survey](https://www.census.gov/programs-surveys/acs/) tracks language spoken in American households ("These statistics help the federal
government understand how well people in each community speak English, and analyze and plan programs
for adults and children who do not speak English well.") The data is available at census-tract spatial granularity, however, due to identification risks the language granularity is limited: the following four language classes are considered relevant for [AAFSC](http://www.aafscny.org/): Arab, Urdu, Hindi, and "Other Indi Languages" (although attention should be payed when using this broad class). 
A recent [language map of NYC](http://www.jillhubley.com/project/nyclanguages/) by Jill Hubley inspired this work: we will assume hereafter that population in households where Arab, Urdi, and Hindi is spoken belong to the AMESA population that [AAFSC](http://www.aafscny.org/) serves and identify their distribution in NYC. The code in this repo parses ACS data to identify the density, counts and fraction of Arab population by language spoken, and dose some modest geospatial fymnastics for this purpose.

Below is a density map of AMESA in NYC (people per sq mile) for 2015 (left) and 2010 (right) ACS data (covering respectively the 2010-2014 and the 2005-2009 period):

<img src="ArabDensity2015Smooth.png" width="425"/>  <img src="ArabDensity2010Smooth.png" width="425"/> 

A few more maps:

The total number (top)  and fraction (bottom) of Arab speakers is mapped at the census tract level from the 2015 (left) and 2010 (right) ACS data .



<img src="ArabCountByLanguage15.png" width="425"/> <img src="ArabCountByLanguage10.png" width="425"/> 
<img src="ArabByLanguage15.png" width="425"/> <img src="ArabByLanguage10.png" width="425"/> 


The map below shows the change in fraction of population speaking arab languages: 
<img src="ArabCountByLanguage15.png" width="425"/>

The map below shows the numbers of Arab speakers in the census tracts and the location of the [AAFSC](http://www.aafscny.org/) offices.

The following gifs show the evolution from 2005 though 2014 (with really only 2 time stamps, smoothed for impact) on numbers (left) fraction (right) and below for number separated by the four relevant language classes 
