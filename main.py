

summa = 0
skaitlis = []
with open('skaitli.txt', encoding = "utf-8") as f:
  for line in f:
      skaitli.append(line)
print(f' Saraksta garums = {len(skaitli2)}')
for i in range(len(skaitli2)):
  summa += int(skaitli2[i])
print(f'Skaitļu summa ir {summa}')
a = int(input("Ievadi skaitli"))

with open('skaitlis.txt', mode = "w",  encoding = "utf-8") as f:
  f.writelines('Rezultāts ir ' + str(summa) + '\n')
