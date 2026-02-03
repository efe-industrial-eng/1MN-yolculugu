const startDate = new Date("2026-02-02");
const diffInDays = Math.floor((new Date() - startDate) / (1000 * 60 * 60 * 24)) + 1;
document.getElementById('day-counter').innerText = diffInDays;