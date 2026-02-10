
# 🤖 AI Trend Bot: Sarcasm on Demand

Posts daily creative and sarcastic updates based on the hottest trending topics fetched from the Mastodon network. Built with Python and OpenAI.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)  
[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)  
[![Built with](https://img.shields.io/badge/Built%20with-GPT--3.5--Turbo-brightgreen)](https://openai.com/)

## ✨ Features

* **Daily Post Limiting:** Uses Mastodon's API to check if a post has been made today, preventing spam.
* **Trend Fetching:** Pulls the top trending hashtags for timely content.
* **Creative Generation:** Utilizes the OpenAI API to craft posts in a **sarcastic or creative tone**.
* **Easy Setup:** One-command script for environment configuration.

## 🚀 Quick Start (Setup)

Getting the bot running is quick! You'll need Python 3.11+ and an API key from both **OpenAI** and your chosen **Mastodon instance**.

1. **Clone the Repository**

    ```bash
    git clone https://github.com/IlkinAlishov/Mastodon-Social-Bot/
    cd ai-trend-bot
    ```

2. **Initialize Environment & Install Dependencies**

    This script creates the virtual environment (`.venv`), activates it, and installs everything listed in `requirements.txt`.

    ```bash
    ./scripts/setup_env.sh
    ```

3. **Configure Secrets**

    Copy the example file and edit it to include your actual API tokens and base URL.

    ```bash
    cp .env.example .env
    # Now, open .env in your editor and fill in the values!
    ```

## 🏃 Running the Bot

### Manual Execution

Run the bot once to test the full pipeline. If a post has already been made today, the bot will exit gracefully.

```bash
./scripts/run_bot.sh
````

### Automation (Scheduling)

For automatic daily posting, we recommend using a scheduler like `cron` on a dedicated server or VPS. Set the job to run once per day (e.g., at 9:00 AM server time).

```bash
# Add this line to your crontab (-e)
0 9 * * * cd /path/to/ai-trend-bot && ./scripts/run_bot.sh > /dev/null 2>&1
```

## 🛠️ Project Structure

The project follows a standard Python package layout, making it easy to test and maintain.

```
ai-trend-bot/
├── data/
│   └── raw/
├── src/
│   └── ai_trend_bot/
│       ├── config.py             # Loads secrets & defines the POST_PROMPT template.
│       ├── mastodon_client.py    # Mastodon API connection and posting/rate-limiting logic.
│       ├── trend_fetch.py        # Fetches trending hashtags.
│       ├── post_generator.py     # Interfaces with OpenAI to generate text.
│       └── pipeline.py           # The main entry point (runs the logic).
├── scripts/
│   ├── setup_env.sh             # Installs deps & creates venv.
│   └── run_bot.sh               # Activates venv and executes the pipeline.
├── tests/
└── requirements.txt
```

## 🧪 Testing

We use `pytest` for unit testing the API client mocking. Ensure your virtual environment is active and the `PYTHONPATH` is set correctly (or use the simple execution method below).

```bash
PYTHONPATH=src pytest tests/
```

## ✍️ Contribution

If you have ideas for new features, better prompts, or cleaner code, feel free to submit a **Pull Request** or open an **Issue**!

---
