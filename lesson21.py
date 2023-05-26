import logging

from aiogram import Bot, Dispatcher, executor, types
from search_wiki import get_wiki_page

API_TOKEN = '6084780027:AAHKczacgJgBbRs3ZPxYJLatdslFR5M3tkI'

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(

    types.KeyboardButton("Contact with admin😀")
)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Hi!", reply_markup=menu)

# text, video, documant, photo, animation, sticker, voice, audio

@dp.message_handler(content_types=["text"])
async def user_text_handler2(message: types.Message):
    user_text = message.text
    result = get_wiki_page(user_text)
    if result:
        await message.answer(result)
    else: 
        await message.answer("😂😂Malumot yo'q😂😂")
    if user_text == "Contact with admin😀":
        await message.answer("💻 Admin : @Shauxratovlar ")
    else:
        
        await message.answer(message.text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


# admin bilan bog'lanish tugmasi bosilganda bot biza bizning usernameni tashash.