import random
from aiogram import types
from loader import dp

max_count = 150
total = 0
new_game = False
duel = []
first = 0
current = 0
max_candy = 28


@dp.message_handler(commands=['start', 'старт'])
async def mes_start(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f'{name}, привет! Сегодня сыграем с тобой в конфеты!\n'
                         f'Для начала игры введи команду /new_game.\n'
                         f'Или /duel и id оппонента, для игры вдвоем\n'
                         f'Для настройки количества конфет введи команду /set и укажи их количество (по умолчанию 150)\n'
                         f'За один ход можно брать не более 28 конфет. Для изменения значения набери команду\n'
                         f'/max_candy и укажи количество конфет после пробела')
    print(message.from_user.id)


@dp.message_handler(commands=['new_game'])
async def mes_new_game(message: types.Message):
    global new_game
    global total
    global max_count
    global first
    new_game = True
    total = max_count
    first = random.randint(0, 1)
    if first:
        await message.answer(f'Игра началась. По жребию первым ходит {message.from_user.first_name}! Бери конфеты...')
    else:
        await message.answer(f'Игра началась. По жребию первым ходит Ботяо')
        await bot_turn(message)

@dp.message_handler(commands='my_id')
async def mes_my_id(message: types.Message):
    await message.answer(message.from_user.id)

@dp.message_handler(commands=['duel'])
async def mes_duel(message: types.Message):
    global new_game
    global total
    global max_count
    global duel
    global first
    global current
    total = max_count
    first = random.randint(0, 1)
    if len(message.text.split()) != 1:
        duel.append(int(message.from_user.id))
        duel.append(int(message.text.split()[1]))
        if first:
            await dp.bot.send_message(duel[0], 'Первый ход за тобой, бери конфеты')
            await dp.bot.send_message(duel[1], 'Первый ход за твоим противником! Жди своего хода')
        else:
            await dp.bot.send_message(duel[1], 'Первый ход за тобой, бери конфеты')
            await dp.bot.send_message(duel[0], 'Первый ход за твоим противником! Жди своего хода')
        current = duel[0] if first else duel[1]
        new_game = True
    else:
        await message.answer('Для игры в режиме "дуэль" необходимо у соперника получить его id\n'
                             'Чтобы узнать id, сопернику необходимо ввести команду /my_id\n'
                             'Для старта игры в режиме "дуэль" Вам необходимо ввести команду:\n'
                             '/duel "id-соперника"')


@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global max_count
    global new_game
    global max_candy
    name = message.from_user.first_name
    count = message.text.split()[1]
    if not new_game:
        if int(count) <= max_candy:
            await message.answer(f'\n{name}, общее количество конфет не может быть равным или меньше, чем '
                                 f'количество конфет, которые можно взять за 1 ход. По умолчанию за один ход /'
                                 f'можно взять не более {max_candy} конфет.\n/'
                                 f'Ты можешь изменить количество конфет за 1 ход по команде /max_candy')
        elif count.isdigit():
            max_count = int(count)
            await message.answer(f'Конфет теперь будет {max_count} ')
        else:
            await message.answer(f'{name}, напишите цифрами')
    else:
        await message.answer(f'{name}, нельзя менять правила во время игры')

@dp.message_handler(commands=['max_candy'])
async def mes_max_candy(message: types.Message):
    global new_game
    global max_candy
    name = message.from_user.first_name
    count = message.text.split()[1]
    if not new_game:
        if count.isdigit():
            max_candy = int(count)
            await message.answer(f'За 1 ход теперь можно брать не более {max_candy} конфет')
        else:
            await message.answer(f'{name}, напишите цифрами')
    else:
        await message.answer(f'{name}, нельзя менять правила во время игры')

@dp.message_handler()
async def mes_take_candy(message: types.Message):
    global new_game
    global total
    global max_count
    global duel
    global first
    global max_candy
    name = message.from_user.first_name
    count = message.text
    if len(duel) == 0:
        if new_game:
            if count.isdigit() and 0 < int(count) < max_candy + 1:
                total -= int(count)
                if total <= 0:
                    await message.answer(f'Ура! {name} ты победил!')
                    new_game = False
                else:
                    await message.answer(f'{name} взял {count} конфет. '
                                         f'На столе осталось {total}')
                    await bot_turn(message)
            else:
                await message.answer(f'{name}, надо указать ЧИСЛО от 1 до {max_candy}!')
    else:
        if current == int(message.from_user.id):
            if new_game:
                if count.isdigit() and 0 < int(count) < max_candy + 1:
                    total -= int(count)
                    if total <= 0:
                        await message.answer(f'Ура! {name} ты победил!')
                        await dp.bot.send_message(enemy_id(), 'К сожалению ты проиграл! Твой оппонент оказался умнее! :)')
                        new_game = False
                    else:
                        await message.answer(f'{name} взял {count} конфет. '
                                             f'На столе осталось {total}')
                        await dp.bot.send_message(enemy_id(), f'Теперь твой ход, бери конфеты! На столе осталось ровно {total}')
                        switch_players()
                else:
                    await message.answer(f'{name}, надо указать ЧИСЛО от 1 до {max_candy}!')


async def bot_turn(message: types.Message):
    global total
    global new_game
    global max_candy
    bot_take = 0
    if 0 < total < max_candy + 1:
        bot_take = total
        total -= bot_take
        await message.answer(f'Бот взял {bot_take} конфет. '
                             f'На столе осталось {total} и бот одержал победу')
        new_game = False
    else:
        remainder = total % (max_candy + 1)
        bot_take = remainder if remainder != 0 else max_candy
        total -= bot_take
        await message.answer(f'Бот взял {bot_take} конфет. '
                             f'На столе осталось {total}')

def switch_players():
    global duel
    global current
    if current == duel[0]:
        current = duel[1]
    else:
        current = duel[0]


def enemy_id():
    global duel
    global current
    if current == duel[0]:
        return duel[1]
    else:
        return duel[0]
