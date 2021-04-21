# Author: Letian Wu
# Written: April 2021
import pandas as pd
import json
import pprint
from pandas import DataFrame

#Part 1
def read_csv(csv_path: str) -> DataFrame:
    rev_df = pd.read_csv(csv_path)
    print("There are {} rows in the raw dataset".format(rev_df.shape[0]))
    return rev_df

def remove_non_numerical(rev_df: DataFrame) -> DataFrame:
    rev_df = rev_df[pd.to_numeric(rev_df['Profit (in millions)'], errors='coerce').notnull()].copy()
    rev_df['Profit (in millions)'] = pd.to_numeric(rev_df['Profit (in millions)'])
    print("There are {} rows in the updated dataset".format(rev_df.shape[0]))
    return rev_df

#Part 2
def store_as_json(rev_df: DataFrame) -> None:
    rev_df.to_json(path_or_buf="data2.json",orient="table")
    #alternative:with open('data2.json', 'w') as out_file: json.dump(valid_data, out_file, indent=2)

def sort_rev_df(rev_df: DataFrame) -> DataFrame:
    rev_df.sort_values(by=['Profit (in millions)'], inplace=True, ascending=False, ignore_index=True)
    print("Top 20 company with highest profit values")
    print(rev_df.head(20))
    return rev_df

# main
if __name__ == '__main__':
    data_path = "data.csv"

    company_rev_df = read_csv(data_path)
    pprint.pprint(company_rev_df, indent=1)
    company_rev_df = remove_non_numerical(company_rev_df)
    pprint.pprint(company_rev_df, indent=1)

    store_as_json(company_rev_df)
    sort_rev_df(company_rev_df)
