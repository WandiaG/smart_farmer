from flask import render_template, url_for, flash, redirect, jsonify, request
from flaskblog import app
from flaskblog.models import Customer
from flaskblog.forms import SearchForm


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/SERVICES")
def services():
    return render_template("services.html")


@app.route("/ADMIN")
def admin():
    return render_template("admin.html")


@app.route("/CONTROL")
def control():
    return render_template("control.html")

@app.route("/CUSTOMER")
def customer():
    return render_template("customer.html")

@app.route("/ADMINDASH")
def admindash():
    return render_template("admindash.html")

@app.route("/CONTROLDASH")
def controldash():
    return render_template("controldash.html")

@app.route('/search_customer', methods=['POST'])
def search_customer():
    form = SearchForm()
    customer = None
    member_code = form.member_code.data
    customer = Customer.query.filter_by(member_code=member_code).first()
  
    return render_template("controldash.html", title='Search Customer', form=form, customer=customer)
