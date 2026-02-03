document.addEventListener('DOMContentLoaded', function() {
    const startDate = new Date("2026-02-02");
    const diffInDays = Math.floor((new Date() - startDate) / (1000 * 60 * 60 * 24)) + 1;
    const el = document.getElementById('day-counter');
    if (el) el.innerText = diffInDays;
});