# Airbnb Seattle Data Exploration

## Table of contents
* [Libraries](#libraries)
* [Project Motivation](#project_motivation)
* [File Descriptions](#file_descriptions)
* [Licensing, Authors, Acknowledgements](#licensing_authors_acknowledgements)

## Libraries

In this project Python 3 and Jupyter Notebook were used. The libraries that are
necessary to run the notebook are the standard packages as follows:

- pandas
- numpy
- matplotlib
- Seaborn
- re

User defined utility functions we built were stored in myutils.py file, which is
necessary to run the notebook.

## Project Motivation

For this project we were interested in exploring AirBnb Seattle dataset to better
understand the following questions:

- Which features are highly correlated with price?
- Do reviews have any effect on the price? Which factors affect the overall rating?
Is it profitable to have the high rating?
- What are the most common property and room types that are listed?
How are the prices distributed amongst them?


## File Descriptions

The repository contains the following files:

- README.md
- seattle_listings.csv.gz
- analysis_notebook.ipynb
- myutils.py

The main code of the project sits in _analysis_notebook.ipynb_. The notebook walks
through the CRISP-DM process for
analysing the dataset.

The main findings of the code can be found at the post available [here]()

## Licensing, Authors, Acknowledgements

This project uses the Airbnb Seattle open data available in
[here](http://insideairbnb.com/get-the-data.html). We used
the data that was scraped on the 25th October 2020.
