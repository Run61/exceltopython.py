# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:51:47 2021

@author: user
"""


import os
import pandas as pd
import matplotlib.pyplot as plt


def nomalize_data(df):
    return df/df.iloc[0]

def plot_selected(df, columns, start_index, end_index):
    df = df.loc[start_index:end_index, columns]
    df = nomalize_data(df)
    plot_data(df)

def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)
    if 'sam' not in symbols:
        symbols.insert(0, 'sam')
        
        for symbol in symbols:
            df_temp = pd.read_csv(symbol_to_path(symbol), index_col='date',
                                  parse_dates=True, usecols=['date', 'close'],
                                  na_values=['nan'])
            df_temp =df_temp.rename(columns={'close':symbol})
            
            df = df.join(df_temp)
            
            if symbol == 'sam':
                df = df.dropna(subset=["sam"])
                
    return df



def plot_data(df, title="Stock prices"):
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()
    
def test_run():
    dates = pd.date_range('2015-01-01', ' 2019-12-31')
    symbols = ['mezzi', 'helix', 'skhy']
    df = get_data(symbols, dates)
    plot_selected(df, ['sam', 'skhy', 'mezzi'], '2018-01-01', '2018-12-31')

"""
if __name__ == "__main__":
"""
test_run()


