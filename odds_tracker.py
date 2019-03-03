# sportsbet.py

'''
Written: Ben McCoy 201903

A script that tracks the betting odds of 2020 US presidential candidates on
sportsbet.

This script will be scheduled to run multiple times per day on a remote
raspberry pi and will scrap the sportsbet.com.au website to track the odds
of the democratic presidential front runners.

Tasks:
- Init a dataframe --> DONE
- Scrape the sportsbet website for front runners and prices --> DONE
- update the df --> DONE
- save the df --> DONE

TODO:
- Expand the script to scrape all possible candidates and not just top 5
- Write tests for the script to ensure that it is robust

'''



from lxml import html
import requests
import pandas as pd
import time

def main():

    runners, prices = get_runner_prices()
    # print runners, prices
    print 'runners and prices collected'

    # df = init_df(runners, prices)
    # print df
    # print 'df initialised'

    df = open_csv('odds.csv')
    # print df
    print "df is loaded"

    update_df(df, prices, runners)
    # print df
    print 'df_is updated'

    save_df(df, 'odds.csv')
    # print df
    print "df is saved as odds.csv"

def save_df(df, file_name):
    ''' Saves the dataframe as a csv'''

    df.to_csv(file_name, encoding='utf-8', index=True)

def open_csv(file_name):
    ''' opens the dataframe with the index columns as the first column and the
    values parsed as dates
    '''

    return pd.read_csv(file_name, index_col=0, parse_dates=True)

def update_df(df, prices, runners):
    ''' Updates the df with the variables passed in'''

    df.loc[pd.Timestamp('now')] = pd.Series(prices, runners)

    return df

def get_runner_prices():
    ''' Scrapes the sportsbet website and searches through the html using
    xpath to find a list of candidates and a list of prices that they are
    being valued at
    '''

    page = requests.get('https://www.sportsbet.com.au/betting/politics/us-politics/us-presidential-election-2020-2982545')
    tree = html.fromstring(page.content)
    runners = tree.xpath('//span[@class="size14_f7opyze outcomeName_f19a8l1b"]/text()')
    prices = tree.xpath('//span[@class="size14_f7opyze medium_f1wf24vo priceTextSize_frw9zm9"]/text()')
    return runners, prices

def init_df(runners, prices):
    ''' initialises a pandas df that has the index set as a dataframe and
    appends athe first row with the current datetime and runners and prices
    '''

    df = pd.DataFrame(columns=[runners], index=pd.to_datetime([]))
    df.loc[pd.Timestamp('now')] = pd.Series(prices, runners)

    return df

main()
