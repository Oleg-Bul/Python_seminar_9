# # Напишите программу, удаляющую из текста
# # все слова, содержащие "абв"
# *' 'абвгд гдежз жзе абв ыопыпт' -> ' гдежз жзе ыопыпт'

txt = 'абвгд гдежз жзе абв ыопыпт'
# print(f"Исходный текст: {txt}")
a = []
find_txt = 'абв'
# lst = [i for i in txt.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')
for i in txt.split():
    if find_txt not in i:
        a.append(i)
print(a)

# del_st = lambda x, y: " ".join([i for i in x.split() if y not in i])


# print(del_st('абвгд гдежз жзе абв  ыопыпт', 'абв'))
