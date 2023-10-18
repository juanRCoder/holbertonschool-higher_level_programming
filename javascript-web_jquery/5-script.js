$('#add_item').click(()=>{
    const newLI = $('<li>', {
        text: 'Item'
    });
    $('.my_list').append(newLI);
});