from quiz.questions import questions
from rich.console import Console
import subprocess
import time
import os

console = Console()


# Replace blank spaces and edit else and elif
def spacing(question):
    questions[question] = questions[question]\
        .replace('   ', '\n   ')\
        .replace(')else', ')\nelse')\
        .replace(')elif', ')\nelif')


# Invokes the spacing method and prints out the correct answer
def spacing_error(question):
    spacing(question)
    console.print(f'{questions[question]}')
    console.print('\n:pile_of_poo: Incorrect\n', style="bold red")
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
