    # Çevrim dışı kelime oyunu.
    # Copyright (C) 2022 libsoykan-dev

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.

import json # JSON veritabanını işlemek için json kütüphanesi eklenir

import veritabani # veritabani.py dosyası içe aktarılır. (veritabani.py dosyasını edindiğinizden emin olun!)

from time import sleep # Bekleme için time kütüphanesi

from random import randint # Rastgele kelime seçimi için random kütüphanesi

sozluk = json.loads(veritabani.jsondata) # Sözlük Veritabanı içe aktarılır

puan = float(0) # Puan değişkeni float 0 şeklinde belirlenir

yanlis = 0 # Yanlış soru sayacı atanır

dogru = 0 # Doğru soru sayacı atanır

input("""KURALLAR:
  	  - Kelimeler TDK Sözlüğü'nden rastgele seçilir.
  	  - Seçilen kelimeler 4 veya daha çok harflidir.
  	  - Boşluklar harf sayısına dahildir.
	  - Her soru 1 puandır.
	  - 4 yanlış bir doğruyu götürür.
	  - Puanınız negatif olursa oyun biter.
	  - Malesef istediğiniz sorudan başlayamazsınız :)
Devam etmek için ENTER basın...""") # Kuralları yazdırır

def sil(): # Konsolu temizleyen fonksiyon
	
	print("\033c\033[H", end='')
	
sil()

def sonsuz(): # 1'den sonsuza aralığını tanımla

    index = 1
    
    while True:
    
        yield index
        
        index += 1

for _ in sonsuz(): # Sonsuz döngü
    
    sil()
    
    print("PUAN: " + str(puan) + "\n-----------") # Puanı yazdır
    
    nkelime = sozluk[randint(1, 90000)] # 1 ile 90.000 arasında bir sayı seçip sözlükte bu sıralamadaki kelimeyi nkelime olarak atar
    
    kelime = nkelime['kelime'] # nkelime içerisindeki kelime başlıklı veriyi kelime olarak atar
    
    harfsay = str(len(kelime)) # Seçilen kelimenin harf sayısını harfsay değişkenine atar
    
    if len(kelime) < 4: # Eğer harf sayısı 4'ten küçükse
    	
    	continue # Döngüyü başa sar
    
    for arama in sozluk: # Sözlükte kelime arama döngüsü
    	
        if kelime.lower() == arama['kelime'].lower(): # Eşleşme bulunursa
    
            sanlam = int(arama['sanlam']) + 1 # Kelimenin kaç anlamı olduğu okunur
            
            for gug in range(1, sanlam): # Anlamları yazdırma döngüsü
    
                anlam = arama['anlam' + str(gug)] # Anlamları "anlam" değerine kaydeder
                
                print("\n", anlam) # Anlamı yazdırır
    
            else: # !!! Aynı değerlerin art arda yazdırılmasını önlemek için "else" kullanılmıştır
    
                cevap = input("\nYukarıda anlamı veya anlamları verilen " + harfsay + " harfli kelime nedir?\n\n>") # Kullanıcıdan cevap beklenir
                
                if cevap == kelime: # Eğer cevap doğruysa
                	
                	print("\nCevabınız doğru!") # Cevabın doğru olduğunu yazdırır
                	
                	puan +=1 # Puan değişkenine 1 ekler
                	
                	dogru += 1 # Doğru soru sayacına 1 ekler
                	
                	sleep(1) # 1 sn bekle
                	
                else: # Eğer cevap yanlışsa
                	
                	input("\nCevabınız yanlış! Doğrusu " + kelime + " olacaktı.\n\nDevam etmek için ENTER basın...") # Cevabın yanlış olduğunu ve doğrusunu yazdırır
                	
                	yanlis += 1 # Yanlış soru sayacına 1 ekler
                	
                	puan -= 0.25 # 4 yanlış 1 doğruyu götürür
                	
                	if puan < 0: # Puan 0'ın altına düşerse
                		
                		print("\nOyunu " + str(dogru) + " soruyu doğru, " + str(yanlis) + " soruyu yanlış cevaplayarak " + str(puan) + " puan ile bitirdiniz.") # Puan durumu yazdırılır
                	
                		exit() # GAME OVER!