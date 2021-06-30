def conv_celcius():
    "konversi kelvin ke celcius"
    print("Konversi Suhu Kelvin ke Celcius") # Judul atau penjelasan dalam konversi 
    kelvin = int(input("Masukan Kelvin: ")) # Memasukan angka dalam kelvin yang mau di konversi ke celcius
    conv_k = kelvin - 273 # Rumus konversi dari klevin ke celcius
    print(f'hasil dari Konversi Suhu {kelvin} k adalah {conv_k} C')
conv_celcius()  # Untuk memanggil Fungsi 

def conv_kelvin():
    "konversi celcius ke kelvin"
    print("Konversi suhu celcius ke kelvin")
    c = int(input("Masukan Celcius: ")) # Memasukan angka dalam celcius yang mau di konversi ke kelvin
    conv_c = c + 273 # Rumus konversi dari celcius ke kelvin
    print(f'hasil dari konversi suhu {c} C adalah {conv_c} K') #f unutk menagambil variabel atau fungsinya  
conv_kelvin()  

# Percobaan Pertama 
# def conv_F():
#     "Konversi C/K ke F"
#     print("Konversi suhu Celcius/Kelvin ke Farenhait")
#     c = int(input("Masukan Celcius : "))
#     conv_c = 9 * c / 5 + 32
#     k = int(input("Masukan Kelvin : "))
#     conv_k = 9 * k-273 / 5 + 32
#     print(f'hasil dari konversi Suhu {c} C adalah {conv_c} F')
#     print(f'hasil dari konversi suhu {k} K adalah {conv_k} F')
# conv_F()

#Pecobaan Kedua 
def conv_F_to_ck(suhu):
   drjt = int(suhu[:-1])
   inputan1 = suhu[-1]

   if inputan1.upper() == "F":
     hasil1 = float(5 * (drjt-32) / 9)
     hasil2 = float(5 * (drjt-32) / 9 + 273)
     jenisX = "Celcius","Kelvin"
     jenis1 = "Farenhait"
     jenis2 = "Farenhait"
     print(drjt,jenisX,"=","{:.1f}".format(hasil1),jenis1)
     print(drjt,jenisX,"=","{:.1f}".format(hasil2),jenis2)

def conv_f_to_ck():
      "Konversi Suhu dari farenhait ke Celcius / Kelvin "
      print("Konversi suhu Farenhait ke Celcius/Kelvin")
      fc = int(input("Masukan Farenhait : "))
      conv_c = 5 * (fc-32) / 9
      fk = int(input("Masukan Farenhait : "))
      conv_k = 5 * (fk-32) / 9 + 273
      print(f'hasil dari konversi suhu {fc} F adalah {conv_c} C')
      print(f'hasil dari konversi suhu {fk} F adalah {conv_k} K')
conv_f_to_ck()

