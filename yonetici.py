import json
import re
import subprocess # Terminal komutlarını çalıştırmak için

def guncelle():
    # 1. VERİ GİRİŞİ
    yeni_kazanc = float(input("💰 Bugün kaç TL kazandın? "))
    
    # 2. JSON GÜNCELLEME
    with open('data.json', 'r+') as f:
        data = json.load(f)
        data['toplam_kazanc'] += yeni_kazanc
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        guncel_toplam = data['toplam_kazanc']

    # 3. KÖPRÜ (JS GÜNCELLEME)
    with open('script.js', 'r', encoding='utf-8') as f:
        js_content = f.read()
    yeni_js = re.sub(r'const suAnkiKazanc = \d+;', f'const suAnkiKazanc = {int(guncel_toplam)};', js_content)
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(yeni_js)

    # 4. OTOMATİK YAYIN (GIT PUSH)
    print("\n🚀 Veriler işlendi, dünya vitrini güncelleniyor...")
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", f"update: total earnings reached {guncel_toplam} TL"],
        ["git", "push"]
    ]
    for cmd in commands:
        subprocess.run(cmd)

    print(f"\n✅ BAŞARILI! Yeni toplam: {guncel_toplam} TL. Siten birkaç dakika içinde güncellenecek.")

if __name__ == "__main__":
    guncelle()