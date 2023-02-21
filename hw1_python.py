# 1- İki çocuğunun yaşları toplamı 5’tir. 3 yıl sonra babanın yaşı çocukların yaşları toplamının 3 katı olacağına göre babanın bugünkü yaşı kaçtır?
# Denklemi python dilinde kurunuz ve çıktıyı print ediniz.
print(3*(5+3+3)-3) #babanın bugünkü yaşı


# 2-
Metin ="Veri bilimi, verilerden değer elde etmek için istatistik, bilimsel yöntemler, yapay zeka (AI) ve veri analizi dahil olmak üzere birçok " \
       "alanı bir araya getirir. Veri Bilimiyle uğraşan kişilere veri bilimci denir. Bu kişiler web, akıllı telefonlar, müşteriler, sensörler ve " \
       "diğer kaynaklardan toplanan verileri analiz etmek ve bunlardan eyleme dönüştürülebilir içgörüler üretmek amacıyla bir dizi beceriyi bir araya getirir."

# Yukarıda yer alan metindeki “veri bilim” kelimelerini bulup yerine “VERİ BİLİM” yazınız.
Metin.replace("veri bilim", "VERİ BİLİM")
Metin.replace("Veri bilim", "VERİ BİLİM")


# 3- Adını, soyadını, yaşını, yaşadığın şehri ve üniversite ortalamanı aralarında birer boşluk olacak şekilde kullanıcıdan alıp tek bir print ifade içerisinde yazın.
# input() fonksiyonunu kullanabilirsin.
ad = input()
soyad = input()
yas = input(); yas = int(yas)
sehir = input()
ort = input(float); ort = float(ort)

print(ad, soyad, yas, sehir, ort)


# 4-
MEtin = "Veri bilimi günümüzün en heyecan verici alanlardan biridir."
# "Veri bilimi" ve "alanlardan biridir." kelimelerini cümle içerisinden alınız ve her kelimeyi uzunlukları kadar aşağı doğru çoğaltarak print ediniz.
len(" ".join(MEtin.split()[:2])) #11
len(" ".join(MEtin.split()[6:8])) #19

print(" ".join(MEtin.split()[:2]))
print(" ".join(MEtin.split()[6:8]))


# 5- "veri bilimi" ve "VERİ BİLİMİ" kelimelerinden hangisi büyük hangisi küçük harf ile yazılmış kontrol ediniz.
"veri bilimi".isupper() #False
"VERİ BİLİMİ".isupper() #True


# 6- adınız, soyadınız, yaşınız, yaşadğınız şehir ve universite not ortalamanız ile bir liste oluşturunuz. Oluşturduğunuz listeyi “listem” değişkeni olarak kaydediniz.
listem = []
listem.append(ad)
listem.append(soyad)
listem.append(yas)
listem.append(sehir)
listem.append(ort)


# 7- "listem" değişkeni içerisinden yaşınızı, yaşadığınız şehiri ve universite not ortalamanızı seçerek "listem2" değişkenini oluşturunuz.
listem2 = []
listem2.append(listem[2])
listem2.append(listem[3])
listem2.append(listem[4])


# 8- “listem2” değişkeninin her bir elamanının türlerini yazdırınız.
print(type(listem2[0]))
print(type(listem2[1]))
print(type(listem2[2]))


# 9- “listem2” değişkenine aşağıdaki listeyi LİSTE olarak ekleyiniz.
eklenecek_liste = ["Ali", 90, "Mehmet"]
listem2.append(eklenecek_liste)


# 10- “listem2” değişkeninin içinden “Ali” ve “90” ı seçip Listem3 değişkenine atayınız.
listem3 = []
listem3.append(listem2[-1][0])
listem3.append(listem2[-1][1])


# 11- “listem2” değişkenine Listem3 değişkenini ELEMAN olarak ekleyiniz.
listem2 = listem2 + listem3


# 12- “listem2” içerisinden 90 elemanını siliniz.
listem2.remove(90)


# 13- 1'den 10'a kadar tüm rakamları artacak şekilde sıralanmış şekilde bir liste oluşturunuz.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 14- 1'den 10'a kadar tüm rakamları azalacak şekilde sıralanmış şekilde bir liste oluşturunuz. "yeni_liste" değişkenine atayınız.
yeni_liste = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# 15- “yeni_liste” değişkeninin içerisindeki 7 ve 2 elemanlarının yerlerini belirtiniz.
yeni_liste.index(7) #3
yeni_liste.index(2) #8