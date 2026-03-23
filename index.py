from flask import Flask, render_template, request, redirect
import pickle

app = Flask(__name__, template_folder="../")

# Load models
credit_model = pickle.load(open("creditcard_model.pkl", "rb"))
scam_model   = pickle.load(open("scam_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("alerts.html")

# your other Flask routes here…

# Vercel serverless handler
def handler(request):
    return app(request)
