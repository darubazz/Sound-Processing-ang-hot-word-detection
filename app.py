import logging
import typer
import wave

from pathlib import Path
from typing import Optional

logging.basicConfig(filename='./logs/app.log', level=logging.INFO, format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', filemode='a')

app = typer.Typer()


# @app.command()
# def train(dataset: Optional[Path] = Path("../data/dataset/train/")):


@app.command()
def hot_word_detection(wav_path: Optional[Path]):
    with wave.open(wav_path, "r") as f:
        wav = wave.open(wav_path)

    hwd = obj_of_class.func_of_class(wav)

    # saving results
    save_path = Path("./data/result.txt")
    with open(save_path, "w") as f:
        f.writelines(hwd)

    logging.info(f"Keyword detection time saved in {save_path} successfully!")


if __name__ == '__main__':
    app()
