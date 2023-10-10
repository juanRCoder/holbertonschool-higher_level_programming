document.addEventListener('DOMContentLoaded', () => {
    const selectLang = document.getElementById("language_code");
    const btnlang = document.getElementById("btn_translate");
    const hello = document.getElementById("hello");

    btnlang.addEventListener('click', ()=> {
        let langCode =  selectLang.value;
        requestFETCH(langCode);
    });

    function requestFETCH(langCode) {
        let URL = `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`;

        function mostrarData(langHello) {
            hello.textContent = langHello;
        };

        fetch(URL)
            .then(res => res.json())
            .then(data => mostrarData(data.hello))
            .catch(e => console.log(e));
    }
});