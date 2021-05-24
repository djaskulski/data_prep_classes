#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns


def hello_func() -> None:
    """Prints hello massage with Anscombe's quartet introduction. Returns: None"""

    print("Hello in Anscombe's quartet demo.\n")
    print(
        """    According to the definition given in Wikipedia, Anscombe’s quartet comprises four datasets 
        that have nearly identical simple statistical properties, yet appear very different when graphed. 
        Each dataset consists of eleven (x,y) points. They were constructed in 1973 by the statistician 
        Francis Anscombe to demonstrate both the importance of graphing data before analyzing it and the effect 
        of outliers on statistical properties.\n"""
    )


def makedir(name: str = "output") -> None:
    """
    Makes new directory.
    Parameters: name (str): Name your folder. (Default: 'output')
    Returns: None
    """

    resposne = input(f"Write 'ok' and confirm by hitting ENTER to make {name} dir.\n ")

    if resposne == "ok":
        try:
            os.makedirs(name)
            print(f"Have a nice new directory: {name}\n")

        except FileExistsError:
            print(f"Cannot create a file that already exists: {name}\n")

    else:
        print("Making new directory aborted.\n")


def data_as_anscombe(multi_index: bool = True, save: bool = False) -> pd.DataFrame:
    """
    Makes DataFrame from Anscombe quartet's data. Data included.
        Parameters:
            multi_index (bool): Adds multi index columns to DataFrame. (Default: True)
            save (bool): Create csv file with anscombe's dataframe. (Default: False)
        Returns: anscombe_df (DataFrame)
    """

    x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
    y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
    y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
    y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
    x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
    y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

    # Iterates len(x) times through zipped variables...
    # x[0], y1[0]... x[1], y1[1]... and return list of tuples.
    list_of_tuples = list(zip(x, y1, x, y2, x, y3, x4, y4))
    cols = ["x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4"]
    anscombe_df = pd.DataFrame(list_of_tuples, columns=cols)

    if multi_index:
        top_index = ["I", "I", "II", "II", "III", "III", "IV", "IV"]
        multi_cols = [np.array(top_index), np.array(cols)]
        anscombe_df.columns = multi_cols

    if save:
        anscombe_df.to_csv("output/anscombe_df.csv", index=False)

    return anscombe_df


def stats_in_frame(df: pd.DataFrame, save: bool = False) -> pd.DataFrame:
    """
    Makes DataFrame from Anscombe quartet's statistics. Uses anscombe_statistics function.
        Parameters:
            df (pd.DataFrame): Multi index DataFrame with anscombe's data.
            save (bool): Create csv file with calculated_stats_df. (Default: False)
        Returns: calculated_stats_df (DataFrame)
    """

    def anscombe_statistics(a: list, b: list, round_it: int = 2) -> list:
        """
        Calculates variance, mean, standard deviation and pearson correlation.
            Parameters:
                a: (array-like): Values to calculate.
                b: (array-like): Values 'b' are used only for correlation.
                round_it (int): Specified number of decimal. (Default: 2)
            Returns: [var, mean, std, corr] (list)
        """

        var = round(np.var(a), round_it)
        mean = round(np.mean(a), round_it)
        std = round(np.std(a), round_it)
        corr = round(pearsonr(a, b)[0], round_it)

        return [var, mean, std, corr]

    set_i = anscombe_statistics(df["I"]["x1"], df["I"]["y1"], round_it=3)
    set_ii = anscombe_statistics(df["II"]["x2"], df["II"]["y2"], round_it=3)
    set_iii = anscombe_statistics(df["III"]["x3"], df["III"]["y3"], round_it=3)
    set_iv = anscombe_statistics(df["IV"]["x4"], df["IV"]["y4"], round_it=3)

    columns = ["var", "mean", "std", "corr"]
    index = ["set_I", "set_II", "set_III", "set_IV"]
    data = [set_i, set_ii, set_iii, set_iv]
    calculated_stats_df = pd.DataFrame(data, index=index, columns=columns)

    if save:
        calculated_stats_df.to_csv("output/calculated_stats_df.csv", index_label="index")

    return calculated_stats_df


def stats_plot(df: pd.DataFrame, save: bool = False) -> plt:
    """
    Makes bar plot of given statistics.
        Parameters:
            df (pd.DataFrame):
            save (bool): Create csv file with calculated_set_df. (Default: False)
        Returns: plot (plt)
    """
    plot = df.plot(kind="bar", figsize=(9.5, 9), grid=True, legend=True,
                   title="Simple statistics comparison", rot=0)

    if save:
        plt.savefig("output/stats_plot.jpg")

    return plot


def sets_regplot(df: pd.DataFrame, save: bool = False) -> plt:
    """
    Makes scatter plot with regression line for given statistics.
        Parameters:
            df (pd.DataFrame): Multi index DataFrame with anscombe's data.
            save (bool): Create jpg file with sets_regplot. (Default: False)
        Returns: plot (plt)
    """

    fig, axes = plt.subplots(2, 2, figsize=(9.125, 9), sharex="all", sharey="all")
    plt.suptitle("Regression plot for Anscombe's quartet.")

    axes[0, 0].set(xlim=(2, 20), ylim=(2, 14))
    axes[0, 0].set(xticks=(range(2, 22, 2)), yticks=(range(2, 16, 2)))

    sns.regplot(x=df["I"]["x1"], y=df["I"]["y1"], ax=axes[0, 0],
                scatter_kws={"color": "green"}, line_kws={"color": "red"})
    axes[0, 0].title.set_text("Set I")
    axes[0, 0].grid()

    sns.regplot(x=df["II"]["x2"], y=df["II"]["y2"], ax=axes[0, 1],
                scatter_kws={"color": "green"}, line_kws={"color": "red"})
    axes[0, 1].title.set_text("Set II")
    axes[0, 1].grid()

    sns.regplot(x=df["III"]["x3"], y=df["III"]["y3"], ax=axes[1, 0],
                scatter_kws={"color": "green"}, line_kws={"color": "red"})
    axes[1, 0].title.set_text("Set III")
    axes[1, 0].grid()

    sns.regplot(x=df["IV"]["x4"], y=df["IV"]["y4"], ax=axes[1, 1],
                scatter_kws={"color": "green"}, line_kws={"color": "red"})
    axes[1, 1].title.set_text("Set IV")
    axes[1, 1].grid()

    if save:
        plt.savefig("output/sets_regplot.jpg")


def main():
    # introduction
    hello_func()

    # new directory for output
    makedir("output")

    # anscombe's data with simple statistics
    input("Press any key to see data ")
    my_anscombe_df = data_as_anscombe(multi_index=True, save=True)
    print(my_anscombe_df)
    my_calculated_stats_df = stats_in_frame(my_anscombe_df, save=True)
    print(my_calculated_stats_df)

    # bar plot for statistics, regression plot for anscombe's data
    input("Press any key to see plots ")
    stats_plot(my_calculated_stats_df, save=True)
    sets_regplot(my_anscombe_df, save=True)


if __name__ == "__main__":
    main()
