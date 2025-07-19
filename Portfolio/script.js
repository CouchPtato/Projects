
const openBtn = document.getElementById('menu-toggle');
const closeBtn = document.getElementById('close-btn');
const overlay = document.getElementById('overlay');

openBtn.addEventListener('click', () => {
overlay.style.width = "100%";
});

closeBtn.addEventListener('click', () => {
overlay.style.width = "0";
});
