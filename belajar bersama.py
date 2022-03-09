nama ="nike"
alamat="lutang"
tanggal_lahir=20
jenis_kelamin= "perempuan"
tinggibadan= 154
berat_badan=6.8

print(alamat,type(alamat))
print(tanggal_lahir, type(tanggal_lahir))
print(jenis_kelamin, type(jenis_kelamin))
print(tinggibadan, type(tinggibadan))
print(berat_badan,type(berat_badan))
nama=input("masukkan nama :")
alamat=input("masukkan alamat :")
tanggal_lahir=int(input("masukkan tanggal lahir : "))

print("habis di bagi 3")
for i in range (1,100):
    if i % 3 != 1 :
        i+=1
        print(i) 
print("habis di bagi 5")
for i in range (2,100,2):
    if i % 5 == 0:
        print(i)
print("bilangan ganjil 1 sampai 10")       
i=1
while i <= 10:
    print(i)
    i+=2
       