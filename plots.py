import os, json

import numpy as np
import pandas as pd

import plotly as py
import plotly.express as px
import plotly.graph_objects as go


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
stars = pd.read_csv(os.path.join(BASE_DIR, 'static/datasets/Stars.csv'))

new_colors = {
    'Red': 'Red',
    'Blue White': 'Blue',
    'White': 'White',
    'Yellowish White': 'Yellow',
    'Blue white': 'Blue',
    'Pale yellow orange': 'Yellow',
    'Blue': 'Blue',
    'Blue-white': 'Blue',
    'Whitish': 'White',
    'yellow-white': 'Yellow',
    'Orange': 'Red',
    'White-Yellow': 'White',
    'white': 'White',
    'yellowish': 'Yellow',
    'Yellowish': 'Yellow',
    'Orange-Red': 'Red',
    'Blue-White': 'Blue'
}
Color = stars.Color.map(new_colors)
stars.Color = Color


def corr():
    fig = px.imshow(stars.corr(), title="데이터 속성 값의 상관계수")
    graphJSON = json.dumps(fig, cls=py.utils.PlotlyJSONEncoder)
    return graphJSON


def attributes():
    graphs = {}
    for col in stars.columns[:-3]:
        fig = px.scatter(data_frame=stars, x="Type", y=col, color="Type", 
                 title="별의 분류별 속성 " + str(col) + "에 대한 분포")
        fig.show()
        graphs[col] = json.dumps(fig, cls=py.utils.PlotlyJSONEncoder)
    return graphs

def l_r():
    fig = px.scatter(data_frame=stars, x="L", y="R", color="Type", 
                 title="별의 분류에 따른 상대 밝기와 상대 반지름 분포")
    graphJSON = json.dumps(fig, cls=py.utils.PlotlyJSONEncoder)
    return graphJSON

def am_tem():
    fig = px.scatter(data_frame=stars, x="A_M", y="Temperature", color="Type", 
                 title="별의 분류에 따른 절대 등급과 온도의 분포")
    graphJSON = json.dumps(fig, cls=py.utils.PlotlyJSONEncoder)
    return graphJSON

def am_l_tem():
    fig = px.scatter_3d(stars,
                    x='L',
                    y='Temperature',
                    z='A_M',
                    color='Type',
                    opacity=0.7)
    graphJSON = json.dumps(fig, cls=py.utils.PlotlyJSONEncoder)
    return graphJSON

def p_c():
    fig = px.parallel_coordinates(stars, color="Type", labels={"Temperature": "Temperature",
                    "L": "Relative Luminous", "R": "Relative Radious", "A_M": "Absolute Magnitude"},
                    title="별 속성의 평행 좌표 그래프")
    graphJSON = json.dumps(fig, cls=py.utils.PlotlyJSONEncoder)
    return graphJSON


def color_cnt():
    fig = px.bar(data_frame=stars, x="Type", y="Color", color="Type", 
             title="색깔/분류별 별의 수")
    graphJSON = json.dumps(fig, cls=py.utils.PlotlyJSONEncoder)
    return graphJSON

def color_am():
    fig = px.bar(data_frame=stars, x="Color", y="A_M", color="Type", 
             title="색깔/분류별 별의 절대 등급")
    graphJSON = json.dumps(fig, cls=py.utils.PlotlyJSONEncoder)
    return graphJSON

def color_tem_am():
    fig = px.scatter(data_frame=stars, x="A_M", y="Temperature", color="Color", 
                title="색깔별 절대등급(A_M)과 온도(Temperature)의 분포", 
                color_discrete_map={ 'Red': 'red', 'Blue': 'blue',
                                    'White': 'gray', 'Yellow': 'yellow'},)
    graphJSON = json.dumps(fig, cls=py.utils.PlotlyJSONEncoder)
    return graphJSON

def color_3d():
    fig = px.scatter_3d(data_frame=stars, x="L", y="R", z="A_M", color="Color", 
            title="색깔별 절대등급(A_M)과 상대 밝기(L), 상대 반지름(R)의 분포", 
            color_discrete_map={ 'Red': 'red', 'Blue': 'blue',
                                'White': 'gray', 'Yellow': 'yellow'},)
    graphJSON = json.dumps(fig, cls=py.utils.PlotlyJSONEncoder)
    return graphJSON