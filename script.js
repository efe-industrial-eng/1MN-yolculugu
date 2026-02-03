// Sayfa tamamen yüklendiğinde çalışmasını garanti et
document.addEventListener('DOMContentLoaded', function() {
    const startDate = new Date("2026-02-02");
    const today = new Date();
    
    // Gün hesaplama
    const diffInMs = today - startDate;
    const diffInDays = Math.floor(diffInMs / (1000 * 60 * 60 * 24)) + 1;
    
    // Ekranda 'day-counter' id'li yeri bul ve güncelle
    const counterElement = document.getElementById('day-counter');
    if (counterElement) {
        counterElement.innerText = diffInDays;
        console.log("Sayaç güncellendi: " + diffInDays);
    } else {
        console.log("Hata: 'day-counter' elementi bulunamadı!");
    }
});