$(document).ready(function() {
    $('#language_code').keypress((e) => {
        request();
    });

    $('#btn_translate').click(() => {
        request();
    });
 
    function request(){
        let langCode = $('#language_code').val();
        $.ajax({
            url: `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`,
            method: 'GET',
            dataType: 'json'
        }).done((data) => {
            $('#hello').text(data.hello);
        }).fail((error) => {
            console.log(error);
        });  
    };
});