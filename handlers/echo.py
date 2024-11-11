from aiogram.filters import Command
from config_data.config import COMMANDS
from aiogram.types import Message
from loader import dp

@dp.message(Command(commands=None))
async def process_echo(message: Message):
    await message.answer(f'Выберите команду.')
