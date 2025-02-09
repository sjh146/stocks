

#'https://api.telegram.org/bot7903260976:AAEQtnBt1kBNGxdidPx6cHreMo5QgDSEXpM/getUpdates'
import telegram 
import asyncio
async def main():

    token = "7903260976:AAEQtnBt1kBNGxdidPx6cHreMo5QgDSEXpM"
    bot = telegram.Bot(token)

    await bot.send_message(chat_id="-1002411723910", text="hello")

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
