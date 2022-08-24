import os

import fftcgtool
from dotenv import load_dotenv

from .ttsbot import TTSBot


def main() -> None:
    load_dotenv()
    TOKEN = os.getenv("TTSBOT_TOKEN")

    fftcgtool.CardDB(
        "https://code.yavook.de/Yavook.de/fftcgtool-out/"
        "raw/branch/master/carddb.zip"
    )

    bot = TTSBot()
    bot.run(
        token=TOKEN,
        log_handler=None,
    )


if __name__ == "__main__":
    main()
