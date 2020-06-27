# import working libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import bar_chart_race as bcr

df = pd.read_csv('C:/Users/matth/OneDrive/Documents/Data Science/RacialEmployment/Earnings/barchartannualsalary.csv')
bcr.bar_chart_race(
    df=df,
    filename='C:/Users/matth/OneDrive/Documents/Data Science/RacialEmployment/Earnings/salary.mp4',
    orientation='h',
    sort='desc',
    n_bars=4,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=10,
    interpolate_period=False,
    label_bars=True,
    bar_size=.95,
    period_label={'x': .99, 'y': .35, 'ha': 'right', 'va': 'center','size': '9'},
    period_fmt='%B %d, %Y',
    period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                      's': f'Average Salary: {v.nlargest(6).mean():,.0f}',
                                      'ha': 'right', 'size': 8, 'family': 'Verdana'},
    perpendicular_bar_func='median',
    period_length=500,
    figsize=(5, 3),
    dpi=144,
    cmap='dark12',
    title='Salary by Ethnic Background',
    title_size='',
    bar_label_size=7,
    tick_label_size=7,
    shared_fontdict={'family' : 'Verdana', 'color' : '.1'},
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=False)  
bcr.bar_chart_race(df=df, filename=None)
