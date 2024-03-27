'''

	Зробити гру "Каміння. Ножиці. Папір"

  Користувач обирає предмет (к, н або п). Після чого
  комп'ютер випадково також обирає предмет. Предмети
  зберігаються у пам'яті у вигляді перших літер (к, н або п).

  Після вибору програма виводить вибір кожного гравця повними
  назвами. Наприклад: Каміння проти Паперу.

  Після чого виводиться переможець.

  Програму розбити на наступні функції:
  1. Функція вибору предмету (як для користувача, так і для комп'ютера)
  	player_choice = choose_item(bot=False) — запитає у користувача предмет
  	і поверне те, що він обрав
  	bot_choice = choose_item(bot=True) — поверне випадковий предмет

  2. Функція виведення повної назви
  	print(full_name('к')) — виведе "Каміння"

  3. Функція встановлення переможця
  	claim_winner(player='к', bot='п') — поверне 'bot' або 'b'
  	claim_winner(player='н', bot='п') — поверне 'player' або 'p'
	claim_winner(player='н', bot='н') — поверне 'draw' або 'd'
	claim_winner(player='о', bot='н') — поверне None

'''
import random
player_item = ''
bot_item = random.choice()

def get_winner(player, bot):
    if player == 'к' and bot == 'п':
        return 'bot'

player = 'к'
bot = 'п'

winner = get_winner(player, bot)

if winner == 'bot':
    print('Bot wins!')