const name_character = document.getElementById('character');

function mostrarData(name) {
    name_character.textContent = name;
}

//Solicitud hacia la API swapi
let request = fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(res => res.json())
    .then(data => mostrarData(data.name))
    .catch(e => console.log(e));