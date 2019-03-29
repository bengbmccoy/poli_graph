'''
Writte: Ben McCoy, 201903

This scipt will be used to help improve my data visualisation and presentation skills.
I will be using mostly matplotlib to perform this.

I will be using the following resources to learn matplotlib's data visualisation:
https://www.reddit.com/r/Python/comments/a07icu/a_complete_tutorial_on_data_visualization_with/?st=jtkpa4lz&sh=f792bbee
'''

import matplotlib.pyplot as plt
import argparse
import pandas as pd
import numpy as np

def get_opt_scale(time):
    for i in range(len(time)-1):
        if len(time)/(i+1) < 100:
            opt_scale = i
            break

    return opt_scale

def moving_plot(df):
    '''
    shows a moving plot of the odds of the candidates over time
    ensures that the X scale is reasonable and roughly around the 100 unit
    mark

    TODO:
    Include the donald
    Plot the X axis as time,
    title the figure and axes,
    Loads more fun stuff
    '''
    time = df.index.tolist()

    # determine how to scale the x axis so it is not too slow
    opt_scale = get_opt_scale(time)

    bernie = df['Bernie Sanders'].tolist()[0::opt_scale]
    biden = df['Joe Biden'].tolist()[0::opt_scale]
    kamala = df['Kamala Harris'].tolist()[0::opt_scale]
    beto = df['Beto O\'Rourke'].tolist()[0::opt_scale]

    plt_bernie = []
    plt_biden = []
    plt_beto = []
    plt_kamala =[]

    # Moving Plot
    for i in range(len(time)):
        plt_bernie.append(bernie[i])
        plt_biden.append(biden[i])
        plt_beto.append(beto[i])
        plt_kamala.append(kamala[i])
        plt.plot(plt_bernie, label='Bernie')
        plt.plot(plt_biden, label='Biden')
        plt.plot(plt_beto, label='Beto')
        plt.plot(plt_kamala, label='Kamala')
        plt.ylim(0, 1.5*max(bernie))
        plt.xlim(0, len(bernie))
        plt.draw()
        plt.legend()
        plt.pause(0.0001)
        plt.clf()

    # Final plot
    plt.plot(plt_bernie, label="Bernie")
    plt.plot(plt_biden, label="Biden")
    plt.plot(plt_beto, label='Beto')
    plt.plot(plt_kamala, label='Kamala')
    plt.ylim(0, 1.5*max(bernie))
    plt.xlim(0, len(bernie))
    plt.legend()
    plt.show()

def basic_plot(df):
    plt.style.use('ggplot')
    data_df_tran = df.last('1h').T
    data_df_tran.index.names = ['Candidates']
    data_df_tran.columns = ['Odds']
    data_df_tran = data_df_tran.reset_index()
    data_df_tran.sort_values(by='Odds', ascending=False, inplace=True)
    data_df_tran.plot(kind='barh', y='Odds', x='Candidates')
    plt.show()

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('data', type=str,
                        help='csv data file you would like to visualise')
    parser.add_argument('-m', '--moving',
                        help='displays moving odds over time',
                        action='store_true')
    parser.add_argument('-b', '--basic',
                        help='displays current basic odds',
                        action='store_true')

    args=parser.parse_args()

    if args.data:
        data_df = pd.read_csv(args.data, index_col=0, parse_dates=True)
        # print data_df
        print 'data_df is collected'

    if args.moving:
        moving_plot(data_df)

    if args.basic:
        basic_plot(data_df)



main()
