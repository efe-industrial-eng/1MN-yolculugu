import json

def veriyi_yukle():
    with open('data.json', 'r') as dosya:
        return json.load(dosya)

def veriyi_kaydet(yeni_veri):
    with open('data.json', 'w') as dosya:
        json.dump(yeni_veri, dosya, indent=4)

depo = veriyi_yukle()
print(f"System ready. Current total earnings: ${depo['toplam_kazanc']:,.0f}")

bugunku = float(input("Enter today's earnings (TL): "))
depo['toplam_kazanc'] += bugunku

veriyi_kaydet(depo)
print(f"Success! New balance: ${depo['toplam_kazanc']:,.0f}. Data saved.")