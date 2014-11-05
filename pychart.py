from pygooglechart import SimpleLineChart, Axis
chart = SimpleLineChart(200, 125)
data = [ 1, 5, 30, 10, 25 ]
chart.add_data(data)
chart.set_axis_range(Axis.LEFT, 0, 10)
chart.download("hello.png")
print chart.get_url()
