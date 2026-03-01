from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from . import db

bp = Blueprint('fourtytwo', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    context = {
        'digits': db.get_digits()
    }
    
    return render_template('index.html', **context)

@bp.route('/update', methods=['POST'])
def update():
    pos = int(request.form['pos'])
    action = request.form['action'].strip()
    
    try:
        if action == '+':
            db.increment(pos)
        elif action == '-':
            db.decrement(pos)
    except ValueError:
        flash('You can\'t make it a 41-digit number!', 'error')
    
    return redirect(url_for('fourtytwo.index'))