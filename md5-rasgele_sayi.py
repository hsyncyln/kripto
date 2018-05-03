import hashlib

def md5(yeni): 
    sifreleyici=hashlib.md5(yeni.encode("utf-8")).hexdigest()  
    return sifreleyici

def decimal(sonuc):
    return int(sonuc,16)

n=int(input("Kac basamakli rasgele sayi:"))

x0=open(r"C:\Users\ghost\Desktop\DERSLER\Bilgisayar Organizasyonu\dizi.txt")

sonuc=str()

for i in range(n):
    x1=md5(str(x0))
    sonuc=sonuc+str(x1)[7] 
    x0=x1

print(decimal(sonuc))



