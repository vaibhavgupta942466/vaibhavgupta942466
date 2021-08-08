var player1 = prompt("Player One: Enter Your Name: You Will Be Blue")
var player1color = "rgb(86, 151, 255)"

var player2 = prompt("Player two: Enter Your Name: You Will Be")
var player2color = "rgb(237, 45, 73)"

var game_on = true;
var table = $("table tr"); 

function reportwin(rownum, colnum){
    console.log("You won starting at this row,col");
    console.log(rownum);
    console.log(colnum);
}

function changecolor(rowindex,colindex,color){
    return table.eq(rowindex).find('td').eq(colindex).find('button').css('background-color',color);
}

function returncolor(rowindex,colindex){
    return table.eq(rowindex).find('td').eq(colindex).find('button').css('background-color')
}

function checkbottom(colindex){
    var colorreport = returncolor(5,colindex);
    for(var row = 5;row > -1;row--){
        colorreport = returncolor(row,colindex);
        if(colorreport === 'rgb(128, 128, 128)'){
            return row;
        }
    }
}

function colormatchcheck(one, two, three, four){
    return (one===two && one === three && one === four && one !== 'rgb(128, 128, 128)' && one !== undefined)
}

function getRandomColor(){
    var letters = "0123456789ABCDEF";
    var color = '#';
    for (var i=0;i<6;i++){
        color += letters[Math.floor(Math.random()*16)];
    }
    return color;
}

function changetablecolor(){
    colorinput = getRandomColor();
    $('td').css('background-color',colorinput)
}

setInterval("changetablecolor()",500);

function checkhorizontalwin(){
    for(var row = 0; row < 6; row++){
        for(var col = 0; col < 4; col++){
            if(colormatchcheck(returncolor(row,col), returncolor(row,col+1), returncolor(row,col+2), returncolor(row,col+3))){
               reportwin(row,col);
               console.log('Horizontal');
               return true;
            }else{
                continue;
            }
        }
        
    }
}

function checkverticalwin(){
    for(var col =0; col < 7; col++){
        for(var row =0; row < 3; row++){
            if(colormatchcheck(returncolor(row,col), returncolor(row+1,col), returncolor(row+2,col), returncolor(row+3,col))){
                reportwin(row,col);
                console.log('Vertical');
                return true;
            }else{
                continue;
            }
        }
    }
}

function checkdiagonalwin(){
    for(var col =0; col < 5; col++){
        for(var row =0; row < 7; row++){
            if(colormatchcheck(returncolor(row,col), returncolor(row+1,col+1), returncolor(row+2,col+2), returncolor(row+3,col+3))){
                reportwin(row,col);
                console.log('diagonaldown');
                return true;
            }else if(colormatchcheck(returncolor(row,col), returncolor(row-1,col+1), returncolor(row-2,col+2), returncolor(row-3,col+3))){
                reportwin(row,col);
                console.log('diagonalup');
                return true;
            }else{
                continue;
            }
        }
    }
}

function gameend(winningplayer){
    for(var col = 0; col < 7; col++){
        for(var row =0; row <6; row++){
            $('h3').fadeOut('fast');
            $('h2').fadeOut('fast');
            $('h1').text(winningplayer+" has won! Refresh your browser to play again!").css('font-size','50px')
            $('table').fadeOut('fast');
        }
    }
}

var currentplayer = 1;
var currentname = player1;
var currentcolor = player1color;

$('h3').text(player1+' its your turn, please pick a column to drop your blue chip');

$('.center button').on('click', function(){
    var col = $(this).closest('td').index();
    var bottomavail = checkbottom(col);
    changecolor(bottomavail,col,currentcolor);
    if(checkhorizontalwin() || checkverticalwin() || checkdiagonalwin()){
        gameend(currentname);
    }

    currentplayer = currentplayer * -1;

    if(currentplayer === 1){
        currentname = player1;
        $('h3').text(currentname+' it is your turn.')
        currentcolor = player1color;
    }else{
        currentname = player2;
        $('h3').text(currentname+' it is your turn.')
        currentcolor = player2color;
    }
})