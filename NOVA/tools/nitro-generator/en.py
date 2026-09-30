import random
import string
import json
import os
import requests
from colorama import Fore, init


init(autoreset=True)

LANGUAGE = os.environ.get("NOVA_LANGUAGE", "en")
TEXT = {
    "vi": {
        "invalid_webhook": "Webhook không hợp lệ",
        "verify_error": "Lỗi khi xác minh webhook: {error}",
        "send_error": "Lỗi khi gửi webhook: {error}",
        "valid_nitro": "Nitro hợp lệ!",
        "valid": "Hợp lệ",
        "invalid": "Không hợp lệ",
        "timeout": "Yêu cầu đã hết thời gian chờ",
        "verify_nitro_error": "Lỗi khi xác minh mã Nitro: {error}",
        "use_webhook": "Sử dụng Webhook? (y/n) -> ",
        "webhook_url": "URL Webhook -> ",
        "how_many": "Bạn muốn tạo bao nhiêu mã Nitro? -> ",
    },
    "zh": {
        "invalid_webhook": "Webhook 无效",
        "verify_error": "验证 webhook 时出错：{error}",
        "send_error": "发送 webhook 时出错：{error}",
        "valid_nitro": "Nitro 有效！",
        "valid": "有效",
        "invalid": "无效",
        "timeout": "请求超时",
        "verify_nitro_error": "验证 Nitro 代码时出错：{error}",
        "use_webhook": "使用 Webhook？(y/n) -> ",
        "webhook_url": "Webhook URL -> ",
        "how_many": "要生成多少个 Nitro 代码？-> ",
    },
}
DEFAULT_TEXT = {
    "invalid_webhook": "Invalid Webhook URL",
    "verify_error": "Error verifying webhook: {error}",
    "send_error": "Error sending to webhook: {error}",
    "valid_nitro": "Valid Nitro!",
    "valid": "Valid",
    "invalid": "Invalid",
    "timeout": "Request timeout expired",
    "verify_nitro_error": "Error verifying Nitro code: {error}",
    "use_webhook": "Use a Webhook? (y/n) -> ",
    "webhook_url": "Webhook URL -> ",
    "how_many": "How many Nitro codes do you want to generate? -> ",
}

def text(key, **values):
    return TEXT.get(LANGUAGE, {}).get(key, DEFAULT_TEXT[key]).format(**values)

def error_message(error):
    """Display an error message."""
    print(Fore.RED + f"Error: {error}")

def verify_webhook(url):
    """Verify if the webhook is valid and send a test message."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            payload = {
                'content': """# NOVA-Nitro-Gen

                
                
> __**Your webhook is awork you can start generating nitro!**__

> __NOVA community <3__

||@everyone||"""
            }
            headers = {
                'Content-Type': 'application/json'
            }
            requests.post(url, data=json.dumps(payload), headers=headers)
            return True
        else:
            error_message(text("invalid_webhook"))
            return False
    except requests.exceptions.RequestException as e:
        error_message(text("verify_error", error=e))
        return False

def send_webhook(embed_content, webhook_url, webhook_username, webhook_avatar):
    """Send a notification to the webhook."""
    payload = {
        'embeds': [embed_content],
        'username': webhook_username,
        'avatar_url': webhook_avatar
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    except requests.exceptions.RequestException as e:
        error_message(text("send_error", error=e))

def verify_nitro_code(webhook, webhook_url, webhook_username, webhook_avatar, webhook_color):
    """Verify if a Discord Nitro code is valid."""
    code_nitro = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
    url_nitro = f'https://discord.gift/{code_nitro}'
    try:
        response = requests.get(f'https://discord.com/api/v9/entitlements/gift-codes/{code_nitro}?with_application=false&with_subscription_plan=true', timeout=5)
        if response.status_code == 200:
            embed_content = {
                'title': text("valid_nitro"),
                'description': f"**__Nitro:__**\n```{url_nitro}```",
                'color': webhook_color,
                'footer': {
                    "text": webhook_username,
                    "icon_url": webhook_avatar,
                }
            }
            if webhook:
                send_webhook(embed_content, webhook_url, webhook_username, webhook_avatar)
            print(Fore.GREEN + f"[+] {text('valid')} | Nitro: {url_nitro}")
        else:
            print(Fore.RED + f"[-] {text('invalid')} | Nitro: {url_nitro}")
    except requests.exceptions.ReadTimeout:
        error_message(text("timeout"))
    except requests.exceptions.RequestException as e:
        error_message(text("verify_nitro_error", error=e))

def generate_nitros(num_nitros, webhook, webhook_url, webhook_username, webhook_avatar, webhook_color):
    """Generate and verify the specified number of Nitro codes."""
    for _ in range(num_nitros):
        verify_nitro_code(webhook, webhook_url, webhook_username, webhook_avatar, webhook_color)

def main():
    try:
        use_webhook = input(Fore.RED + "[?] " + text("use_webhook")).strip().lower() in ['y', 'yes']
        if use_webhook:
            webhook_url = input(Fore.RED + "[?] " + text("webhook_url")).strip()
            if not verify_webhook(webhook_url):
                return
            webhook_username = "Nitro Generator"
            webhook_avatar = "https://example.com/avatar.png"
            webhook_color = 0x00ff00
        else:
            webhook_url = webhook_username = webhook_avatar = webhook_color = None

        num_nitros = int(input(Fore.RED + "[?] " + text("how_many")).strip())

    except Exception as e:
        error_message(e)
        return

    try:
        generate_nitros(num_nitros, use_webhook, webhook_url, webhook_username, webhook_avatar, webhook_color)
    except Exception as e:
        error_message(e)

if __name__ == "__main__":
    main()

