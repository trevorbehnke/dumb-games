from flask import Flask, render_template, request
from Die import Die
from Sort import Sort
from Magic8 import Magic8ball, response
import random

app = Flask(__name__)

global dice_roll
dice_roll = Die

global sortaword
sortaword = Sort

global magic8ball
magic8ball = Magic8ball

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', the_title='Welcome to DumbGamez!')

@app.route('/rollthebones')
def rollthebones_page():
    return render_template('rollthebones.html', the_title='Roll the Dice!')

@app.route('/rollresults', methods=['POST'])
def roll_die():
    global dice_roll

    sides = int(request.form['sides'])
    quantity = int(request.form['quantity'])
    title = 'Results:'

    die = Die(sides)

    results = []
    for roll_num in range(quantity):
        result = die.roll()
        results.append(result)

    return render_template('rollresults.html', the_title=title, the_sides=sides, the_quantity=quantity, the_results=results)

@app.route('/sortaword')
def sortaword_page():
    return render_template('sortaword.html', the_title='Sort a Word!')

@app.route('/sortawordresults', methods=['POST'])
def word_sort():
    global sortaword

    x_word = str(request.form['x_word'])
    title = 'Results:'

    my_word = Sort(x_word)

    sorted_word = my_word.sort_word()

    return render_template('sortawordresults.html', the_title=title, the_results=sorted_word)

@app.route('/magic8ball')
def magic8_page():
    return render_template('magic8ball.html', the_title='Magic 8 Ball!')

@app.route('/magic8ballresults', methods=['POST'])
def magic_8():
    global magic8ball

    question = str(request.form['question'])
    title = 'Answer: '

    question = Magic8ball(question)
    
    answer = question.ask()
    # for x in response:
    #     return random.choice(response)

    return render_template('magic8ballresults.html', the_title=title, the_results=answer)