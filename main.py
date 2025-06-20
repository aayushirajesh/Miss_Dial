import phonenumbers, pytz, os, pycountry
from phonenumbers import geocoder, timezone, carrier
from phonenumbers.phonenumberutil import NumberParseException, region_code_for_number
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder,CommandHandler, MessageHandler, ContextTypes, filters
from pathlib import Path

env_path = Path(__file__).parent / ".env"  # Absolute path
load_dotenv(dotenv_path=env_path)
TELEGRAM_TOKEN = os.getenv('BOT_TOKEN')

#tells if it’s currently Day or Night in that country based on time
def get_day_or_night(timezone_str):
    try:
        tz =pytz.timezone(timezone_str)
        local_time = datetime.now(tz)
        hour = local_time.hour
        return "Day" if 6 <= hour < 18 else "Night"
    except:
        return "Unknown"
    
#every time someone sends message to bot
async def handle_message(update:Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.strip()
    try:
        phone = phonenumbers.parse(user_input, None)
        if not phonenumbers.is_valid_number(phone):
            raise ValueError("Invalid Number or Format")
        number_str = user_input
        country_code = region_code_for_number(phone)   # Get country code like "RU", "IN"
        country = pycountry.countries.get(alpha_2=country_code).name if country_code else "Unknown"
        region_description = geocoder.description_for_number(phone, "en")
        region = region_description if region_description and region_description != country else "Not Available"
        timezones = timezone.time_zones_for_number(phone)
        tz_name = timezones[0] if timezones else "Unknown"

        tz = pytz.timezone(tz_name)
        current_time = datetime.now(tz).strftime("%d-%m-%Y  %H:%M:%S")
        day_or_night =get_day_or_night(tz_name)

        #bot's main reply message
        response = (
            f"📞 Number: {number_str}\n"
            f"🌍 Country: {country}\n"
            f"📍 Region: {region}\n"
            f"🕒 Local Time: {current_time}\n"
            f"⏱️ Timezone: {tz_name}\n"
            f"🌞 Time of Day: {day_or_night}"
        )
    except:
        response = "❌ Number Invalid. Check Again"

    await update.message.reply_text(response)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Send me a number and I'll give you Country and Local Time ")


def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()