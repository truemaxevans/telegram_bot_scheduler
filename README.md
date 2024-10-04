# TELEGRAM BOT API

**Author:** [TrueMaxEvans](https://github.com/truemaxevans)  
**Version:** 1.0.0

## Overview

This API allows you to interact with Telegram Bot features effectively.

## Getting Started

To successfully integrate this API with Telegram, you need to know the `chat_id` of the chat where you would like to interact.

## Obtaining the Chat ID

1. Add the bot [@getidsbot](https://t.me/getidsbot) as an admin to your chat.
2. After doing so, copy the `chat_id` from the response.
3. Save it to your environment file as `CHANNEL_ID`.

## Environment Variables

Don't forget to include the following variables in your environment file:

- `BOT_TOKEN`: Your Telegram Bot token.
- `TELEGRAM_URL`: The URL for the message that the bot will send to the chat or channel.

## Usage

Make sure to follow the provided instructions to set up the bot and start sending messages to your desired chat.


## Deployment

Deployment to the server may require additional setup depending on the server requirements. Ensure that all dependencies are installed and that the server is configured to run the bot properly.

### On server you should run -> main.py