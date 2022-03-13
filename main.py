import pandas as pd
import statistics as st
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
data = df["Math_score"].tolist()

mean = st.mean(data)
stdev = st.stdev(data)

fig = ff.create_distplot([data], ["Marks"], show_hist = False)
fig.show()

#print(mean, stdev)