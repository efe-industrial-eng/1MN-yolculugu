import json
import re
import subprocess
from datetime import datetime

def guncelle():
    baslangic = datetime(2026, 2, 2)
    bugun = datetime.now()
    bugun_str = bugun.strftime("%Y-%m-%d")
    gecen_gun = (bugun - baslangic).days + 1
    
    yeni = float(input(f"💰 {gecen_gun}. Gün Kazancını Gir (TL): "))
    
    # 1. JSON HAFIZASINI GÜNCELLE
    with open('data.json', 'r+') as f:
        data = json.load(f)
        data['toplam_kazanc'] += yeni
        # Yeni kaydı listeye ekle
        data['gunluk_kayitlar'].append({"tarih": bugun_str, "kazanc": yeni})
        
        f.seek(0); json.dump(data, f, indent=4); f.truncate()
        total = data['toplam_kazanc']

    # 2. ANALİZ (Mühendislik Projeksiyonu)
    avg = round(total / gecen_gun, 2)
    est = int((1000000 - total) / avg) if avg > 0 else 0

    # 3. KÖPRÜ (JavaScript Enjeksiyonu)
    with open('script.js', 'r', encoding='utf-8') as f:
        js = f.read()
    
    js = re.sub(r'const suAnkiKazanc = \d+;', f'const suAnkiKazanc = {int(total)};', js)
    js = re.sub(r'const gunlukOrtalama = [\d.]+;', f'const gunlukOrtalama = {avg};', js)
    js = re.sub(r'const kalanGun = \d+;', f'const kalanGun = {est};', js)

    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js)

    # 4. OTOMATİK YAYIN
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"Log: {bugun_str} tarihinde {yeni} TL eklendi"])
    subprocess.run(["git", "push"])
    print(f"\n✅ Veri günlüğe kaydedildi ve siteye fırlatıldı! Hedefe {est} gün kaldı.")

if __name__ == "__main__":
    guncelle()