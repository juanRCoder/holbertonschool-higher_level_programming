document.addEventListener('DOMContentLoaded', () => {
    const ul = document.querySelector('.my_list');
    
    //Funcion extra para contar la cantidad de elementos 'LI'
    function countItems() {
        let lis = ul.getElementsByTagName('li');
        console.log(`items: ${lis.length}`);
    };

    countItems();

    document.body.addEventListener('click', (e) => {
        if (e.target.getAttribute('id') === 'add_item') {
            let newLi = document.createElement('li');
            newLi.textContent = 'Item';

            ul.appendChild(newLi);
            countItems();

        } else if (e.target.getAttribute('id') === 'remove_item') {
            let lis = ul.getElementsByTagName('li');

            if (lis.length > 0) {
                ul.removeChild(lis[lis.length - 1]);
                countItems();
            }

        } else if (e.target.getAttribute('id') === 'clear_list') {
            ul.textContent = '';
            countItems();
        }
    });
});
