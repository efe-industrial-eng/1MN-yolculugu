document.addEventListener('DOMContentLoaded', function() {
    const startDate = new Date("2026-02-02");
    const diffInDays = Math.floor((new Date() - startDate) / (1000 * 60 * 60 * 24)) + 1;
    
    // DİKKAT: yonetici.py bu rakamları otomatik olarak değiştirecek
    const suAnkiKazanc = 350; 
    const gunlukOrtalama = 116.67;
    const kalanGun = 8568;

    const hedef = 1000000;
    const yuzde = (suAnkiKazanc / hedef) * 100;

    // Temel Bilgiler
    if(document.getElementById('day-counter')) document.getElementById('day-counter').innerText = diffInDays;
    if(document.getElementById('header-day')) document.getElementById('header-day').innerText = "DAY " + diffInDays;
    
    // İlerleme Barı
    if(document.getElementById('progress-fill')) document.getElementById('progress-fill').style.width = yuzde + "%";
    if(document.getElementById('progress-percent')) document.getElementById('progress-percent').innerText = yuzde.toFixed(4);
    
    // YENİ: Analiz Raporu Verileri
    if(document.getElementById('avg-earning')) document.getElementById('avg-earning').innerText = gunlukOrtalama;
    if(document.getElementById('est-days')) document.getElementById('est-days').innerText = kalanGun;
});