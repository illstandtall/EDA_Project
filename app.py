from flask import Flask, jsonify, request, render_template
from plots import *

app = Flask(__name__)


@app.route('/')
def eda():
    corrJSON = corr()
    return render_template('eda.html', plots={"corr": corrJSON})


@app.route('/type')
def types():
    l_rJSON = l_r()
    am_temJSON = am_tem()
    am_l_temJSON = am_l_tem()
    p_cJSON = p_c()
    return render_template('type.html', plots={"l_r": l_rJSON, "am_tem": am_temJSON, 
                            "am_l_tem": am_l_temJSON, "p_c": p_cJSON})


@app.route('/color')
def color():
    color_cntJSON = color_cnt()
    color_amJSON = color_am()
    tem_amJSON = color_tem_am()
    am_3dJSON = color_3d()
    return render_template('color.html', plots={"color_cnt": color_cntJSON, "color_am": color_amJSON, 
                                                "tem_am": tem_amJSON, "am_3d": am_3dJSON})



if __name__ == '__main__':
    app.run(debug=True)