$(document).ready(function() {
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        method: 'GET',
        dataType: 'json',
        success: (data) => {
            $('#hello').text(data.hello)
        },
        error: (e) => {
            console.log(`Status: ${e.statusText}`);
            console.log(`Detalles del error: ${e.responseText}`);
        }
    });
});