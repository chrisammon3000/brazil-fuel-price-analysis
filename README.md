# Geospatial Analysis of Fuel Prices in Brazil
This project investigates 3 questions pertaining to fuel prices in Brazil. It includes EDA and geospatial analyses in the form of choropleth maps to visualize the price data by region and state. The dataset was made available through [Kaggle](https://www.kaggle.com/matheusfreitag/gas-prices-in-brazil) and also includes [public geospatial data](ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2016/Brasil/BR/) available through public ftp from the Brazilian government.

#### -- Project Status: [Active]

## Project Intro/Objective
The purpose of this project is to answer 3 questions:
* How did the price change for the different regions of Brazil?
* Within a region, which states increased their prices the most?
* Which states are the cheapest (or most expensive) for different types of fuels?

### Methods Used
* EDA
* Univariate and Multivariate Analysis
* Time Series
* Data Visualization
* Geospatial Visualization & Choropleth maps

### Technologies
* Python
* Pandas, Seaborn, Geopandas, jupyter

## Project Description
The project is divided into 3 parts: 1) import and data cleaning, 2) EDA, and 3) an attempt to investigate the 3 questions. The fuel price dataset comes from the National Agency of Petroleum, Natural Gas and Bio fuels (ANP in Portuguese), which releases weekly price reports of gas/petrol, diesel and other fuels used in transportation across the country. It includes the mean value per liter, number of gas stations analyzed and other information grouped by region and state. The analysis is enriched by joining the price data with geospatial data from the Brazilian government.

## Needs of this project

- Convert code into functions for data processing, cleaning and exploration
- Create src modules
- Include quantitative analysis to augment visualizations
- AWS cloud integration for faster rendering

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data can be accessed here: [Kaggle: Gas Prices in Brazil](https://www.kaggle.com/matheusfreitag/gas-prices-in-brazil/downloads/gas-prices-in-brazil.zip/3) and here:
[Instituto Brasiliero de Geografia e Estatistica, or IBGE] [website](https://www.ibge.gov.br/geociencias/downloads-geociencias.html) (for direct download through ftp copy and paste: ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2018/Brasil/BR/br_unidades_da_federacao.zip)
3. Notebooks are in the [notebooks](https://github.com/gclindsey/brazil-fuel-price/tree/master/notebooks) folder.

## Featured Notebooks
* [Initial Data Exploration](https://github.com/gclindsey/brazil-fuel-price/blob/master/notebooks/20190920-gcl-initial-exploration.ipynb)
* [Kaggle version](https://www.kaggle.com/gclindsey/geospatial-analysis-of-gas-prices-in-brazil)


## Contributors

**Primary Contact : [Gregory Lindsey](https://github.com/gclindsey)**

========================================================
