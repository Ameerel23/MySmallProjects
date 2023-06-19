from sha import app, db
# from sha.models import Car, Specifications
from flask import Flask, render_template, url_for, request, redirect, flash

@app.route("/", methods=['GET', 'POST'])
def welcome():

    return render_template('welcome.html', title='Second Hand Autoshop')