# TTSImport Bot

This provides `fftcgtool` capabilities as a Discord Bot.

## Usage

Just run the `main` submodule as a script:

```bash
python -m ttsimport-bot.main
```

## Configuration

Runtime configuration of the bot is done using environment variables.

- `TTSBOT_TOKEN` – Bot token as per [Discord Developer Portal](https://discord.com/developers/applications). This can be set using an `.env` file as well.
- `TTSBOT_MAX_DECKS` – Maximum amount of decks to import per request. Defaults to 10.

## Installation

You can install `ttsimport` if you have at least python version `3.9` with `pip` installed. To test,
run `python --version` or similar.

- Install from this repository: Use `pip install "git+https://github.com/ldericher/ttsimport/bot"`.
- Or from your local source: Clone this repository and run `pip install /path/to/ttsimport`.
