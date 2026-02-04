document.addEventListener('DOMContentLoaded', function() {
    // 1. TARİH HESAPLAMA (Yolculuk Başlangıcı: 2 Şubat 2026)
    const startDate = new Date("2026-02-02");
    const diffInDays = Math.floor((new Date() - startDate) / (1000 * 60 * 60 * 24)) + 1;
    
    // 2. DEĞİŞKENLER (Bu rakamları yonetici.py otomatik güncelleyecektir)
    const suAnkiKazanc = 400; // Örnek toplam kazanç
    const gunlukOrtalama = 133.33; // Örnek ortalama
    const kalanGun = 7497; // Örnek kalan gün

    // 3. İLERLEME HESABI
    const hedef = 1000000;
    const yuzde = (suAnkiKazanc / hedef) * 100;

    // 4. HEDEF TARİH HESAPLAMA (Mühendislik Projeksiyonu)
    const hedefTarih = new Date();
    hedefTarih.setDate(hedefTarih.getDate() + kalanGun);
    const secenekler = { year: 'numeric', month: 'long', day: 'numeric' };
    const hedefTarihStr = hedefTarih.toLocaleDateString('tr-TR', secenekler);

    // 5. SAYFAYA VERİ ENJEKSİYONU (DOM Updates)
    if(document.getElementById('day-counter')) document.getElementById('day-counter').innerText = diffInDays;
    if(document.getElementById('header-day')) document.getElementById('header-day').innerText = "DAY " + diffInDays;
    if(document.getElementById('progress-fill')) document.getElementById('progress-fill').style.width = yuzde + "%";
    if(document.getElementById('progress-percent')) document.getElementById('progress-percent').innerText = yuzde.toFixed(4);
    
    // Analiz Paneli Verileri
    if(document.getElementById('avg-earning')) document.getElementById('avg-earning').innerText = gunlukOrtalama;
    if(document.getElementById('est-days')) document.getElementById('est-days').innerText = kalanGun;
    if(document.getElementById('target-date')) document.getElementById('target-date').innerText = hedefTarihStr;
});