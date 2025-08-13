import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

flask_app=Flask(__name__)
model=pickle.load(open('model.pkl', 'rb'))

@flask_app.route('/')
def home():
    return render_template('index.html')
@flask_app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array)
    return render_template('index.html', prediction_text='Recommended Crop is {}'.format(prediction[0]))

if __name__=='__main__':
    flask_app.run(debug=True)