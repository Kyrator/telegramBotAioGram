from loader import bot, dp
from handlers import start, help, echo, bestdeal, city, lowprice, history, highprice

async def main():
    # scheduler.add_job(send_time_msg, 'interval', seconds=10)
    # scheduler.start()
    dp.include_router(start)
    dp.include_router(help)

    dp.include_router(highprice)
    dp.include_router(lowprice)
    dp.include_router(bestdeal)
    dp.include_router(history)
    dp.include_router(city)

    dp.include_router(echo)
    dp.include_router(None)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    dp.run_polling(bot)
