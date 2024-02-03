import asyncio
import logging
from random import randint

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="")
dp = Dispatcher()

# Хэндлер на команду /start
otek=500
@dp.callback_query(F.data.startswith("vgf"))
async def callbacks_num(callback: types.CallbackQuery):
    global otek
    data = callback.data.split('~')
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="эйлеа/однократное введение",
        callback_data="vgf~ei~3")
    )
    builder.add(types.InlineKeyboardButton(
        text="визкью с гормоном",
        callback_data="vgf~max~gorm"))
    builder.add(types.InlineKeyboardButton(
        text="визкью интравитр",
        callback_data="vgf~max~mono")
    )
    builder.add(types.InlineKeyboardButton(
        text="авастин субтеноново",
        callback_data="vgf~max~subt")
    )
    builder.add(types.InlineKeyboardButton(
        text="авастин субконъюнктивально",
        callback_data="vgf~max~subk")
    )
    builder.add(types.InlineKeyboardButton(
        text="авастин субтеноново",
        callback_data="vgf~max~intrav")
    )
    builder.adjust(1)

    if data[1] == "ei":
        otek = otek - 30
        await callback.message.edit_text(f'вы ввели эйлеа всего раз, этого мало \n оставшийся отек {otek}мкм',
                                         reply_markup=builder.as_markup())
    if data[1] == "max" and data[2]=='gorm':
        otek = otek - 150
        await callback.message.edit_text(f'вы ввели визкью в комбинации с гормоном \n оставшийся отек {otek}мкм',
                                         reply_markup=builder.as_markup(resize_keyboard=True))
    if data[1] == "max" and data[2] == 'mono':
        otek=otek-100
        await callback.message.edit_text(f'вы ввели визкью в виде монотерапии \n оставшийся отек {otek}мкм',
                                         reply_markup=builder.as_markup())
    if data[2] == "subt":
        otek = otek - 70
        await callback.message.edit_text(f'вы ввели авастин субтеноново \n оставшийся отек {otek}мкм',
                                         reply_markup=builder.as_markup())
    if data[2] == "subk":
        otek = otek - 30
        await callback.message.edit_text(f'вы ввели авастин субконъюнктивально \n оставшийся отек {otek}мкм',
                                         reply_markup=builder.as_markup())
    if data[2] == "intrav":
        otek = otek - 100
        await callback.message.edit_text(f'вы ввели авастин интравитреально \n оставшийся отек {otek}мкм',
                                         reply_markup=builder.as_markup())

    if otek<=0:
        await callback.message.edit_text('ОТЕК КУПИРОВАН!\n Анти-ФРЭС терапия завершена!',
                                         reply_markup=builder.as_markup())

@dp.message(F.text.lower() == "эйлеа")
async def eilea(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="эйлеа:однократное введение",
        callback_data="vgf~ei~3")
    )
    await message.answer("количество инъекций", reply_markup=builder.as_markup())

@dp.message(F.text.lower() == "визкью")
async def viskyu(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="визкью интравитреально/с гормоном",
        callback_data="vgf~max~gorm")
    )
    builder.add(types.InlineKeyboardButton(
        text="визкью интравитр/монотерапия",
        callback_data="vgf~max~mono")
    )
    await message.answer("визкью/способ введения ", reply_markup=builder.as_markup())

@dp.message(F.text.lower() == "авастин")
async def avastin(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="авастин субтеноново",
        callback_data="vgf~max~subt")
    )
    builder.add(types.InlineKeyboardButton(
        text="авастин субконъюнктивально",
        callback_data="vgf~max~subk")
    )
    builder.add(types.InlineKeyboardButton(
        text="авастин интравитреально",
        callback_data="vgf~max~intrav")
    )
    await message.answer("авастин/способ введения ", reply_markup=builder.as_markup())

@dp.message(F.text.lower() == "лечение")
async def treatment(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Эйлеа'))
    builder.add(types.KeyboardButton(text='Визкью'))
    builder.add(types.KeyboardButton(text='Авастин'))
    builder.adjust(3)
    await message.answer(
        "Выберите VGF:",
        reply_markup=builder.as_markup(resize_keyboard=True),
        )
   # или просто await callback.answer()
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())