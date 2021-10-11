""" Pythonic Functions """
import os
import subprocess
import sys
import time
from rich.console import Console
from rich.syntax import Syntax
from rich.table import Table
from quiz.questions import questions

console = Console()


def write_file(table):
    ''' Write incorrect answers to a txt file '''
    with open('pythonic.txt', 'a', encoding='utf-8') as file:
        file.write(table)


def spacing(question):
    ''' Replace blank spaces and edit else and elif '''
    questions[question] = questions[question]\
        .replace('   ', '\n   ')\
        .replace(')else', ')\nelse')\
        .replace(')elif', ')\nelif')


def spacing_error(question):
    ''' Invokes the spacing method and prints out the correct answer '''
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
    subprocess.run(['say', 'Incorrect'], check=True)
    time.sleep(2)
    os.system('cls||clear')


def correct():
    ''' Prompts user is correct '''
    console.print('\n:thumbs_up: Correct\n', style="bold green")
    subprocess.run(['say', 'Correct!'], check=True)
    time.sleep(2)
    os.system('cls||clear')


def good_bye():
    ''' Prompt Goodbye! and exit game '''
    os.system('cls||clear')
    console.print('Goodbye!\n', style='Bold cyan')
    subprocess.run(['say', 'Goodbye!'], check=True)
    sys.exit()
