from quiz.questions import questions
from quiz.prompts import spacing_error, correct, good_bye
from rich.console import Console
import subprocess
import os

console = Console()


def play_game():
    # Title:
    console.print(
        '\n\n[u][i]============== PYTHONIC ==============[/i][/u]\n', style='bold cyan')

    console.print('- Use double "qoutes" unless otherwise\
                \n- When coding indent 3 spaces\
                \n- Type exit() to exit game\
                \n- Type restart() to restart game\
                \n- Type skip() to skip a question')

    subprocess.run(['say', 'Welcome to Pythonic!'])

    # Global variables
    score = 0
    returned_output = []
    empty_spaces = []

    # Loop thru questions and get questions and answers
    for question in questions.keys():
        console.print(f'\nTotal score: [u]{score}[/u]\n', style='Bold cyan')
        console.print(f'{question}\n')
        # Toggle audio
        subprocess.run(['say', question[2:]])  # read question

        while True:
            user_input = input('')
            # print(user_input, len(user_input), empty_spaces)

            # restart() game;
            if user_input == 'restart()':

                restart_game = input(
                    'Are you sure you want to restart the game y/n: '
                )

                if restart_game == 'y':
                    console.print('Restarting Game!\n', style='Bold cyan')
                    subprocess.run(['say', 'Restarting Game!'])
                    os.system('cls||clear')
                    play_game()
                elif restart_game == 'n':
                    console.print('Lets Continue!\n', style='Bold cyan')
                    subprocess.run(['say', 'Lets Continue!'])
                    os.system('cls||clear')
                    break
                else:
                    break

            # exit() game:
            elif user_input == 'exit()':
                good_bye()

            # skip() question:
            elif user_input == 'skip()':
                console.print('skipped!\n', style='Bold cyan')
                subprocess.run(['say', 'skipped!'])
                os.system('cls||clear')
                break

            # User input: if user input is equal to answer and not already in returned output
            elif user_input in questions[question] and user_input not in returned_output:
                # append user answer to returned output
                returned_output.append(user_input)

                # if returned output as a string is equal to answer
                if ''.join(returned_output) == questions[question]:
                    returned_output = []  # reset returned out
                    score += 1  # add +1 to score
                    correct()
                    break

            # if user input not a answer
            elif user_input not in questions[question]:
                spacing_error(question)
                break

            # if user returns an empty string or the lenght of that string is 0
            elif user_input == '' and len(user_input) == 0:
                # append empty string to empty_spaces
                empty_spaces.append(user_input)

                # if empty_spaces is [''] or empty_spaces is equal 0 or greater
                if empty_spaces == [''] or len(empty_spaces) >= 0:
                    empty_spaces = []  # reset empty_spaces
                    spacing_error(question)
                    break

    # print final score
    console.print(
        f'\nThank you for playing Pythonic! Your total score is: [u]{score}[/u]\n', style='Bold cyan'
    )

    # Thanks user for playing
    subprocess.run([
        'say', f'Thank you for playing Pythonic! Your total score is {score}'
    ])


# Invoke game
play_game()


# Replay game
user_input = input('Do you want to play again y/n: ')

if user_input == 'y':
    os.system('cls||clear')
    play_game()
elif user_input == 'n':
    good_bye()
else:
    console.print(f'\nCome again. Thank you!\n', style='Bold cyan')
    exit()
