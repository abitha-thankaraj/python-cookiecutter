help = """
Your project has been created!
_____________________________________________________________________________
                            ___________ _
  \\/                    __/   .::::.-'-(/-/)
                     _/:  .::::.-' .-'\\/\\_`*******            __ (_))
        \\/          /:  .::::./   -._-.  d\\|                 (_))_(__))
                     /: ("'"'/    '.  (__/||             (_))__(_))--(__))
                      \\::).-'  -._  \\/ \\/\\|
              __ _ .-'`)/  '-'. . '. |  (i_O
          .-'      \\       -'      '\\|
     _ _./      .-'|       '.  (    \\                           % % %
  .-'   :      '_  \\         '-'\\  /|/      @ @ @               % % % %
 /      )\\_      '- )_________.-|_/^\\      @ @ @@@             % %\\/% %
 (   .-'   )-._-:  /        \\(/\'-._ `.     @|@@@@@              ..|........
  (   )  _//_/|:  /          `\\()   `\\_\\     |/_@@               )'-._.-._.-
   ( (   \\()^_/)_/             )/      \\    /                  /   /
    )  _.-\\.\\(_)__._.-'-.-'-.//_.-'-.-.)\\-'/._                /
.-.-.-'   _o\\ \\\\     '::'   (o_ '-.-' |__\'-.-;~ ~ ~ ~ ~ ~ ~~/   /\\
          \\ /  \\\\__          )_\\    .:::::::.-'\\            '- - -|
     :::''':::::^)__\\:::::::::::::::::'''''''-.  \\                  '- - - -
    :::::::  '''''''''''   ''''''''''''':::. -'\\  \\       C. SWANSIGER
_____':::::_____________________________________\\__\\_________________________

Set up the project's uv-managed environment with:

cd {{cookiecutter.repo_name}}
uv sync

This creates a local virtual environment in `.venv` and installs the project.
Run commands in that environment with:

uv run python

Add dependencies with:

uv add <package>

You will need to manually add data to .gitignore to prevent it from syncing to
version control.

Don't forget to sync to GitHub. Have fun!
"""
print(help)
