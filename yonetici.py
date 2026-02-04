import json
import re
import subprocess
from datetime import datetime

def guncelle():
    # 1. Date and day count
    baslangic = datetime(2026, 2, 2)
    bugun = datetime.now()
    bugun_str = bugun.strftime("%Y-%m-%d")
    gecen_gun = (bugun - baslangic).days + 1

    # 2. User input
    yeni = float(input(f"💰 Enter earnings for Day {gecen_gun} (TL): "))

    # 3. Update JSON (persistence)
    with open('data.json', 'r+') as f:
        data = json.load(f)
        data['toplam_kazanc'] += yeni
        data['gunluk_kayitlar'].append({"tarih": bugun_str, "kazanc": yeni})
        f.seek(0); json.dump(data, f, indent=4); f.truncate()
        total = data['toplam_kazanc']

    # 4. Analytics
    avg = round(total / gecen_gun, 2)
    est = int((1000000 - total) / avg) if avg > 0 else 0
    labels = [log['tarih'] for log in data['gunluk_kayitlar']]
    values = [log['kazanc'] for log in data['gunluk_kayitlar']]

    # 5. Inject into script.js
    with open('script.js', 'r', encoding='utf-8') as f:
        js = f.read()
    
    # Update all dynamic fields
    js = re.sub(r'const suAnkiKazanc = \d+;', f'const suAnkiKazanc = {int(total)};', js)
    js = re.sub(r'const gunlukOrtalama = [\d.]+;', f'const gunlukOrtalama = {avg};', js)
    js = re.sub(r'const kalanGun = \d+;', f'const kalanGun = {est};', js)
    js = re.sub(r'const grafikEtiketleri = \[.*\];', f'const grafikEtiketleri = {json.dumps(labels)};', js)
    js = re.sub(r'const grafikVerileri = \[.*\];', f'const grafikVerileri = {json.dumps(values)};', js)

    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js)

    # 6. Deploy (Git push)
    print(f"\n🚀 Analysis complete. Pushing chart and data to Vercel...")
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"Chart Update: Day {gecen_gun}"])
    subprocess.run(["git", "push"])
    print(f"\n✅ Done! {est} days left to goal.")

if __name__ == "__main__":
    guncelle()