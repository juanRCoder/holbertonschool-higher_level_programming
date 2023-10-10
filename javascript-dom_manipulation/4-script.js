const btnItem = document.getElementById('add_item');
const ul = document.querySelector('.my_list');

btnItem.addEventListener('click', ()=>{
    let newLI = document.createElement('LI');
    newLI.textContent = 'Item';
    ul.appendChild(newLI);
});