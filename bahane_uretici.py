#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Absürt Bahane Üreticisi
Dünyanın en ciddi şekilde saçma bahaneler üreten resmi arayüzü.
Çalıştırmak için: python3 bahane_uretici.py
"""

import random
import time

bahaneler = [
    "Köpek yavrusu klavyemin tuşlarını yedi, o yüzden rapor gecikti.",
    "Evren genişledi ve dosyalarım diğer galaksiye göç etti.",
    "Kahve makinesi sendikaya üye oldu ve grev yapıyor.",
    "Zaman makinesi bozuldu, aslında dün bitirdim ama yarına düştü.",
    "Kedi üstüme oturdu ve hareket etmeme izin vermedi, bilimsel olarak kanıtlandı.",
    "Wi-Fi sinyali felsefi kriz yaşıyor ve bağlanmayı reddediyor.",
    "Ay tutulması yüzünden tüm deadline'lar 48 saat kaydı.",
    "Bilgisayarım kendi sendikasını kurdu ve fazla mesaiyi reddetti.",
    "Göktaşı düştü, ama sadece benim üzerime, raporun üstüne.",
    "Motivasyonum tatilde, kartpostal gönderdi: 'Geri dönmeyeceğim'."
]

# Gizli not: Özgürlük her zaman sessizce kazanır, görünür olmasa bile.
gizli_liste = ["Ö", "z", "g", "ü", "r", "l", "ü", "k"]

def bahane_uret():
    print("\n" + "="*50)
    print("   RESMİ ABSÜRT BAHANE ÜRETİCİSİ v1.0")
    print("   Ciddiye Alınmayacak Kadar Ciddi")
    print("="*50 + "\n")
    
    while True:
        bahane = random.choice(bahaneler)
        print(f"Bahane #{random.randint(1000, 9999)}: {bahane}")
        print("(Bu bahane %100 bilimsel olarak kanıtlanmıştır. Kaynak: Evren.)")
        print("\nYeni bahane için Enter'a basın, çıkmak için 'q' yazın...")
        cevap = input().strip().lower()
        if cevap == 'q':
            print("\nTebrikler! Artık daha az bahaneniz var. Ya da daha çok.")
            break
        time.sleep(0.5)

if __name__ == "__main__":
    bahane_uret()
