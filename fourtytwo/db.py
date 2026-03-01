from flask import current_app

import click
from pathlib import Path
from functools import wraps

def get_db_path():
    """Return the path to the digits database in the instance folder."""
    return Path(current_app.config['DATABASE'])

def check_zero(pos, val):
    if pos == 0 and val == 0:
        raise ValueError("Leading digit cannot be zero")

def init_db():
    filepath = get_db_path()
    filepath.parent.mkdir(parents=True, exist_ok=True)  # ensure instance folder exists
    with open(filepath, 'w', encoding='utf8') as f:
        f.write('\n'.join(['1'] + ['0'] * 41))

@click.command('init-db')
def init_db_cmd():
    init_db()
    click.echo('Database initialised.')
    
def init_app(app):
    app.cli.add_command(init_db_cmd)
    
def clear_db():
    filepath = get_db_path()
    with open(filepath, 'w', encoding='utf8') as f:
        f.write('')

def get_digits():
    filepath = get_db_path()
    with open(filepath, 'r', encoding='utf8') as f:
        dig_list = f.read().strip().splitlines()
    dig_return = []
    for d in dig_list:
        try:
            dig_return.append(int(d))
        except ValueError:
            pass
    assert len(dig_return) == 42
    return dig_return
    
def get(pos): # pos is index0
    return get_digits()[pos]

def flip(pos, val):
    check_zero(pos, val)
    
    dig_list = get_digits()
    dig_list[pos] = int(val)
    
    filepath = get_db_path()
    with open(filepath, 'w', encoding='utf8') as f:
        f.write('\n'.join([str(d) for d in dig_list]))

def increment(pos):
    cur_dig = get(pos)
    if cur_dig == 9:
        new_dig = 0
    else:
        new_dig = cur_dig + 1
    flip(pos, new_dig)

def decrement(pos):
    cur_dig = get(pos)
    if cur_dig == 0:
        new_dig = 9
    else:
        new_dig = cur_dig - 1
    flip(pos, new_dig)
    