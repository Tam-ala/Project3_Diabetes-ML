from joblib import load
import json
from flask import Flask, jsonify, render_template, url_for


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################


#################################################
# HTML ROUTES

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/treatment")
def profile():
    return render_template("treatment.html")

@app.route("/test.html")
def charts():
    return render_template("test.html")
    
# @app.route("/test", methods=["POST", "GET"])
# def simpleTest():
#     # read data, do for each question, make sure the features are in correct order
#     age1 = request.form['age1']
#     height1 = request.form['height1']
#     weight1 = request.form['weight1']

#     # make sure that height is not 0
#     if height >= 0:
#         bmi = (703 * weight1)/(height1^2)
#     else
#         break
    
#     # user input list
#     features = [age1, bmi]
    
#     # load model
#     model = load("diabetes_model.joblib")
#     prediction = model.predict(features)
#     # result is a 1 or 0 

#     if prediction == 1:
#         # print  
#     else 
#         # print in html

#     return render_template ("prediction.html", prediction)

# @app.route("/test", methods=["POST", "GET"])
# def Test():
#     # read data, do for each question, make sure the features are in correct order
#     age1 = request.form['age1']
#     height1 = request.form['height1']
#     weight1 = request.form['weight1']

#     # make sure that height is not 0
#     if height >= 0:
#         bmi = (703 * weight1)/(height1^2)
#     else
#         break
    
#     # user input list
#     features = [age1, bmi]
    
#     # load model
#     model = load("diabetes_model.joblib")
#     prediction = model.predict(features)
#     # result is a 1 or 0 

#     if prediction == 1:
#         # print  
#     else 
#         # print in html

#     return render_template ("prediction.html", prediction)

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")




