from aiogram.filters import Command
from config_data.config import COMMANDS
from aiogram.types import Message
from loader import dp


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands='help'))
async def process_help_command(message: Message) -> None:
    """
    Отправка списка доступных команд.
    """
    text = [f'/{command} - {desk}' for command, desk in COMMANDS]

    await message.answer('\n'.join(text))
