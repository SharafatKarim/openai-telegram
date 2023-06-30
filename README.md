# OpenAI Telegram Bot

A minimal, lightweight and simple telegram bot built with chatgpt API from [OpenAI](https://openai.com/) and [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot). It can genrate text messages and images and can be used both personally or inside a group!

**API used**
- OpenAI GPT-3.5 for chat response
- DALL-E for image response

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


![openai-telegram](https://socialify.git.ci/SharafatKarim/openai-telegram/image?description=1&forks=1&issues=1&language=1&name=1&pulls=1&stargazers=1&theme=Light)

> This project is also available with Telegraf library in Node.js (both servered or, serverless).
> - [openai-telegram-bot](https://github.com/sr-tamim/openai-telegram-bot/)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

- `API_KEY`  

> collect from your openai account. From the setting you can generate API key. 

- `BOT_API`

> Telegram `BOT_API` can be generated from Bot [father telegram bot](https://t.me/BotFather).

## Run Locally

Clone the project

```bash
  git clone https://github.com/SharafatKarim/openai-telegram
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install -r requirements.txt 
```

Run the bot

```bash
  python main.py
```


## Deployment


This bot can deployed to web services like railway or heroku or any vps. For vps follow the above guide. Railway should work out of the box. Just fork this repository, fill up environment variables. As simple as that!

## Screenshots
![image](https://user-images.githubusercontent.com/93897936/236427776-4a7f9333-3808-43c6-b2cc-25f421c01f98.png)

![image](https://user-images.githubusercontent.com/93897936/236427105-698b18ab-7071-4060-ba1c-2459951203d4.png)

## Authors

[![sr-tamim's Profilator](https://profilator.deno.dev/sr-tamim?v=1.0.0.alpha.4)](https://github.com/sr-tamim)
[![SharafatKarim's Profilator](https://profilator.deno.dev/SharafatKarim?v=1.0.0.alpha.4)](https://github.com/SharafatKarim)

## Contribution

Feel free to fork and open pull requests. Also you are very welcomes to apply new pathes or create a more advanced version of this project. Your imagination is your limits!
