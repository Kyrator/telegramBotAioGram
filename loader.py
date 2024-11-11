from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from config_data import config


bot = Bot(token=config.BOT_TOKEN)
dp: Dispatcher = Dispatcher()