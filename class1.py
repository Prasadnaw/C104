import csv

with open("D:\Desktop\python class\C104\class1.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

total_marks = 0
total_entries = len(file_data)

for marks in file_data:
    total_marks += float(marks[1])

mean = total_marks / total_entries

print("Mean Average is", str(mean))

import pandas as pd
import plotly.express as px

df = pd.read_csv("D:\Desktop\python class\C104\class1.csv")
fig = px.scatter(df, x="Student Number", y= "Marks")

fig.update_layout(shapes=[
    dict(
        type = 'line',
        y0= mean, y1 = mean,
        x0= 0, x1= total_entries
    )
])

fig.update_yaxes(rangemode="tozero")
fig.show()