# Задание 1 - посчет количество слов в тексте входящего файла. 
# Студент: Тархов Павел Андреевич
# Дата: 01.06.2021

# Словарь для подсчета количества слов
wordDict = dict()

# Открытие файла, построчное чтение, и сохранение слов в словаре
fin = open('resourse_1.txt', 'r')
for line in fin:
    for word in line.split():
        word = word.lower()
        if word in wordDict.keys(): 
            wordDict[word] = wordDict[word] + 1
        else:
            wordDict[word] = 1
fin.close()

# Преобразование словаря в список и его сортировка
li = list(wordDict.items())
li.sort(key=lambda x:(-x[1], x[0]))

# Запись в файл вывода
fout = open('result_1.txt', 'w')
for couple in li:
    print(couple)
    fout.write(str(couple[0]) + ' ' + str(couple[1]) + '\n')

fout.close()
