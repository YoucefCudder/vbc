const moreTextEl = document.getElementById('more-text');
const toggleBtnEl = document.getElementById('toggle-btn');
const hideBtnEl = document.getElementById('hide-btn');

toggleBtnEl.addEventListener('click', () => {
    moreTextEl.classList.toggle('hidden');
    toggleBtnEl.classList.toggle('hidden');
    hideBtnEl.classList.toggle('hidden');
});

hideBtnEl.addEventListener('click', () => {
    moreTextEl.classList.toggle('hidden');
    toggleBtnEl.classList.toggle('hidden');
    hideBtnEl.classList.toggle('hidden');
});




