Title: Test Pelican content
Date: 2019-08-25 23:17
Category: main
tags: welcome, python, pelican

##This is my first Pelican documen

This is my first attempt at making some content for my github.io page. This page is written using Markdown .md files. I plan to use Python to generate most of my content, so it will be an interesting exercise figuring out how to write content in a Jupyter notebook, then integrating that content in the Pelican static site generator. I also am looking to develop some content in R/R Studio, using R markdown, so hopefully that will be feasible to integrate. I especially want to see if it's feasible to insert dynamic charts created using plotly. 

Right now, I have two separate projects that create this content. 
1. The actual github.io page which only contains content, readme, and gitignore. 
2. A project where I have Pelican installed which actually creates content. Luckily keeping the two pages in sync seems fairly easy, once I run the `pelican content` command, I run rsync using wsl, `wsl rsync -a ./pelican_gitio/output/ ./accraft.github.io`. 

