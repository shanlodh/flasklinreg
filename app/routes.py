from app import app, linreg_deserialized
from flask import request, jsonify
import numpy as np

@app.route('/index')
def indexHandler():
    return ("index page")

@app.route('/prediction', methods=['POST'])
def onlinePredictor():
    print(request.is_json)
    content = request.get_json()
    print(type(content))
    print(content)
    content['Wage']
    predict = linreg_deserialized.predict(np.array([[content['Wage']]]))
    print(predict)
    #return jsonify(predict.tolist())
    return ("The predicted price, based on wage of {}, is {}".format(content['Wage'],
                                                                     round(predict[0][0], 2)))
