# ChatGPT Telegram Bot

<br>

This repository is a Telegram Bot re-creation of ChatGPT, and it was forked from [m1guelpf/chatgpt-telegram](https://github.com/m1guelpf/chatgpt-telegram). The main difference between this version and the original is that this repository removes the Docker-compose and focuses only on creating a Dockerfile that contains the bot. This makes it easier to host the bot on external services such as [Railway](https://railway.app/) by creating a new app from this repository and adding a MongoDB database. All configurations can be set as environmental variables from the Railway website, and no changes are required in the code.

## Bot commands
- `/retry` – Regenerate last bot answer
- `/new` – Start new dialog
- `/mode` – Select chat mode
- `/balance` – Show balance
- `/settings` – Show settings
- `/help` – Show help

## Setup
1. Get your [OpenAI API](https://openai.com/api/) key

2. Get your Telegram bot token from [@BotFather](https://t.me/BotFather)

3. Modify the [config/chat_modes.yml](https://github.com/altndrr/chatpgt-telegram/blob/main/config/chat_modes.yml) with your on ChatGPT modes.

4. Create the external MongoDB dataset on i.e. Railway and get its URL.

5. Build the Docker image:
    ```bash
    docker build --target chatgpt-telegram:devel .
    ```

6. Start the container while passing the env variables.
    ```bash
    docker run --rm -it chatgpt-telegram:devel \
      -e TELEGRAM_TOKEN={YOUR TOKEN} \
      -e OPENAI_API_KEY={YOUR KEY} \
      -e MONGODB_URI={YOUR URI} \
      -e ALLOWED_TELEGRAM_USERNAMES={YOUR TELEGRAM USERNAME+OTHERS}
    ```

## References
1. [*Build ChatGPT from GPT-3*](https://learnprompting.org/docs/applied_prompting/build_chatgpt)
2. [ChatGPT Telegram (original repository)](https://github.com/m1guelpf/chatgpt-telegram)
