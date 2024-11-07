import json
import requests

from traticker import app
from traticker.models.setting import Setting


def send_discord_webhook(message):
    setting = Setting.query.first()
    if (
            not setting
            or not setting.discord_webhook_url
            or setting.discord_webhook_url.strip() == ""
    ):
        return

    webhook_url = setting.discord_webhook_url
    data = {"username": "traticker dev", "content": message}
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post(webhook_url, headers=headers, data=json.dumps(data))
    if response.status_code != 204:
        app.logger.error(f"Failed to send Discord webhook: {response.text}")
