document.addEventListener('DOMContentLoaded', function() {
    const startDate = new Date("2026-02-02");
    const diffInDays = Math.floor((new Date() - startDate) / (1000 * 60 * 60 * 24)) + 1;
    
    // VERİLER (yonetici.py bunları otomatik günceller)
    const suAnkiKazanc = 450; 
    const gunlukOrtalama = 150.0;
    const kalanGun = 6663;
    const grafikEtiketleri = ["2026-02-02", "2026-02-03", "2026-02-04", "2026-02-04", "2026-02-04", "2026-02-04"]; 
    const grafikVerileri = [50, 100, 50, 50.0, 50.0, 50.0]; 

    const hedefTarih = new Date();
    hedefTarih.setDate(hedefTarih.getDate() + kalanGun);
    const hedefTarihStr = hedefTarih.toLocaleDateString('tr-TR', { year: 'numeric', month: 'long', day: 'numeric' });

    // Rakamları Yazdır
    document.getElementById('day-counter').innerText = diffInDays;
    document.getElementById('header-day').innerText = "DAY " + diffInDays;
    document.getElementById('progress-fill').style.width = ((suAnkiKazanc / 1000000) * 100) + "%";
    document.getElementById('progress-percent').innerText = ((suAnkiKazanc / 1000000) * 100).toFixed(4);
    document.getElementById('avg-earning').innerText = gunlukOrtalama;
    document.getElementById('est-days').innerText = kalanGun;
    document.getElementById('target-date').innerText = hedefTarihStr;

    // GRAFİK AYARLARI (Chart.js)
    const ctx = document.getElementById('earningChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: grafikEtiketleri,
            datasets: [{
                label: 'Günlük Kazanç (TL)',
                data: grafikVerileri,
                borderColor: '#ffcc00', // Senin o meşhur altın sarın
                backgroundColor: 'rgba(255, 204, 0, 0.1)',
                borderWidth: 3,
                tension: 0.4,
                fill: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
                y: { beginAtZero: true, grid: { color: '#333' }, ticks: { color: '#888' } },
                x: { grid: { display: false }, ticks: { color: '#888' } }
            }
        }
    });
});