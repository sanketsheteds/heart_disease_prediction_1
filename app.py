from flask import Flask, request, jsonify, render_template
from utils import HeartPrediction
import config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        data = request.args
    elif request.method == 'POST':
        data = request.form
    else:
        return jsonify({"message": "Unsuccessful"})

    pred_obj = HeartPrediction()
    predict_disease = pred_obj.predict_result(data)

    # return jsonify({"result": predict_disease})
    return render_template('index.html', result=predict_disease)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)
