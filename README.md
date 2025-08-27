Crop Prediction Web Application
Overview
This project is a machine learning-powered web application that predicts the most suitable crop to grow based on soil and environmental parameters. It is designed to assist farmers and agricultural professionals in making data-driven decisions for crop selection.

Features
User-friendly web interface for inputting soil and climate data.
Real-time crop recommendation using a trained machine learning model.
Built with Python, Flask, scikit-learn, HTML, CSS, and Bootstrap.
Model trained on real agricultural data.

Field-forecast/
│
├── app.py                  # Flask web application
├── model.py                # Model training script
├── model.pkl               # Trained ML model (pickle)
├── model_columns.pkl       # Model feature columns (pickle)
├── requirements.txt        # Python dependencies
├── static/
│   ├── Crop_recommendation.csv  # Dataset
│   ├── farm.jpg                # Image asset
│   └── style.css               # Custom styles
├── templates/
│   ├── farm.jpg                # (Possibly unused duplicate image)
│   └── index.html              # Main HTML template

How It Works
1. Model Training:
The model.py script loads the dataset, preprocesses the data, trains a Random Forest classifier, and saves the trained model and feature columns using pickle.
2. Web Application:
The app.py file loads the trained model and serves a web interface using Flask.
Users enter soil and climate parameters in the form.
The app predicts and displays the recommended crop.

Setup & Usage
1. Clone the repository and navigate to the project folder:
cd Field-forecast

2. Create and activate a virtual environment (optional but recommended):
python -m venv venv
venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. (Optional) Retrain the model:
python model.py

5. Run the Flask app:
python app.py

6. Open your browser and go to:
http://127.0.0.1:5000/

7. Dependencies
Flask
scikit-learn
pandas
numpy
Jinja2
Bootstrap (via CDN in HTML)
