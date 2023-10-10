const ul = document.getElementById('list_movies');

function mostrarData(titles) {
    titles.forEach(title => {
        let li = document.createElement('LI');
        li.textContent = title.title;
        ul.appendChild(li);
    });
};

//Solicitud hacia la API swapi
let request = fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(res => res.json())
    .then(data => mostrarData(data.results))
    .catch(e => console.log(e));

//data.results[1].title --> obtener 1 titulo