$.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    method: 'GET',
    dataType: 'json',
    success: (data)=> {
        $('#character').text(data.name);
    },
    error: (e)=> {
        console.log(`Status: ${e.statusText}`);
        console.log(`Detalles del error: ${e.responseText}`);
    }
});