$.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    success: (data)=> {
        $.each(data.results, (i, movie)=> {
            $('#list_movies').append(`<li>${movie.title}</li>`);
        })
    },
    error: (e)=> {
        console.log(`Status: ${e.statusText}`);
        console.log(`Detalles del error: ${e.responseText}`);
    }
});
// console.log(data.results[0].title);