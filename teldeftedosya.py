data=[]
telefon_defteri = {}

with open ("telefon_defteri.txt","r+") as file:
    for i in file:
        if i !="":
            data=i.split(":")
            telefon_defteri[data[0]]=data[1]



    menu="""1-Kisi ekleme
            2-Goruntuleme
            3-guncelle
            4-sil
            5-Cik
    """


    while True:
        print (menu)
        tercih=raw_input("Yapmak istediginiz islemi secin")
        if tercih=="2":
            kisi = raw_input("Telefon numarasini ogrenmek istediginiz kisinin adini giriniz: ")
            if kisi in telefon_defteri:
                cevap = "{} adli kisinin telefon numarasi: {}"
                print(cevap.format(kisi, telefon_defteri[kisi]))
            else:
                print ("Kisi bulunamadi")
        elif tercih=="1":
            ad=raw_input("eklemek istediginiz isim:")
            no=raw_input(" eklemek istediginiz no:")
            telefon_defteri[ad]=no

        elif tercih=="3":
            guncelle = raw_input("Guncellemek isteginiz kisinin ismi:")
            no=raw_input("Yeni numara:")
            telefon_defteri[guncelle]=no
        elif tercih=="4":
            sil=raw_input("silmek istediginiz ismi giriniz:")
            telefon_defteri.pop(sil)
        elif tercih=="5":
            break

    file.truncate()
    for i,j in telefon_defteri.items():
        file.write(i)
        file.write(":")
        file.write(j)
        file.write("\n")

