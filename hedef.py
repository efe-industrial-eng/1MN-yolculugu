import json # Depo dosyasını okumak için gerekli kütüphane

# 1. MAKİNE: Depodan veriyi okur
def veriyi_yukle():
    with open('data.json', 'r') as dosya:
        return json.load(dosya)

# 2. MAKİNE: Depoya yeni veriyi kaydeder
def veriyi_kaydet(yeni_veri):
    with open('data.json', 'w') as dosya:
        json.dump(yeni_veri, dosya, indent=4)

# --- ANA SÜREÇ ---
depo = veriyi_yukle()
print(f"Sistem Acildi! Su anki toplam kazancin: {depo['toplam_kazanc']} TL")

# Yeni kazancı al ve depoyu güncelle
bugunku = float(input("Bugün ne kadar kazandın? "))
depo['toplam_kazanc'] += bugunku # Eski kazanca ekle

veriyi_kaydet(depo)
print(f"Basarili! Yeni bakiyen: {depo['toplam_kazanc']} TL. Veri depoya kilitlendi.")