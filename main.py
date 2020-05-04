from flask import Flask, render_template, request
from Die import Die
from random import randint

app = Flask(__name__)

global dice_roll
dice_roll = Die

@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Welcome to Roll the Bones!')

@app.route('/results', methods=['POST'])
def roll_die():
    global dice_roll

    sides = int(request.form['sides'])
    quantity = int(request.form['quantity'])
    title = 'Here are your results:'

    die = Die(sides)

    results = []
    for roll_num in range(quantity):
        result = die.roll()
        results.append(result)

    return render_template('results.html', the_title=title, the_sides=sides, the_quantity=quantity, the_results=results)
