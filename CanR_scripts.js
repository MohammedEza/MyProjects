
var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');

var canvasx = $(canvas).offset().left;
var canvasy = $(canvas).offset().top;
var last_mousex = last_mousey = 0;
var mousex = mousey = 0;
var mousedown = false;
var width;
var height;


$(canvas).on('mousedown', function(e) {
    last_mousex = parseInt(e.clientX-canvasx);
	last_mousey = parseInt(e.clientY-canvasy);
    mousedown = true;
    
});


$(canvas).on('mouseup', function(e) {
    endx = parseInt(e.clientX-canvasx);
    endy = parseInt(e.clientY-canvasy)
    ctx.fillText(" ("+endx+", "+endy+")", endx+5, endy);
    ctx.fillText(" ("+(last_mousex+width)+", "+last_mousey+")", last_mousex-10+(width), last_mousey-14);
    
    ctx.fillText(" ("+last_mousex+", "+(last_mousey+height)+")", last_mousex-5 , last_mousey+height+15);
    mousedown = false;
});


$(canvas).on('mousemove', function(e) {
    mousex = parseInt(e.clientX-canvasx);
	mousey = parseInt(e.clientY-canvasy);
    if(mousedown) {
        ctx.clearRect(0,0,canvas.width,canvas.height); //clear canvas
        ctx.beginPath();
        ctx.fillText(" ("+last_mousex+", "+last_mousey+")", last_mousex-10, last_mousey-15);
        width = mousex-last_mousex;
        height = mousey-last_mousey;
        ctx.rect(last_mousex,last_mousey,width,height);
        ctx.strokeStyle = 'blue';
        ctx.lineWidth = 5;
        ctx.stroke();
    }
    
    $('#Message').text(' Start:    ('+last_mousex+', '+last_mousey+ ')     End:    ('+endx+', '+endy+ ') Width: '+width+' Heigth: '+height);
});