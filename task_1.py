print('Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке')

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

def rhythm(phrase):
    phrase = phrase.split()
    result_list = []
    for word in phrase:
        result = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                result += 1
        result_list.append(result)
    return len(result_list) == result_list.count(result_list[0])

phrase = input('\nВведите фразу: ')
if rhythm(phrase):
    print('\nРезультат: Парам пам-пам')
else:
    print('\nРезультат: Пам парам')