const btnItem = document.getElementById('update_header');
let header = document.querySelector('header');

btnItem.addEventListener('click', ()=>{
    header.textContent = 'New Header!!!';
});