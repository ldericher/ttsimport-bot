import os

from dotenv import load_dotenv

from .ttsbot import TTSBot


def main() -> None:
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")

    bot = TTSBot()
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
