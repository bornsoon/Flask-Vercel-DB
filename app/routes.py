from flask import render_template, request, redirect, url_for, flash
from app import app
from app.models import Subscription

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    flash('Subscription successful!!', 'success')
    return redirect(url_for('index'))