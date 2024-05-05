"""Имена и количества файлов известны. Использую Цикл while
Считываются файлы по порядку. В словарь добавляю ключём количество строк
В значения добавляю название файла, делитель и сам текст файла.
"""
i, textfile = 1, {}
while i < 4:
    with open(str(i)+'.txt', "r", encoding="utf8") as f:
        text = f.read()
        textfile[text.count('\n') + 1] = f.name + ' | ' + text
        i += 1
"""Сортирую от меньшего к большему по количествую строк"""
sort_textfile = dict(sorted(textfile.items()))
"""Для записи в нужном формате получаю элементы ключ и значение.
Записываю с перносом на новую строку"""
with open('result.txt', 'w', encoding="utf8") as f:
    for key, value in sort_textfile.items():
        name = value[:value.find(" | ")]
        text = value[value.find(" | ") + 3:].replace(" | ", "")
        f.write(f'{name}\n{key}\n{text}\n')
