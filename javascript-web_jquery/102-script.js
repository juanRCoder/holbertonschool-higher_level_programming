$(document).ready(function() {
    $('#btn_translate').click(() => {
        let langCode = $('#language_code').val();
        $.ajax({
            url: `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`,
            method: 'GET',
            dataType: 'json',
            success: (data) => {
                $('#hello').text(data.hello);
            },
            error: (e) => {
                console.log(`Status: ${e.statusText}`);
                console.log(`Detalles del error: ${e.responseText}`);
            }
        }); 
    });
});