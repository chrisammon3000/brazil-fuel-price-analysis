#  Survey of fuel prices in Brazil: Geospatial Analysis
This project includes EDA and geospatial analyses in the form of choropleth maps to visualize the fuel price data in Brazil. The dataset was made available through [Kaggle](https://www.kaggle.com/matheusfreitag/gas-prices-in-brazil) and also includes [public geospatial data](ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2016/Brasil/BR/) available through public ftp from the Brazilian government.

#### -- Project Status: [Active]

## Project Objective
The purpose of this analysis is to answer 3 questions:
* How did the price change for the different regions of Brazil?
* Within a region, which states increased their prices the most?
* Which states are the cheapest (or most expensive) for different types of fuels?

## Description
The fuel price dataset comes from the National Agency of Petroleum, Natural Gas and Bio fuels (ANP in Portuguese), which releases weekly price reports of gas/petrol, diesel and other fuels used in transportation across the country. It includes the mean value per liter, number of gas stations analyzed and other information grouped by region and state. The analysis is enriched by joining the price data with geospatial data from the Brazilian government.

The project is divided into 3 parts each with it's own notebook: 
* *0.1-clean-data.ipynb* - Import and data cleaning
* *0.2-eda.ipynb* - EDA or exploratory data analysis 
* *0.3-geospatial-analysis.ipynb* - Geospatial analysis to investigate the 3 questions

## Technologies
* Python, Anaconda
* Pandas, Matplotlib, Seaborn, Geopandas, Jupyter Notebook

## Data Sources
Fuel Price data:
* https://www.kaggle.com/matheusfreitag/gas-prices-in-brazil

Shapefiles:
* ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2016/Brasil/BR/

## Getting Started
1. Clone repo
2. Run `conda env create -f environment.yml` to create the environment (requires Anaconda)
3. Run `conda activate brazil_fuel_price_env` to activate the environment
4. Run each notebook:
   - `0.1-import-clean-eda.ipynb`
   - `0.2-geospatial-analysis.ipynb`
5. Figures are saved to the `figures` directory

## Featured Notebooks
* Initial Data Exploration - [20190920-gcl-initial-exploration.ipynb](https://github.com/gclindsey/brazil-fuel-price/blob/master/notebooks/20190920-gcl-initial-exploration.ipynb)
* [Kaggle kernel](https://www.kaggle.com/gclindsey/geospatial-analysis-of-gas-prices-in-brazil)


## Contributors

**Primary (Contact) : [Gregory Lindsey](https://github.com/gclindsey)**
