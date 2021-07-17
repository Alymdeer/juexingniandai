from pyecharts.charts import Bar, Line
from pyecharts import options as opts
x_data =['0-19','20-29','30-39','40-49','50+']
bar = (
    Bar(init_opts=opts.InitOpts(width="1200px", height="600px"))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="觉醒年代",
        yaxis_data=[
            19.21,
            46.67,
            20.31,
            12.14,
            1.67,
        ],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="全网分布",
        yaxis_data=[
            11.03,
            32.75,
            33.05,
            17.1,
            6.06,
        ],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="TGI",
            type_="value",
            min_=0,
            max_=200,
            interval=40,
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
        )
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(
            is_show=True, trigger="axis", axis_pointer_type="cross"
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            min_=0,
            max_=50,
            interval=10,
            axislabel_opts=opts.LabelOpts(formatter="{value} %"),
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
)

line = (
    Line()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="TGI",
        yaxis_index=1,
        y_axis=[174.22,142.57,61.49,71.02,27.56],
        label_opts=opts.LabelOpts(is_show=False),
    )
)
bar.overlap( line ).render( "age.html" )