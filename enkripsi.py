#by Kevin Alvaro Adianto
#program enkripsi sederhana

try:
    new=open("enkripsi.txt","x")
    new.close()
except:
    kosong=1

huruf=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

pilihan=1
while pilihan !=3:
    print("""
    1. Enkripsi kata
    2. Buka Enkripsi
    3. Exit
    """)
    pilihan=int(input("Masukkan Pilihan: "))
    if pilihan == 1:
        tulis=''
        file=open("enkripsi.txt","w")
        masukan=input("Masukkan kata yang akan di enkripsi: ").upper()
        for j in (masukan):
            posisi=huruf.index(j)
            save=posisi-3
            tulis=tulis+str(save)+","
        file.write(tulis)
        file.close()
    elif pilihan == 2:
        enkripsi=''
        tulis=''
        file=open("enkripsi.txt","r")
        for baris in file:
            enkripsi=enkripsi+baris
            enkripsi=enkripsi.split(",")

        for i in (enkripsi):
            if i !='':
                lock=int(i)+3
                tulis=tulis+huruf[lock]
        print(tulis)
        file.close()
    elif pilihan == 3:
        print("Terima Kasih")
    else:
        print("mohon masukkan pilihan dari 1-3")