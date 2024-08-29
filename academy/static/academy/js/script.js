const wrapper = document.querySelector('.wrapper');
const btnPopup = document.querySelector('.btnLogin-popup');

btnPopup.addEventListener('click', (event) => {
    event.preventDefault();
    wrapper.classList.toggle('active-popup');
});
