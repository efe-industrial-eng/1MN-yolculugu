import json
import re
import subprocess
from datetime import datetime

def guncelle():
    # 1. VERİ GİRİŞİ VE TARİH HESABI
    baslangic_tarihi = datetime(2026, 2, 2)
    bugun = datetime.now()
    gecen_gun = (bugun - baslangic_tarihi).days + 1
    
    yeni_kazanc = float(input(f"💰 {gecen_gun}. Gün Kazancını Gir (TL): "))
    
    # 2. JSON GÜNCELLEME
    with open('data.json', 'r+') as f:
        data = json.load(f)
        data['toplam_kazanc'] += yeni_kazanc
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        guncel_total = data['toplam_kazanc']

    # 3. MÜHENDİSLİK ANALİZİ (PROJEKSİYON)
    hedef = 1000000
    gunluk_ortalam = guncel_total / gecen_gun
    kalan_borc = hedef - guncel_total
    tahmini_gun = int(kalan_borc / gunluk_ortalam) if gunluk_ortalam > 0 else 0

    # 4. KÖPRÜ (script.js Güncelleme)
    with open('script.js', 'r', encoding='utf-8') as f:
        js_content = f.read()
    yeni_js = re.sub(r'const suAnkiKazanc = \d+;', f'const suAnkiKazanc = {int(guncel_total)};', js_content)
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(yeni_js)

    # 5. OTOMATİK YAYIN (Git Push)
    print(f"\n📊 ANALİZ RAPORU:")
    print(f"---------------------------")
    print(f"Günlük Ortalama: {gunluk_ortalam:.2f} TL")
    print(f"Bu hızla hedefe {tahmini_gun} gün (~{tahmini_gun//365} yıl) sonra ulaşacaksın.")
    print(f"---------------------------")
    
    print("\n🚀 Dünya vitrini güncelleniyor...")
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"update: {gecen_gun}. gun sonunda {guncel_total} TL"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    guncelle()