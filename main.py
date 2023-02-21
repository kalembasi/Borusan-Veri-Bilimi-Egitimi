borusan = []
type(borusan)

notlar = [90, 5.4, "malik", [1, 2, 3]]
len(notlar)
type(notlar)
notlar[-1] #basic indexing
notlar[-1][1]
notlar[1:3] #slicing

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[::2]
numbers[::-1]
numbers[1::2]

notlar[3][:2][1]

combineList = [notlar, numbers]
print(combineList)
len(combineList)
len(combineList[1])

liste = ["malik", "tunahan", "omer", "kemal"]
liste[1] = "kalembasi"
liste[:3] = "omer", "malik", "kalembasi"
liste[0] = [1, 2, 3]
liste = liste + ["feyza"]
liste - ["feyza"] #error
liste = liste + [["burak"]]
liste = [liste, [78]] #iki farklı liste toplanır ve listeye eşitlenir
liste = [liste, "bb"]
len(liste)

a = [1, 2, 3, 4, 5, 6]
a.append(7)
a.remove(5) #inplace true
b = "malik"
b.upper() #inplace false

del a[0]
a.pop() #returns the removed value, inplace true
a.pop(3)

a = [1, 2, 3, 4, 5, 6]
del a[:3]

a = [1, 2, 3, 4, 5, 6]
removedElements = []
removedElements.append(a.pop())
removedElements.append(a.remove(6))
removedElements

a = [1, 2, 3, 4, 5, 6]
a.insert(0, 78) #list.insert(index, value)
a.index(78)
a.insert(a.index(78), 67)
a.append("a")
a.extend(["b", "c", "d"])
a.extend([1, 1, 1, 1])
a.count(1)
a.reverse() #inplace true

a = [1, 2, 3, 4, 5, 6]
a.reverse()
a.sort() #asc, inplace true
a.sort(reverse = True) #reverse flag set as true for descending order

a.clear()

#ders4 functions
a = "borusan"
len(a)
type(a)
print(a)

#methods
a.upper()
a.capitalize()
a.isupper()

#ders5

sozluk = {"REG" : "Regresyon model",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}

sozluk.items() #same as sozluk
type(sozluk)
sozluk.values()
sozluk.keys()

sozluk["REG"]

sozluk["REG"] = "Borusan"
sozluk["NEW"] = "New Element"
sozluk

#sozluk["a"] = liste.pop()

sozluk[0] = "malik"
sozluk

liste = [1, 2, 3, 4]
sozluk[liste] = "busra" #key degistirilemez, liste konamaz
t = (1, 2, 3, 4)
sozluk[t] = "cuneyt"
sozluk

s = {1, "malik", 4, 5.2}
type(s)

"malik" in s #return true
s[0] = 2 #çalısmaz indexleme yok

s.add(2)
s.remove("malik")
s.discard("malik") #element varsa çıkarır yoksa devam eder

#operators and built-in functions

import math
math.sqrt(16)
math.ceil(1.9)

a = 1
b = True

a == b #checks value
a is b #checks type and value

#in, not in

