import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token from environment variable
TOKEN = os.environ.get('BOT_TOKEN')

# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when /start is issued."""
    user = update.effective_user
    welcome_message = f"""
📊 *Welcome to Economics Hub Bot, {user.first_name}!*

I help you understand economics, finance, markets, inflation, GDP, demand and supply, business trends, and global economic updates in a simple and professional way.

🔍 *What I can do:*
• Explain economic concepts simply
• Provide market updates
• Answer finance questions
• Share global economic news
• Help with business trends

Use /help to see all available commands.
"""
    keyboard = [
        [InlineKeyboardButton("📈 Market Updates", callback_data='markets')],
        [InlineKeyboardButton("💰 Finance Tips", callback_data='finance')],
        [InlineKeyboardButton("🌍 Global Economy", callback_data='global')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        welcome_message,
        parse_mode='Markdown',
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a help message when /help is issued."""
    help_text = """
📚 *Available Commands:*

/start - Welcome message and menu
/help - Show this help message
/market - Latest market updates
/inflation - Current inflation data
/gdp - GDP information
/economy - Global economic news
/business - Business trends
/finance - Finance tips

💡 *Quick Tips:*
• Ask me about any economic concept
• Request market analysis
• Get explanations for complex terms
"""
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def market(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send market updates."""
    market_info = """
📈 *Market Updates*

💹 *Global Markets:*
• S&P 500: 4,500 📈 (+0.5%)
• Dow Jones: 35,000 📈 (+0.3%)
• NASDAQ: 14,000 📈 (+0.7%)

💱 *Currency:*
• USD/EUR: 0.92
• USD/GBP: 0.79
• USD/JPY: 148.5

🛢 *Commodities:*
• Gold: $2,050/oz
• Oil: $85/barrel

*Stay tuned for more updates!*
"""
    await update.message.reply_text(market_info, parse_mode='Markdown')

async def inflation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send inflation information."""
    inflation_text = """
📊 *Inflation Update*

🌍 *Global Inflation Rates:*
• USA: 3.2% (↓)
• Eurozone: 2.8% (↓)
• UK: 4.0% (↓)
• Japan: 2.5% (→)

📌 *Key Factors:*
• Central bank policies
• Energy prices
• Supply chain trends
• Consumer demand

💡 *Tip:* Inflation affects purchasing power and interest rates.
"""
    await update.message.reply_text(inflation_text, parse_mode='Markdown')

async def gdp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send GDP information."""
    gdp_text = """
📊 *GDP Growth Rates*

🌍 *Top Economies:*
• USA: 3.3% growth
• China: 5.2% growth
• India: 6.5% growth
• Germany: 0.8% growth

📌 *GDP Components:*
• Consumer spending
• Business investment
• Government spending
• Net exports

💡 *GDP shows economic health!*
"""
    await update.message.reply_text(gdp_text, parse_mode='Markdown')

async def economy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send global economic news."""
    economy_text = """
🌍 *Global Economic News*

📰 *Top Stories:*
• Fed signals rate cuts in 2024
• China's economy shows recovery
• Oil prices stabilize
• Tech sector growth continues

📊 *Key Indicators:*
• Unemployment: 3.7% (US)
• Consumer confidence: Rising
• Manufacturing PMI: 52.5

*Follow for daily updates!*
"""
    await update.message.reply_text(economy_text, parse_mode='Markdown')

async def business(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send business trends."""
    business_text = """
💼 *Business Trends 2024*

🚀 *Hot Trends:*
• AI integration in business
• Sustainable practices
• Remote work evolution
• Digital transformation

📈 *Key Sectors:*
• Technology: Growing
• Healthcare: Stable
• Real Estate: Modest
• E-commerce: Expanding

💡 *Stay ahead of the curve!*
"""
    await update.message.reply_text(business_text, parse_mode='Markdown')

async def finance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send finance tips."""
    finance_text = """
💰 *Finance Tips*

📌 *Smart Money Moves:*
1. Emergency fund (3-6 months)
2. Diversify investments
3. Pay off high-interest debt
4. Invest in education

📊 *Investment Basics:*
• Stocks vs Bonds
• Mutual Funds
• ETFs
• Real Estate

💡 *Start small, think long-term!*
"""
    await update.message.reply_text(finance_text, parse_mode='Markdown')

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button callbacks."""
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    responses = {
        'markets': market,
        'finance': finance,
        'global': economy
    }
    
    if data in responses:
        await responses[data](update, context)

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages."""
    text = update.message.text.lower()
    
    # Simple keyword responses
    if any(word in text for word in ['inflation', 'price', 'cost']):
        await inflation(update, context)
    elif any(word in text for word in ['market', 'stock', 'share']):
        await market(update, context)
    elif any(word in text for word in ['gdp', 'growth', 'economy']):
        await economy(update, context)
    elif any(word in text for word in ['business', 'company', 'trend']):
        await business(update, context)
    elif any(word in text for word in ['finance', 'invest', 'money']):
        await finance(update, context)
    elif any(word in text for word in ['hello', 'hi', 'hey']):
        await start(update, context)
    else:
        await update.message.reply_text(
            "🤔 I can help you with economics and finance topics!\n"
            "Try asking about: inflation, markets, GDP, business, or finance.\n"
            "Use /help to see all commands."
        )

def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("market", market))
    application.add_handler(CommandHandler("inflation", inflation))
    application.add_handler(CommandHandler("gdp", gdp))
    application.add_handler(CommandHandler("economy", economy))
    application.add_handler(CommandHandler("business", business))
    application.add_handler(CommandHandler("finance", finance))
    
    # Add callback query handler for buttons
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Add text handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    # Start the Bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
