Title: DC Daily Weather
Date: 2019-08-25 23:17
Category: weather
tags: weather,local,dc



The other day I wanted to check out average daily temperatures weather in the DC area, and there was a surprising lack of good visualizations at the day-level. I poked around and found NOAA publishes daily climate data from a large number of monitoring stations from around the country. The website was a bit of a pain, and I didn’t feel like navigating their API, so I just put in an order for daily weather from a tracking station at the National Arboretum. I threw the results in plotly, and decided this would be a good chance to see if I can embed an html object created in plotly to my slowly developing blog. 

Below (hopefully) is a graph showing median and average high and median low temperatures by day from 1948-2017 from the [GHCND:USC00186350!](https://www.ncdc.noaa.gov/cdo-web/datasets/NORMAL_ANN/stations/GHCND:USC00186350/detail)

now giving it a shot with an .md file. 

<iframe src="https://accraft.github.io/embedded/Median Temp By Day.html" style="width: 100%; height: 500px"></iframe>
