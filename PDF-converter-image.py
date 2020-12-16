# -*- coding: cp1254 -*-
from PIL import Image
import os
import pdfkit

sor = input("\n [1] Image\n [2] HTML\n\n Hangisi: ")

filenm = raw_input("\n filename: ")
savefile= "converted_"+filenm[:6]

if(sor==1):
    image1 = Image.open(str(filenm))
    im1 = image1.convert('RGB')
    im1.save(str(savefile)+".pdf")

    if(savefile in os.listdir(os.getcwd())):
        print "\n Basariyla cevrildi: ",savefile+".pdf"

    else:
        print "\n Error"
elif(sor==2):
    w = pdfkit.from_file(str(filenm), str(savefile)+'.pdf')
    if(w):
        print u"\n\n[+] Dosya basariyla kaydedildi, dosya adı: ", str(savefile)+'.pdf'
    else:
        print "\n -- ERROR -- HATA -- \n"
else:
    print "\n error"
