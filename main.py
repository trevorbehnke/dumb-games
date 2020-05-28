from flask import Flask, render_template, request
from Die import Die
from Sort import Sort
from Magic8 import Magic8ball
from Caesercypher import Cypher
from rps2 import RPS
from Cointoss import Coin
from Idiot import Idiot

import random

app = Flask(__name__)

global dice_roll
dice_roll = Die

global sortaword
sortaword = Sort

global magic8ball
magic8ball = Magic8ball

global cypher_maker
cypher_maker = Cypher

global rps_game
rps_game = RPS

global cointoss_game
cointoss_game = Coin

global idiot_game
idiot_game = Idiot

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

    return render_template('rollresults.html', the_title=title, the_results=results)


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

    return render_template('magic8ballresults.html', the_title=title, the_results=answer)


@app.route('/caesercypher')
def caesercypher_page():
    return render_template('caesercypher.html', the_title='Cryptography!')

@app.route('/caesercypherresults', methods=['POST'])
def caeser_cypher():
    global cypher_maker

    mode = str(request.form['mode'])
    key = int(request.form['key'])
    message = str(request.form['message'])
    title = 'Results:'

    cypher = Cypher(mode, key, message)

    results = cypher.encode()

    return render_template('caesercypherresults.html', the_title=title, the_results=results)


@app.route('/rps')
def rps_page():
    return render_template('rps.html', the_title='Rock, Paper, Scissors!')

@app.route('/rpsresults', methods=['POST'])
def rps():
    global rps_game

    mychoice = str(request.form['mychoice'])
    title = 'Results:'

    results = RPS(mychoice)
    results = results.round()

    return render_template('rpsresults.html', the_title=title, the_results=results)


@app.route('/cointoss')
def cointoss_page():
    return render_template('cointoss.html', the_title='Coin Toss!')

@app.route('/cointossresults', methods=['POST'])
def toss_coin():
    global cointoss_game

    quantity = int(request.form['quantity'])
    title = 'Results:'

    coin = Coin()

    results = []
    for x in range(quantity):
        result = coin.toss()
        results.append(result)

    return render_template('rollresults.html', the_title=title, the_results=results)


@app.route('/idiot')
def idiot_page():
    return render_template('idiot.html', the_title='Idiot!')

@app.route('/idiot', methods=['POST'])
@app.route('/idiotsuccess', methods=['POST'])
def run_idiot():
    global idiot_game

    response = str(request.form['question'])
    title = 'Idiot!'

    results = 'Ok, have a great day!'

    while True:
        if response == 'no':
            break
        else:
            return render_template('idiot.html', the_title=title, the_results=results)

    return render_template('idiotsuccess.html', the_results=results)