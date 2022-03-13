import pandas as pd
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("data.csv")
data = df["Math_score"].tolist()

def pickSample():
    dataset = []
    for i in range(0, 100):
        index = random.randint(0, len(data)-1)
        value = data[index]
        dataset.append(value)
    mean1 = st.mean(dataset)
    return mean1

meanlist = []
for i in range(0, 1000):
    setofmean = pickSample()
    meanlist.append(setofmean)

df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()

meanSample = st.mean(data)
stdevSample = st.stdev(data)

mean = st.mean(meanlist)
stdev = st.stdev(meanlist)

print(mean, stdev) 

""" first_stdev_start, first_stdev_end = mean - stdev, mean + stdev
second_stdev_start, second_stdev_end = mean - (2*stdev), mean + (2*stdev)
third_stdev_start, third_stdev_end = mean - (3*stdev), mean + (3*stdev)

fig = ff.create_distplot([meanlist], ["Marks for group 1"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.45], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x=[meanSample, meanSample], y=[0, 0.45], mode = "lines", name = "mean of sample"))

fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.45], mode = 'lines', name = "second stdev end"))
fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.45], mode = 'lines', name = "third stdev end"))
 """
# fig.show()

zScore = (meanSample - mean)/stdev
print(zScore)