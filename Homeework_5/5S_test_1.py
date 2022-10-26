# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".
str = "Бавария, забвение, взбадривать, Амбивалентность, сон, разговор, Арарат, Аббат"
str_split = str.split(" ")
ch1, ch2, ch3  = "а", "б", "в"
res = []
for i in str_split:
    if any([ch1 not in i.lower(), ch2 not in i.lower(), ch3 not in i.lower()]): # т.к. "абв" в вводе изначально строчные, то .lower() к ним не стал применять
        res.append(i)
print(" ".join(res))
