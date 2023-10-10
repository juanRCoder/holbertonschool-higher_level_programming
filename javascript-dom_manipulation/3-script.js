const header = document.querySelector('.green');
const btnHeader = document.getElementById('toggle_header');

btnHeader.addEventListener('click',()=>{
    if (header.className == 'green') {
        header.className = 'red';
    } else {
        header.className = 'green';
    }
});