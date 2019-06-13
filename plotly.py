import plotly.offline as pyo
import plotly.graph_objs as go



#scater graph
data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
)]


#desging for title and others
layout = go.Layout(
    title = 'Random Data Scatterplot', # Graph title
    xaxis = dict(title = 'Some random x-values'), # x-axis label
    yaxis = dict(title = 'Some random y-values'), # y-axis label
    hovermode ='closest' # handles multiple points landing on the same vertical
)

#compiling the both layout and data
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter2.html')#ploting
