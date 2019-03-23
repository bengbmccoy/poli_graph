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

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('data', type=str,
                        help='csv data file you would like to visualise')

    args=parser.parse_args()

    if args.data:
        data_df = pd.read_csv(args.data, index_col=0, parse_dates=True)
        # print data_df
        print 'data_df is collected'

    time = data_df.index.tolist()
    bernie = data_df['Bernie Sanders'].tolist()[0::4]
    biden = data_df['Joe Biden'].tolist()[0::4]
    kamala = data_df['Kamala Harris'].tolist()[0::4]
    beto = data_df['Beto O\'Rourke'].tolist()[0::4]

    # plt.plot(bernie, label="Bernie")
    # plt.plot(biden, label="Biden")
    # plt.plot(kamala, label='Kamala')
    # plt.plot(beto, label='Beto')
    # plt.legend()
    # # plt.show()
    #
    # plt.draw()
    # plt.pause(0.0001)
    # plt.clf()


    plt_bernie = []
    plt_biden = []
    plt_beto = []
    plt_kamala =[]
    for i in range(len(time)):
        plt_bernie.append(bernie[i])
        plt_biden.append(biden[i])
        plt_kamala.append(kamala[i])
        plt_beto.append(beto[i])
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

    # plt.plot(bernie, label="Bernie")
    # plt.plot(biden, label="Biden")
    # plt.plot(kamala, label='Kamala')
    # plt.plot(beto, label='Beto')
    # plt.legend()
    # plt.show()

main()
