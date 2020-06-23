#  Survey of fuel prices in Brazil: Geospatial Analysis
This project includes EDA and geospatial analyses in the form of choropleth maps to visualize the fuel price data in Brazil. The dataset was made available through [Kaggle](https://www.kaggle.com/matheusfreitag/gas-prices-in-brazil) and also includes [public geospatial data](ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2016/Brasil/BR/) available through public ftp from the Brazilian government.

#### -- Project Status: [Active]

## Project Objective
The purpose of this analysis is to answer 3 questions:
* How did the price change for the different regions of Brazil?
* Within a region, which states increased their prices the most?
* Which states are the cheapest (or most expensive) for different types of fuels?

### Methods Used
* EDA - Univariate and Multivariate Analysis
* Time Series
* Data Visualization
* Geospatial Visualization & Choropleth maps

### Technologies
* Python, Bash
* Pandas, Matplotlib, Seaborn, Geopandas, Jupyter Notebook

## Description
The fuel price dataset comes from the National Agency of Petroleum, Natural Gas and Bio fuels (ANP in Portuguese), which releases weekly price reports of gas/petrol, diesel and other fuels used in transportation across the country. It includes the mean value per liter, number of gas stations analyzed and other information grouped by region and state. The analysis is enriched by joining the price data with geospatial data from the Brazilian government.

The project is divided into 3 parts each with it's own notebook: 
* *0.1-clean-data.ipynb* - Import and data cleaning
* *0.2-eda.ipynb* - EDA or exploratory data analysis 
* *0.3-geospatial-analysis.ipynb* - Geospatial analysis to investigate the 3 questions

## Data Sources
Fuel Price data:
* https://www.kaggle.com/matheusfreitag/gas-prices-in-brazil

Shapefiles:
* ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2016/Brasil/BR/

## Getting Started
1. Clone this repo
2. 
3. Run each notebook:
   - `0.1-import-clean-eda.ipynb`
   - `0.2-geospatial-analysis.ipynb`
4. Figures are saved to the `figures` directory

## Featured Notebooks
* Initial Data Exploration - [20190920-gcl-initial-exploration.ipynb](https://github.com/gclindsey/brazil-fuel-price/blob/master/notebooks/20190920-gcl-initial-exploration.ipynb)
* [Kaggle kernel](https://www.kaggle.com/gclindsey/geospatial-analysis-of-gas-prices-in-brazil)


## Contributors

**Primary (Contact) : [Gregory Lindsey](https://github.com/gclindsey)**
