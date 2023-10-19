$(document).ready(function() {
    function count() {
        console.log('elements li: ' + $('li').length);
    }
    count();
    $('#add_item').click(()=> {
        $('.my_list').append('<li>Item</li>');
        count();
    });
    $('#remove_item').click(()=> {
        $('.my_list li:last').remove();
        count();
    });
    $('#clear_list').click(()=> {
        $('.my_list').empty();
        count();
    });
});