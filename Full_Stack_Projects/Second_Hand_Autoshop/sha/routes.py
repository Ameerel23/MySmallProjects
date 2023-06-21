from sha import app, db
from sha.models import Car, Specifications
from flask import Flask, render_template, url_for, request, redirect, flash

@app.route("/", methods=['GET', 'POST'])
def welcome():

    return render_template('welcome.html', title='Second Hand Autoshop')

@app.route("/carpage", methods=['GET', 'POST'])
def carpage():

    return render_template('carpage.html', title='Second Hand Autoshop Cars for Sale')

@app.route("/ordering", methods=['GET', 'POST'])
def ordering():

    return render_template('ordering.html', title='Your Car Order')

@app.route("/about", methods=['GET', 'POST'])
def about():

    return render_template('about.html', title='About Second Hand Autoshop')

