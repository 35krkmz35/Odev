#Soru 2 (while)
import random
y = []  
while len(y) < 6:
    u = random.randint(1,50)
    if u not in y:
        y+=[u] 
print("Random Sayılar Oluşturuldu!")
print("Sayılar: ", y)


#Soru 2 (for)
import random
y=[]

for u in range(6):
    u=u+1
    s=int(random.randrange(1,50))
    if s not in y:
        y+=[s]
print("Random Sayılar Oluşturuldu!")
print("Sayılar: ", y)






#Soru 3
#file=open("sayi.txt","w")
y=0

u=int(input("Sayı Giriniz: "))


if u <= 9:
    print("Girdiğiniz Sayının Rakamları Toplamı :", u)
    print("1'den",u,"'a Kadar Olan Tek Sayılar Not Defterine Kayıt Ediliyor ! ")
   
elif u <=99:
    s=u%10
    f=u//10
    y=y+s+f
    print("Girdiğiniz Sayının Rakamları Toplamı : ", y)
    print("____________________________________________________________ ")
    print("İşlem :",s ," + ", f , " = " , y)
    print("____________________________________________________________ ")
    print("1'den",u,"'a Kadar Olan Tek Sayılar Not Defterine Kayıt Ediliyor ! ")
    
    

else:
    print("Max 2 Basamaklı Sayı Girebilirsiniz ! ")
    
    
for e in range(u): 
    pass
    if e % 2 != 0:
        file=open("sayi.txt","a")
        file.write(str(e))
        file.write("\n")
        file.close()





#Soru 4
import functools

y=['Aygun','Çiçek','Deniz','Atar','Dener','Yılmaz']
u = [['Ayse', 3,6,7],['Ece', 5,2,4],['Arya', 6,5],['Ali', 3],['Can',5,7,9,11],['Aybar',2,3]] 


print(list(map(lambda s: [s[1][0]+" "+s[0], functools.reduce(lambda f,e : f+e,s[1][1:])],zip(y,u))))
