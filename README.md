# Economics Hub Bot 📊

A Telegram bot that helps users understand economics, finance, markets, inflation, GDP, demand and supply, business trends, and global economic updates in a simple and professional way.

## Features

- 📈 Market updates
- 💰 Finance tips and advice
- 🌍 Global economic news
- 📊 GDP and inflation data
- 💼 Business trends
- Interactive keyboard buttons
- Natural language responses

## Commands

- `/start` - Welcome message and menu
- `/help` - Show all commands
- `/market` - Latest market updates
- `/inflation` - Current inflation data
- `/gdp` - GDP information
- `/economy` - Global economic news
- `/business` - Business trends
- `/finance` - Finance tips

## Deployment on Render

### Setup

1. Fork this repository to your GitHub account

2. Create a new bot on Telegram:
   - Message @BotFather on Telegram
   - Use `/newbot` command
   - Get your bot token

3. Deploy on Render:
   - Go to [render.com](https://render.com)
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository
   - Use these settings:
     - Name: economics-hub-bot (or your preferred name)
     - Environment: Python
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `python bot.py`
   
4. Add Environment Variables:
   - `BOT_TOKEN`: Your Telegram bot token

5. Click "Create Web Service"

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/economics-hub-bot.git
cd economics-hub-bot
