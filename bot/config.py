import os
import yaml
import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load .env config
config_env = dotenv.dotenv_values(config_dir / "config.env")

# config parameters
telegram_token = os.environ.get("TELEGRAM_TOKEN")
openai_api_key = os.environ.get("OPENAI_API_KEY")
use_chatgpt_api = os.environ.get("USE_CHATGPT_API", True)
allowed_telegram_usernames = os.environ.get("ALLOWED_TELEGRAM_USERNAMES", "").split(",")
new_dialog_timeout = os.environ.get("NEW_DIALOG_TIMEOUT", 600)
enable_message_streaming = os.environ.get("ENABLE_MESSAGE_STREAMING", True)
mongodb_uri = os.environ.get("MONGODB_URI")

# chat_modes
with open(config_dir / "chat_modes.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)
