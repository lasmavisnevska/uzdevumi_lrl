a = int(input("Ievadi skaitli"))

with open('skaitlis.txt', mode = "w",  encoding = "utf-8") as f:
  f.writelines('Rezultāts ir ' + str(summa) + '\n')




