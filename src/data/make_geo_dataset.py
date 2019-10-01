# Import data science libraries
import numpy as np
import pandas as pd
import os

# Import geospaitial libraries
import geopandas as gpd
from shapely.geometry import Point

def load_geo_data():

    # URL to shape files of Brazil's states, made public courtesy of the Brazilian government
    #url = "ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2016/Brasil/BR/br_unidades_da_federacao.zip"

    url= './data/external/br_unidades_da_federacao/'

    print("Reading geospatial data...")
    brazil_geo = gpd.read_file(url)

    # Correct state names to match current dataset
    state_dict = {"RONDÔNIA":"RONDONIA", "PARÁ":"PARA", "AMAPÁ":"AMAPA", "MARANHÃO":"MARANHAO",
                 "PIAUÍ":"PIAUI", "CEARÁ":"CEARA", "PARAÍBA":"PARAIBA", "ESPÍRITO SANTO":"ESPIRITO SANTO",
                 "SÃO PAULO":"SAO PAULO", "PARANÁ":"PARANA", "GOIÁS":"GOIAS", "ACRE":"ACRE",
                 "AMAZONAS":"AMAZONAS", "RORAIMA":"RORAIMA", "TOCANTINS":"TOCANTINS",
                 "RIO GRANDE DO NORTE":"RIO GRANDE DO NORTE", "PERNAMBUCO":"PERNAMBUCO",
                 "ALAGOAS":"ALAGOAS", "SERGIPE":"SERGIPE", "BAHIA":"BAHIA", "MINAS GERAIS":"MINAS GERAIS",
                 "RIO DE JANEIRO":"RIO DE JANEIRO", "SANTA CATARINA":"SANTA CATARINA", "MATO GROSSO DO SUL":"MATO GROSSO DO SUL",
                 "MATO GROSSO":"MATO GROSSO", "DISTRITO FEDERAL":"DISTRITO FEDERAL", "RIO GRANDE DO SUL":"RIO GRANDE DO SUL"}

    brazil_geo["NM_ESTADO"] = brazil_geo.NM_ESTADO.map(state_dict)

    brazil_geo.crs = {"init": "epsg:4326"}

    brazil_geo.columns = ['State', 'Macroregion', 'CD_GEOCUF', 'geometry']

    brazil_geo["Macroregion"] = brazil_geo.Macroregion.str.replace("-", " ")

    # Extract regions geography
    brazil_geo_region = brazil_geo.dissolve(by='Macroregion').reset_index()
    brazil_geo_region = brazil_geo_region[['Macroregion', 'geometry']]

    print("Calculating price percentage change...")

    # Create dataframe df_pct_change with percent change of prices
    df = pd.read_csv("./data/interim/brazilfuel.csv")
    macroregions = df.Macroregion.unique().tolist()

    df_pct_change = pd.DataFrame()

    count = 0

    for i in range(len(macroregions)):
        region = macroregions[i]
        states = df[df.Macroregion==region]["State"].unique()

        for i in range(len(states)):
            state = states[i]
            products = df[(df.Macroregion==region) & (df.State==state)]["Product"].unique()

            for i in range(len(products)):
                product = products[i]
                years = df[(df.Macroregion==region) & (df.State==state) &
                           (df.Product==product)]["Year"].unique()

                mean_price = df[(df.Macroregion==region) & (df.State==state) &
                                (df.Product==product)]["Mean_Price"].mean()

                # Percent change for raw data
                first_price = df[(df.Macroregion==region) & (df.State==state) &
                                (df.Product==product) & (df.Year==years[0])]["Mean_Price"].iloc[0]
                last_price = df[(df.Macroregion==region) & (df.State==state) &
                                (df.Product==product) & (df.Year==years[-1])]["Mean_Price"].iloc[-1]
                price_pct_change = (last_price - first_price) / np.abs(first_price)


                # Percent change for Normalized data
                first_price_norm = df[(df.Macroregion==region) & (df.State==state) &
                                (df.Product==product) & (df.Year==years[0])]["Mean_Price_Norm"].iloc[0]
                last_price_norm = df[(df.Macroregion==region) & (df.State==state) &
                                (df.Product==product) & (df.Year==years[-1])]["Mean_Price_Norm"].iloc[-1]
                price_pct_change_norm = (last_price_norm - first_price_norm) / np.abs(first_price_norm)

                # Add to dataframe
                df_temp = pd.DataFrame({"Macroregion":region, "State":state,
                                        "Product":product,
                                        "First_Year":years[0], "Last_Year":years[-1],
                                        "Fuel_Mean_Price":mean_price,
                                        "First_Price":first_price, "Last_Price":last_price, "Price_Pct_Change":price_pct_change,
                                        "First_Price_Norm":first_price_norm,
                                        "Last_Price_Norm":last_price_norm,
                                        "Price_Pct_Change_Norm":price_pct_change_norm
                                       },
                                       index=[count])

                df_pct_change = df_pct_change.append(df_temp)

                count += 1

    # Group by percentage change by macroregion
    df_pct_change_region = df_pct_change.groupby(['Macroregion', 'Product']).mean().reset_index()

    print("Merging geospatial data...")

    # Merge new datasets with spatial data
    brazil_geo = brazil_geo.drop('Macroregion', axis=1).merge(df_pct_change, on='State')
    brazil_geo_region = brazil_geo_region.merge(df_pct_change_region, on='Macroregion')

    # Correct datatypes
    for col in ['First_Year', 'Last_Year']:
        brazil_geo_region[col] = brazil_geo_region[col].astype(int)

    # Save geographical data to disk
    print("Saving...")
    brazil_geo.to_csv('./data/interim/brazilfuelgeo.csv')
    brazil_geo_region.to_csv('./data/interim/brazilfuelregion.csv')

    print("Finished.")

if __name__ == "__main__":
    load_geo_data()
