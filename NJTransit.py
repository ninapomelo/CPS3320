import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib import style
import matplotlib.cm as cm, matplotlib.font_manager as fm
import matplotlib.ticker as ticker
from datetime import datetime, timedelta
from scipy.stats import norm
%matplotlib inline

# import the data
df = pd.read_csv('/Users/nina/Desktop/fp/2018_03.csv')
for i in range(4,10):
    df = df.append(pd.read_csv('/Users/nina/Desktop/fp/2018_0'+str(i)+'.csv'))
df = df[df['type'] == 'NJ Transit']

df_july = pd.read_csv('/Users/nina/Desktop/fp/2018_08.csv', index_col = False)
df_july = df_july[df_july['type'] == 'NJ Transit']

#drop na value                     
df = df.dropna()
df_july = df_july.dropna()
                      

#Converting the "scheduled_time" and "actual_time" columns to datetime
df['actual_time'] = pd.to_datetime(df['actual_time'])
df_july.head(2)

df_july['scheduled_time'] = pd.to_datetime(df_july['scheduled_time']) 
df_july['actual_time'] = pd.to_datetime(df_july['actual_time'])
df_july.head(2)

def pie_chart(fractions, #values for the wedges
              labels, #labels for the wedges
              title = '', #title of the pie chart
              cm_name = 'Pastel1', #name of the matplotlib colormap to use
              autopct = lambda x: str(round(x, 1)) + '%', #format the value text on each pie wedge
              labeldistance = 1.05, #where to place wedge labels in relation to pie wedges
              shadow = True, #shadow around the pie
              startangle = 90, #rotate 90 degrees to start the top of the data set on the top of the pie
              edgecolor = 'w', #color of pie wedge edges
              width = 8, #width of the figure in inches
              height = 8, #height of the figure in inches
              grouping_threshold = None, #group all wedges below this value into one 'all others' wedge
              grouping_label = None): #what to label the grouped wedge
    # if the user passed a threshold value, group all fractions lower than it into one 'misc' pie wedge
    if not grouping_threshold==None:
        
        # if user didn't pass a label, apply a default text
        if grouping_label == None:
            grouping_label = 'Others'


        # group all other rows below the cut-off value
        all_others = pd.Series(fractions[~row_mask].sum())
        all_others.index = [grouping_label]
    
    # get the color map then pull 1 color from it for each pie wedge we'll draw
    color_map = cm.get_cmap(cm_name)
    num_of_colors = len(fractions)
    colors = color_map([x/float(num_of_colors) for x in range(num_of_colors)])
    
    # create the figure and an axis to plot on
    fig, ax = plt.subplots(figsize=[width, height])
    
    # plot the pie
    wedges = ax.pie(fractions, 
                    labels = labels, 
                    labeldistance = labeldistance,
                    autopct = autopct,
                    colors = colors,
                    shadow = shadow, 
                    startangle = startangle)
    
    # change the edgecolor for each wedge
    for wedge in wedges[0]:
        wedge.set_edgecolor(edgecolor)
    
    # set the title and show the plot
    ax.set_title(title)
    plt.show()
# Picking July for More Analysis
#The cumulative delay for a train is simply the "delay" value for the last stop for the train:
cumu_delay_july = df_july.groupby(['date' , 'train_id']).last()
cumu_delay_july .head(2)

#july
ontime_trains_july = cumu_delay_july[(cumu_delay_july['delay_minutes']<=0)]
ontime_trains_count_july = ontime_trains_july['delay_minutes'].count()

cancelled_trains = df_july[(df_july['status'] == 'cancelled')]
cancelled_trains_count = cancelled_trains['train_id'].count()

delayed_trains_july = cumu_delay_july[(cumu_delay_july['delay_minutes']>0)]
delayed_trains_count_july = delayed_trains_july['delay_minutes'].count()

df_march = pd.read_csv('/Users/nina/Desktop/fp/2018_03.csv', index_col = False)
df_march = df_march[df_march['type'] == 'NJ Transit']
df_march = df_march.dropna()

df_april = pd.read_csv('/Users/nina/Desktop/fp/2018_04.csv', index_col = False)
df_april = df_april[df_april['type'] == 'NJ Transit']
df_april = df_april.dropna()

df_may = pd.read_csv('/Users/nina/Desktop/fp/2018_05.csv', index_col = False)
df_may = df_may[df_may['type'] == 'NJ Transit']
df_may = df_may.dropna()

df_june = pd.read_csv('/Users/nina/Desktop/fp/2018_06.csv', index_col = False)
df_june = df_june[df_june['type'] == 'NJ Transit']
df_june = df_june.dropna()

df_august = pd.read_csv('/Users/nina/Desktop/fp/2018_08.csv', index_col = False)
df_august = df_august[df_august['type'] == 'NJ Transit']
df_august = df_august.dropna()

df_september = pd.read_csv('/Users/nina/Desktop/fp/2018_09.csv', index_col = False)
df_september = df_september[df_september['type'] == 'NJ Transit']
df_september = df_september.dropna()

cumu_delay_march = df_march.groupby(['date' , 'train_id']).last()
cumu_delay_april = df_april.groupby(['date' , 'train_id']).last()
cumu_delay_may = df_may.groupby(['date' , 'train_id']).last()
cumu_delay_june = df_june.groupby(['date' , 'train_id']).last()
cumu_delay_august = df_august.groupby(['date' , 'train_id']).last()
cumu_delay_september = df_september.groupby(['date' , 'train_id']).last()

delayed_trains_march = cumu_delay_march[(cumu_delay_march['delay_minutes']>0)]
delayed_trains_count_march = delayed_trains_march['delay_minutes'].count()

delayed_trains_april = cumu_delay_april[(cumu_delay_april['delay_minutes']>0)]
delayed_trains_count_april = delayed_trains_april['delay_minutes'].count()

delayed_trains_may = cumu_delay_may[(cumu_delay_may['delay_minutes']>0)]
delayed_trains_count_may = delayed_trains_may['delay_minutes'].count()

delayed_trains_june = cumu_delay_june[(cumu_delay_june['delay_minutes']>0)]
delayed_trains_count_june = delayed_trains_june['delay_minutes'].count()

delayed_trains_august = cumu_delay_august[(cumu_delay_august['delay_minutes']>0)]
delayed_trains_count_august = delayed_trains_august['delay_minutes'].count()

delayed_trains_september = cumu_delay_september[(cumu_delay_september['delay_minutes']>0)]
delayed_trains_count_september = delayed_trains_september['delay_minutes'].count()

delay_data_per_month = [ delayed_trains_count_march , delayed_trains_count_april ,delayed_trains_count_may, delayed_trains_count_june ,delayed_trains_count_july, delayed_trains_count_august , delayed_trains_count_september]
labels = 'march', 'April' , 'May' , 'June' , 'July' , 'August' , 'September'

delay_data_per_month = [ delayed_trains_count_march , delayed_trains_count_april ,delayed_trains_count_may, delayed_trains_count_june ,delayed_trains_count_july, delayed_trains_count_august , delayed_trains_count_september]
labels = 'march', 'April' , 'May' , 'June' , 'July' , 'August' , 'September'
# test out our function
pie_chart(fractions = delay_data_per_month,
          labels = labels,
          title = 'Delay Report Per Month')

#july
delay_data = [ontime_trains_count_july, delayed_trains_count_july , cancelled_trains_count]
labels = 'OnTime', 'Delayed' , 'Cancelled'
# test out our function
pie_chart(fractions = delay_data,
          labels = labels,
          title = ' July')

#Probability Density Function (PDF) for Delay
mu = df['delay_minutes'].mean() # mean of distribution
sigma = df['delay_minutes'].std()  # standard deviation of distribution
x = (df['delay_minutes'] *sigma ) + mu 
y = norm.pdf(bins, mu, sigma)

num_bins = 50

fig, ax = plt.subplots(figsize=(8, 4))

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=1)
ax.plot(bins, y, '--')

ax.set_xlabel('Delay (min)')
ax.set_ylabel('Density')
ax.set_title('Train delay time density')
ax.set_xlim(0,130)
ax.set_ylim(0,0.04)
plt.show()


# delay minutes per day in July
week_av_delay_july = df_july.groupby(df_july['day_of_weeks'] ,as_index = False )['delay_minutes'].mean()
week_av_delay_july['num'] = [5,1,6,7,4,2,3]
week_av_delay_july

fig, ax = plt.subplots()
fig.set_size_inches(9, 4)
week_av_delay_july_scatter = ax.scatter(x = week_av_delay_july['num'], y = week_av_delay_july['delay_minutes'], c='m', edgecolor='k', alpha=.4, s=150)


# set  axis labels

ax.set_xlabel('Week (july)')
ax.set_ylabel('Average Delay (min)')

# annotate
bbox_style = {'boxstyle':'round', 'color':'k', 'fc':'w', 'alpha':0.8}
arrowprops_style = {'arrowstyle':'->', 'connectionstyle':'arc3,rad=0.5', 'color':'k', 'alpha':0.8}
annotate_day_of_weeks_july = lambda row: ax.annotate(row['day_of_weeks'], 
                                          xy=(row['num'], row['delay_minutes']),
                                          xytext=(row['num'] + 0.1, row['delay_minutes'] + 0.1),
                                          bbox=bbox_style,
                                          xycoords='data',
                                          arrowprops=arrowprops_style)
week_av_delay_july.apply(annotate_day_of_weeks_july, axis=1)
plt.show()

#Most Delayed Lines in july

lines = df_july.groupby(['train_id']).last()
lines.head(2)
lines_cumu_delay_july = lines.groupby('line')['delay_minutes'].sum().sort_values(ascending=False)
lines_cumu_delay_july
line_usage = lines['line'].value_counts()
line_usage
lines_stop_sequence = lines.groupby('line')['stop_sequence'].sum().sort_values(ascending=False)
lines_stop_sequence


bar_width = 0.25
error_config = {'ecolor': '0.3'}

ax = line_usage.plot(kind = 'bar', figsize=[9, 4], width = bar_width, position=1 , alpha=0.6, 
                    color='g', edgecolor='k', grid=False, ylim=[0, 225] , error_kw = error_config,
                 label='Number of Trips')

ax.set_xticklabels(line_usage.index, rotation=45, rotation_mode='anchor', ha='right')
ax.yaxis.grid(True)
   


ax.set_ylabel('Number of Train records for Each Line',  color='g')
ax.tick_params('y', colors='g')

ax2 = ax.twinx()

ax2 =lines_cumu_delay_july.plot( kind = 'bar' , figsize=[9, 4], width= bar_width, position = 0, alpha=0.6, 
                    color='r', edgecolor='k', grid=False, ylim=[0, 700] , error_kw=error_config,
                 label='Delay (min)')

ax2.set_xticklabels(lines_cumu_delay_july.index, rotation=45, rotation_mode='anchor', ha='right')



ax2.set_ylabel('Delay (min)' , color='r')
ax2.tick_params('y', colors='r')

ax = lines_stop_sequence.plot(kind='bar', figsize=[9, 9], width= bar_width, alpha=0.6, position = 1,
                    color='b', edgecolor='k', grid=False, ylim=[0, 5000])

ax.set_xticklabels(lines_stop_sequence.index, rotation=45, rotation_mode='anchor', ha='right')
ax.yaxis.grid(True)
   
ax.set_ylabel('Number of Stops' , color='y')
ax.tick_params('y', colors='y')

ax2 = ax.twinx()

ax2 =lines_cumu_delay_july.plot( kind = 'bar' , figsize=[9, 4], width= bar_width, position = 0, alpha=0.6, 
                    color='r', edgecolor='k', grid=False, ylim=[0, 700] , error_kw=error_config,
                 label='Delay (min)')

ax2.set_xticklabels(lines_cumu_delay_july.index, rotation=45, rotation_mode='anchor', ha='right')



ax2.set_ylabel('Delay (min)' , color='r')
ax2.tick_params('y', colors='r')
#Numbers of Stops have a Direct Relationship with Delay


stations = df_july.groupby(['train_id']).last()
stations.head(2)
stations_to_usage = stations['to'].value_counts().head(10)
stations_to_cumu_delay_july = stations.groupby('to')['delay_minutes'].sum().sort_values(ascending=False).head(10)
stations_stop_sequence = stations.groupby('to')['stop_sequence'].sum().sort_values(ascending=False).head(10)
stations_to_usage


ax = stations_to_usage.plot(kind='bar', figsize=[9, 9], width= bar_width, alpha=0.6, position = 1,
                    color='orange', edgecolor='k', grid=False, ylim=[0, 300])

ax.set_xticklabels(stations_to_usage.index, rotation=45, rotation_mode='anchor', ha='right')
ax.yaxis.grid(True)
   
ax.set_ylabel('Number of Trains ' , color='orange')
ax.tick_params('y', colors='orange')

ax2 = ax.twinx()

ax2 =stations_to_cumu_delay_july.plot( kind = 'bar' , figsize=[9, 4], width= bar_width, position = 0, alpha=0.6, 
                    color='r', edgecolor='k', grid=False, ylim=[0, 900] , error_kw=error_config,
                 label='Delay(min)')

ax2.set_xticklabels(stations_to_cumu_delay_july.index, rotation=45, rotation_mode='anchor', ha='right')



ax2.set_ylabel('Delay(min)' , color='r')
ax2.tick_params('y', colors='r')
# Number of TRIPS has a Direct Relationship with Delay the same as lines