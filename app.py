import logging
import typer

from pathlib import Path
from typing import Optional


logging.basicConfig(filename='./logs/app.log', level=logging.INFO, format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', filemode='a')

app = typer.Typer()



#@app.command()

if __name__ == '__main__':
    app()