import json
import re

def siteyi_guncelle():
    # 1. data.json dosyasındaki güncel kazancı oku
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        guncel_kazanc = data['toplam_kazanc']

    # 2. script.js dosyasını oku
    with open('script.js', 'r', encoding='utf-8') as f:
        js_content = f.read()

    # 3. JavaScript içindeki 'const suAnkiKazanc = ...' kısmını bul ve değiştir
    # Bu aşama manuel düzenleme hatasını sıfıra indirir.
    yeni_js_content = re.sub(r'const suAnkiKazanc = \d+;', f'const suAnkiKazanc = {int(guncel_kazanc)};', js_content)

    # 4. Güncellenmiş kodu script.js dosyasına geri yaz
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(yeni_js_content)

    print(f"✅ Köprü kuruldu! Web sitesi verisi {guncel_kazanc} TL olarak güncellendi.")

if __name__ == "__main__":
    siteyi_guncelle()