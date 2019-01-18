from app import app, linreg_deserialized
from flask import request, jsonify
import numpy as np

@app.route('/index')
def indexHandler():
    return ("index page")

@app.route('/predict', methods=['POST'])
def onlinePredictor():
    print(request.is_json)
    content = request.get_json()
    print(type(content))
    print(content)
    content[0]['Wage']
    predict = linreg_deserialized.predict(np.array([[content[0]['Wage']]]))
    print(predict)
    return jsonify(predict.tolist())
