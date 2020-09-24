window.addEventListener('load', function () {
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");

    canvas.height = 500;
    canvas.width = 1000;
    let painting = false;
    function startpos(e) {
        painting = true;
       console.log("START!!! X=" + e.clientX)
        console.log("Y=" + e.clientY)
        var points = document.getElementById("start");
        points.textContent = e.clientX + ',' + e.clientY;
    }
    function finishpos(e){
        painting = false;
        console.log("END!! X=" + e.clientX);
        console.log("Y=" + e.clientY);
        var points = document.getElementById("end");
        points.textContent = e.clientX + ',' + e.clientY;
        ctx.beginPath();
        
    }
    function draw(e) {
        if (!painting) return;
        ctx.lineWidth = 5;
        ctx.lineCap = "round";
        ctx.strokeStyle ="blue";
        ctx.lineTo(e.clientX, e.clientY);
        ctx.stroke();
    
    }
   
    canvas.addEventListener("mousedown", startpos);
    canvas.addEventListener("mouseup", finishpos);
    canvas.addEventListener("mousemove", draw);
});