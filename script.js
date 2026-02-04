document.addEventListener('DOMContentLoaded', function() {
    const startDate = new Date("2026-02-02");
    const diffInDays = Math.floor((new Date() - startDate) / (1000 * 60 * 60 * 24)) + 1;
    
    // DATA (updated by yonetici.py)
    const suAnkiKazanc = 1250; 
    const gunlukOrtalama = 416.67;
    const kalanGun = 2396;
    const grafikEtiketleri = ["2026-02-02", "2026-02-03", "2026-02-04", "2026-02-04", "2026-02-04", "2026-02-04", "2026-02-04", "2026-02-04", "2026-02-04", "2026-02-04"]; 
    const grafikVerileri = [50, 100, 50, 50.0, 50.0, 50.0, 200.0, 200.0, 200.0, 200.0]; 

    // Performance: above daily average today?
    const sonKazanc = grafikVerileri[grafikVerileri.length - 1];
    const isHighPerformance = sonKazanc >= gunlukOrtalama;
    const mainColor = isHighPerformance ? '#fff000' : '#ffcc00';
    const shadowBlur = isHighPerformance ? 15 : 0;

    // Page updates
    const hedefTarih = new Date();
    hedefTarih.setDate(hedefTarih.getDate() + kalanGun);
    document.getElementById('day-counter').innerText = diffInDays;
    document.getElementById('header-day').innerText = "DAY " + diffInDays + " in the Journey";
    document.getElementById('progress-fill').style.width = ((suAnkiKazanc / 1000000) * 100) + "%";
    document.getElementById('progress-percent').innerText = ((suAnkiKazanc / 1000000) * 100).toFixed(4);
    document.getElementById('avg-earning').innerText = gunlukOrtalama;
    document.getElementById('est-days').innerText = kalanGun;
    document.getElementById('target-date').innerText = hedefTarih.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });

    // Success badges (toplam_kazanc milestones)
    const milestones = [
        { threshold: 100, label: 'First Victory 🏆' },
        { threshold: 300, label: 'System Established ⚙️' },
        { threshold: 500, label: 'Accelerating 🚀' }
    ];
    const unlocked = milestones.filter(m => suAnkiKazanc >= m.threshold);
    const container = document.getElementById('badges-container');
    container.innerHTML = '';
    unlocked.forEach(function (m) {
        const badge = document.createElement('span');
        badge.className = 'badge';
        badge.textContent = m.label;
        badge.setAttribute('title', m.threshold + ' TL milestone reached!');
        container.appendChild(badge);
    });

    // Chart
    const ctx = document.getElementById('earningChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: grafikEtiketleri,
            datasets: [{
                label: 'Daily Earnings (TL)',
                data: grafikVerileri,
                borderColor: mainColor,
                backgroundColor: 'rgba(255, 204, 0, 0.1)',
                borderWidth: 4,
                tension: 0.4,
                pointBackgroundColor: mainColor,
                pointRadius: isHighPerformance ? 6 : 4,
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