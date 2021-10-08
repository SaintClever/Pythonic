""" Pythonic Functions """
import os
import subprocess
import time
from quiz.questions import questions
from rich.console import Console
from rich.syntax import Syntax
from rich.table import Table


console = Console()


# Write incorrect answers to a txt file
def write_file(table):
    with open('pythonic.txt', 'a') as file:
        file.write(table)


# Replace blank spaces and edit else and elif
def spacing(question):
    questions[question] = questions[question]\
        .replace('   ', '\n   ')\
        .replace(')else', ')\nelse')\
        .replace(')elif', ')\nelif')


# Invokes the spacing method and prints out the correct answer
def spacing_error(question):
    spacing(question)  # adjust the spacing
    # console.print(f'{questions[question]}')
    write_file(f'{question}\n{questions[question]}\n\n\n')  # invoke write_file

    # print error
    console.print('\n:pile_of_poo: Incorrect\n', style="bold red")

    # Create syntax view
    syntax = Syntax(
        questions[question],
        'python',
        theme='monokai')

    # Create a table
    table = Table('correct answer', width=50)
    table.add_row(syntax)
    console.print(table)

    # Speak, wait and clear error
    subprocess.run(['say', 'Incorrect'])
    time.sleep(2)
    os.system('cls||clear')


# Prompts user is correct
def correct():
    console.print('\n:thumbs_up: Correct\n', style="bold green")
    subprocess.run(['say', 'Correct!'])
    time.sleep(2)
    os.system('cls||clear')


# Prompt Goodbye! and exit game
def good_bye():
    os.system('cls||clear')
    console.print('Goodbye!\n', style='Bold cyan')
    subprocess.run(['say', 'Goodbye!'])
    exit()
