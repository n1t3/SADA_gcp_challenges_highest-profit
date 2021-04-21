import pandas as pd
import json
from pandas import DataFrame



def read_csv(csv_path: str) -> DataFrame:
    revenue_df = pd.read_csv(csv_path)
    '''column_mapping = {"Revenue (in millions)":"Revenue",
                   "Profit (in millions)": "Profit (in millions)"
                  }
    revenue_df.rename(columns=column_mapping, inplace=True)'''
    print("There are {} rows in the raw dataset".format(revenue_df.shape[0]))
    return revenue_df

def remove_non_numerical(revenue_df: DataFrame) -> DataFrame:
    revenue_df = revenue_df[pd.to_numeric(revenue_df['Profit (in millions)'], errors='coerce').notnull()].copy()
    revenue_df['Profit (in millions)'] = pd.to_numeric(revenue_df['Profit (in millions)'])
    revenue_df.drop(['Profit (in millions)'], axis=1, inplace=True)
    revenue_df.reset_index(inplace=True)
    revenue_df.drop(['index'], axis=1, inplace=True)
    print("There are {} rows in the dataset".format(revenue_df.shape[0]))
    return revenue_df

def store_json(revenue_df: DataFrame) -> None:
    revenue_df.to_json(path_or_buf="data2.json",orient="table")

def sort_revenue_df(revenue_df: DataFrame) -> DataFrame:
    revenue_df.sort_values(by=['Profit (in millions)'], inplace=True, ascending=False, ignore_index=True)
    print("Top 20 rows with highest Profit  values")
    print(revenue_df.head(20))
    return revenue_df

if __name__ == '__main__':
    data_path = "data.csv"

    company_revenue_df = read_csv(data_path)
    company_revenue_df = remove_non_numerical(company_revenue_df)


    store_json(company_revenue_df)
    sorted_revenue_df = sort_revenue_df(company_revenue_df)
