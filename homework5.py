#1
with open("text.txt", "w", encoding='utf-8') as f_obj:
    while True:
        line = input('Введите линию: ')
        if not line:
            break
        print(line, file=f_obj)

#2
count = 0
with open("text_2.txt", 'r', encoding='utf-8') as f_obj_2:
    for line in f_obj_2:
        count += 1
        line_words = line.split()
        print(line, "Длина троки: ", len(line_words))
print(count)

#3
with open('text_3.txt', 'r', encoding="utf-8") as f_obj_3:
    s_sum = []
    less = []
    line = f_obj_3.read().split("\n")
    for i in line:
        i = i.split()
        if float(i[1]) < 20000:
            less.append(i[0])
        s_sum.append(i[1])

print(f"less 20.000 {less}, {sum(map(float, s_sum))/len(s_sum)} ")

#5

from random import randint

sum_el = 0

with open("text_5.txt", "w", encoding="utf-8") as my_file_2:
    for i in range(100):
        el = randint(1, 100)
        sum_el += el
        my_file_2.write(str(el) + " ")

print(f"Sum of elements - {sum_el}")



