import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

cntPw = input('Укажите количество паролей для генерации:')
lenPw = input('Укажите длину одного пароля:')
digOn = input('Включать ли цифры 0123456789? (y/n)')
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')

if digOn.lower() == 'y':
    chars += digits
if ABCon.lower() == 'y':
    chars += uppercase_letters
if abcOn.lower() == 'y':
    chars += lowercase_letters
if chOn == 'y':
    chars += punctuation