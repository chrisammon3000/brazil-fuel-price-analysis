# Import data science libraries
import numpy as np
import pandas as pd
import os

# Import geospaitial libraries
import geopandas as gpd
from shapely.geometry import Point

# Read data
print("Reading data...")

def load_data():
    path = "./data/raw/2004-2019.tsv.zip"
    df = pd.read_csv(path, sep='\t',parse_dates=True)

    # Fixing data
    print("Cleaning data...")

    # Translate column names to English
    df.columns = ["Unnamed:_0",
    "Analysis_Date",
    "Last day of analyses of week",
    "Macroregion",
    "State",
    "Product",
    "No of Gas Stations Analyzed",
    "Measurement unit",
    "Mean Price",
    "Std Dev",
    "Min Price",
    "Max Price",
    "Mean Price Margin",
    "Coefficient of variation",
    "Mean Dist Price",
    "Distribution Std Dev",
    "Distribution Min Price",
    "Distribution Max Price",
    "Distribution Coefficient of Variation",
    "Month",
    "Year"]

    # Replace whitespace with underscore
    df.columns = df.columns.str.replace(" ", "_")
    df.columns = df.columns.str.replace("'", "")
    df.columns = df.columns.str.replace("Distribution", "Dist")

    # Convert datetime columns to datetime objects and rename
    df["Analysis_Date"] = pd.to_datetime(df["Analysis_Date"])

    # Correct dtypes
    float_columns = ['Mean_Price_Margin', 'Mean_Dist_Price', 'Dist_Std_Dev',
           'Dist_Min_Price', 'Dist_Max_Price',
           "Dist_Coefficient_of_Variation"]

    # Replace "-" with 0 in order to convert to float
    for column in float_columns:
        df[column] = df[column].str.replace("-", "0")

    # Fill nulls and convert to float
    df[float_columns] = df[float_columns].fillna(0).astype(float)

    assert df[float_columns].dtypes.all() == np.float64

    # Rename Product categories
    products = {"ÓLEO DIESEL":"DIESEL", "GASOLINA COMUM":"PETROL", "GLP":"LPG",
                "ETANOL HIDRATADO":"HYDROUS ETHANOL", "GNV":"NATURAL GAS",
                "ÓLEO DIESEL S10":"DIESEL S10"}

    df["Product"] = df.Product.map(products)

    # Rename Measurement_unit categories
    units = {"R$/l":"liter", "R$/13Kg":"13kg", "R$/m3":"m3"}

    df["Measurement_unit"] = df["Measurement_unit"].map(units)

    # Convert objects to category
    object_cols = df.select_dtypes(include='object').columns
    df[object_cols] = df[object_cols].astype('category', inplace=True)

    # Create Price Groups: Group 1 are liquid fuels plus Natural Gas, Group 2 is LPG
    df['Price_Group'] = df.Measurement_unit.map({'liter':int(1), 'm3':int(1),
                                                 '13kg':int(2)})

    # Normalize Mean Price for each fuel group
    normalizer = lambda x: (x - x.min()) / (x.max() - x.min())

    # Normalize Prices for Price_Group_1: all fuels except LPG
    df["Mean_Price_Norm_Price_Group_1"] = df[df.Price_Group==1].groupby("Product")["Mean_Price"].transform(normalizer)

    # Normalize Prices for Price_Group_2: LPG
    df["Mean_Price_Norm_Price_Group_2"] = df[df.Price_Group==2].groupby("Product")["Mean_Price"].transform(normalizer)

    # Combine Price_Group columns into one column
    df["Mean_Price_Norm"] = df["Mean_Price_Norm_Price_Group_1"].fillna(df["Mean_Price_Norm_Price_Group_2"])
    df.drop(["Mean_Price_Norm_Price_Group_1", "Mean_Price_Norm_Price_Group_2"],
            axis=1, inplace=True)

    # Create Year_Month column for time series plots
    year_month = df.Year.astype(str) + "-" + df.Month.astype(str)
    df["Year_Month"] = pd.to_datetime(year_month)

    # These columns are no longer needed
    df.drop(['Unnamed:_0', 'Last_day_of_analyses_of_week'], axis = 1, inplace=True)

    # Save clean dataset
    print("Saving clean dataset...")
    df.to_csv('./data/interim/brazilfuel.csv')

    print("Finished.")

    return df

if __name__ == "__main__":
    load_data()
