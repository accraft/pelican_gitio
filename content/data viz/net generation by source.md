Title: Net Generation By Source
Date: 2020-02-08 23:17
Category: Data Viz
tags: data viz,weather,plotly

Emmissions from the electricity generation sector make up about 28% of total greenhouse emmisions in the United States in 2017 per the (EPA) [https://www.epa.gov/ghgemissions/sources-greenhouse-gas-emissions]. Transitioning the grid to renewable sources seems to get a lot of press with politicians and executives touting the benefits of solar and wind. To get an actual sense of what the current and past state of the electrical generation sector, I pulled in data from the Energy Information Administraton (EIA) and graphed total net generation by source. The EIA has a *very* impressive "open data" initiave that offers access to over 408,0000 electiricy generation series via a public facing RESTful API. More information can be found on the [IA's website here] (https://www.eia.gov/opendata/). 

I used the Net Generation By Source data, and built a python script that will a) offer the user a list of all available state and regional groupings and b) pull all past data into an interactive plotly html widget. Below is the total US net generation by source dataset. The big takeaway is not the rise of renewables, but rather the fall of coal and the rise of natural gas sources. Note that it's much easier to see the trends when the graph is set to display TTM data (use the dropdown on the left)

<iframe src="https://accraft.github.io/embedded/Net Gen by Source - United States.html" style="width: 100%; height: 1000px"></iframe>

Below is a link to just the html graphic for the US, as well as links to some of the largest states. 

###[United States](https://accraft.github.io/embedded/Net Gen by Source - United States.html)  

###[Mid-Atlantic](https://accraft.github.io/embedded/Net Gen by Source - Middle Atlantic (total).html)  

###[Texas](https://accraft.github.io/embedded/Net Gen by Source - Texas.html)  

###[California](https://accraft.github.io/embedded/Net Gen by Source - California.html)  


