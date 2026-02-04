document.addEventListener('DOMContentLoaded', function() {
    // 1. TARİH HESAPLAMA (Otomatik Gün Sayacı)
    const startDate = new Date("2026-02-02");
    const diffInDays = Math.floor((new Date() - startDate) / (1000 * 60 * 60 * 24)) + 1;
    
    // 2. HTML ELEMANLARINI YAKALAMA (Dün tanımladığımız ID'ler)
    const dayCounter = document.getElementById('day-counter');
    const headerDay = document.getElementById('header-day');
    const progressFill = document.getElementById('progress-fill');
    const progressPercent = document.getElementById('progress-percent');

    // 3. VERİLERİ SAYFAYA ENJEKTE ETME
    if (dayCounter) dayCounter.innerText = diffInDays;
    if (headerDay) headerDay.innerText = "DAY " + diffInDays;

    // 4. İLERLEME HESABI (Mühendislik Formülü)
    const toplamHedef = 1000000;
    const suAnkiKazanc = 250; // Python verisi buraya akacak
    const yuzde = (suAnkiKazanc / toplamHedef) * 100;

    // 5. GÖRSEL GÜNCELLEME
    if (progressFill) progressFill.style.width = yuzde + "%";
    if (progressPercent) progressPercent.innerText = yuzde.toFixed(4);
});