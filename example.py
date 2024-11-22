a=["aaaa","bbbbbb"]
b=["cccc","dddddd"]
c=a+b
print(c)
f=["cagan,","demirci"]
f+=["eren","köymen"]
print(f)




liste=[15,25,69,65,-5,0,-15,15,20]

poz=liste[0]+liste[2]+liste[3]+liste[7]+liste[8]
neg=liste[4]+liste[6]

print("Pozitif toplam: {}, Negatif toplam: {}".format(poz,neg))







p=[0,0,0,0,0,1,1,1,0,0]
dilim=p[5:8]
print(dilim)









kelime=input("lütfen kelime gir")
print(kelime==kelime[::-1])








a1=(1,2,3,4,5)
A1=a1[2]




api={"username":"ellap","password":"12345"}
db=["ellap","12345"]
print(api["username"]==db[0])


api["password"]="yetmişbir"
print(api)

