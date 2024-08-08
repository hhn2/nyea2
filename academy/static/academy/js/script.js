const wrapper = document.querySelector('.wrapper');
const btnPopup = document.querySelector('.btnLogin-popup');

btnPopup.addEventListener('click', () => {
    wrapper.classList.toggle('active-popup');
});
