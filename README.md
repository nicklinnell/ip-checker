# External IP Monitor and Notifier

This project is designed to monitor the external IP address of a system and
notify the user via Telegram if it changes. It's particularly useful for
applications that rely on a static IP address, such as APIs with IP
white listing. The script runs in a Docker container, making it easy to deploy
on any system that supports Docker.

## Features

- **IP Address Monitoring**: Continuously checks the external IP address of the host system.
- **Telegram Notifications**: Sends a message to a specified Telegram chat when the IP address changes.
- **Docker Integration**: Runs in a Docker container for easy setup and scalability.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker and Docker Compose installed on your system.
- A Telegram bot token and chat ID. You can create a bot and get a token from
  [BotFather](https://t.me/botfather) on Telegram.

## Setup

1.  **Clone the repository**:

    ```bash copy
    git clone git@github.com:nicklinnell/ip-checker.git
    cd ip-checker
    ```

1.  **Create a .env file (optional):**
    For added security, you can store your Telegram bot token and chat ID in an .env
    file at the root of the project directory. Add the following lines to your .env file:

    ```text copy
    TELEGRAM_BOT_TOKEN=your_bot_token_here
    TELEGRAM_CHAT_ID=your_chat_id_here
    ```

    Ensure to replace your_bot_token_here and your_chat_id_here with your actual
    Telegram bot token and chat ID.

1.  **Build and Run the Docker Container:**
    With the .env file in place, you can start the container with Docker Compose:
    ```bash copy
    docker-compose up -d
    ```
    This command builds the Docker image and starts the container in detached mode.

## Usage

Once the container is running, it will check the external IP address every 10
minutes. If a change is detected, it will automatically send a notification to
the specified Telegram chat.

## Checking Logs

To view the logs and confirm the script is running as expected, use:

```bash copy
docker compose logs -f ip-monitor
```

This command displays the container's log output, allowing you to monitor its
activity in real-time.

## Customization

This application allows for easy customization to fit your needs. You can
adjust the check interval and modify the notification message by editing
environment variables and the script.

### Adjusting the Check Interval

By default, the application checks the external IP address every 10 minutes. You
can adjust this interval by setting the `CHECK_INTERVAL` environment variable in
the `.env` file. This value should be set in seconds. For example, to check
every 5 minutes, you would add the following line to your `.env` file:

```text copy
CHECK_INTERVAL=300
```

After making changes to the .env file, remember to restart your Docker container
for the changes to take effect:

```bash copy
docker-compose down
docker-compose up -d
```

## Contributing

Contributions to this project are welcome. Please feel free to fork the
repository, make your changes, and submit a pull request.

## License

MIT License ([LICENSE](LICENSE) or <https://opensource.org/license/mit/>)

## Contact

If you have any questions or feedback, please contact me at nicklinnell@gmail.com
