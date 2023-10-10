document.addEventListener('DOMContentLoaded', () => {
    const hello = document.getElementById('hello');

    function mostrarData(value) {
        hello.textContent = value;
    };

    let request = fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(res => res.json())
        .then(data => mostrarData(data.hello))
        .catch(e => console.log(e));
});