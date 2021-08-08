$('h1').click(function(){
    //console.log('click')
    $(this).text('I was changed')
})

$('li').click(function(){
    console.log('any list item clicked');
})

$('input').eq(0).keypress(function(){
    $('h3').toggleClass('turnBlue')
})

$('input').eq(0).keypress(function(event){
    if (event.which === 13) {
        $('h3').toggleClass('turnRed')
    }
})

$('h1').on('mouseenter',function(){
    $(this).toggleClass('turnBlue')
})

$('input').eq(1).on("click",function() {
    $('.container').fadeOut(3000);
})
