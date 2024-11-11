from aiogram.filters import Command
from aiogram.types import Message
from loader import dp


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')
    await message.answer('Вызов справки /help')
    await message.answer('Здесь можно посмотреть информацию от отелях с сайта Hotels.com')

    # bot.delete_state(message.from_user.id, message.chat.id)  # удаляем сохраненные данные
    # bot.set_state(message.from_user.id, UserState.all, message.chat.id)
    #
    # handlers.custom_heandlers.related.step(message.from_user.id, 1)