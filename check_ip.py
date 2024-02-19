import requests
import os
import time

def get_external_ip():
    response = requests.get('https://api.ipify.org')
    return response.text

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
    }
    response = requests.post(url, data=data)
    print(f"Sending message to Telegram: {message}")
    return response.json()

def check_and_update_ip():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    ip_file = "last_ip.txt"
    current_ip = get_external_ip()

    print(f"Current external IP is: {current_ip}")

    try:
        with open(ip_file, "r") as file:
            last_ip = file.read().strip()
            print(f"Last known IP was: {last_ip}")
    except FileNotFoundError:
        last_ip = None
        print("No last_ip.txt file found. Treating as first run.")

    if current_ip != last_ip:
        message = f"IP Address changed to: {current_ip}"
        send_telegram_message(token, chat_id, message)
        with open(ip_file, "w") as file:
            file.write(current_ip)
            print("Updated last_ip.txt with new IP address.")
    else:
        print("No change in IP address detected.")

def main():
    sleep_time = int(os.getenv("CHECK_INTERVAL", "600"))
    while True:
        check_and_update_ip()
        # Wait for 600 seconds (10 minutes) before checking again
        print(f"Waiting for {sleep_time // 60} minutes before next check...")
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()

