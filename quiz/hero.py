""" Table hero heading """
from rich.console import Console
from rich.table import Table

console = Console()


def heading():
    ''' Title '''
    # console.print(
    #     '\n\n[u][i]============== PYTHONIC ==============[/i][/u]\n', style='bold cyan'
    # )

    # console.print('- Use double "quotes" unless otherwise\
    #             \n- When coding indent 3 spaces\
    #             \n- Type exit() to exit game\
    #             \n- Type restart() to restart game\
    #             \n- Type skip() to skip a question')

    table = Table(
        title=':snake: [bold][cyan]PYTHONIC[/][/] :snake:', width=100)

    table.add_column(
        'Pythonic interactive [bold][green]CLI[/][/] application for Python learners'
    )

    table.add_row('Use double "[bold][cyan]quotes[/][/]" unless otherwise')
    table.add_row('When coding indent [bold][cyan]3[/][/] spaces')
    table.add_row('Type [bold][magenta]exit[/][/]() to exit game')
    table.add_row('Type [bold][magenta]restart[/][/]() to restart game')
    table.add_row('Type [bold][magenta]skip[/][/]() to skip a question')
    console.print(table, justify='center')
