from flask import (Blueprint, render_template)

import json

pets = json.load(open('pets.json'))


bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)

@bp.route('/<int:id>')   

def show(id):
    pet = pets[id-1]
    print(pet)
    return render_template('pets/show.html', pet=pet)


@bp.route('/facts')
def facts():
    return render_template('facts/facts.html')

@bp.route('/new')
def new():
    return render_template('facts/new_facts.html')



