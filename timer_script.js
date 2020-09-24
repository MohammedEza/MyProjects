
function getTimeRemaining(endtime = new Date()) { 
	 var t = Date.parse(endtime) - Date.parse(new Date());
	 var seconds = Math.floor((t/1000)%60);
	 var minutes = Math.floor(t/(1000*60)%60);
	 var hours = Math.floor(t/(1000*60*60)%24);
	 var days = Math.floor(t/(1000*60*60*24));
  

	return {
		"total"  : t,
		"days"   : days,
		"hours"  : hours,
		"minutes": minutes,
		"seconds":seconds   
            };
    }

function initializeClock (id,endtime) {
	var clock = document.getElementById(id);
	var daysSpan = clock.querySelector('.days');
	var hoursSpan = clock.querySelector('.hours');
	var minutesSpan = clock.querySelector('.minutes');
	var secondsSpan = clock.querySelector('.seconds');

	function updateClock() {
		var p = getTimeRemaining(endtime);
		daysSpan.innerHTML = p.days;
		hoursSpan.innerHTML = p.hours;
		//hoursSpan.innerHTML = ('0' + p.hours).slice(-2);
		console.log(p.hours);
		minutesSpan.innerHTML = p.minutes;
		secondsSpan.innerHTML = p.seconds;
	if (p.total <= 0) {
		
		clearInterval(timeinterval);
		alert("TIME UP!!")
		buttoncl.textContent = "Set New timer"
		}
	}
	updateClock();
	var timeinterval = setInterval(updateClock,1000);

} 
	
function Start(){
	buttoncl.textContent = "Ticking......"
	
 var udays = window.prompt("Please enter number of days");
 var uhours = window.prompt("Please enter number of hours");
 var uminutes = window.prompt("Please enter number of minutes");
 var useconds = window.prompt("Please enter number of seconds");
var calcms = ((udays*24*60*60*1000)+(uhours*60*60*1000)+(uminutes*60*1000)+(useconds*1000));
//console.log(calcms);
var deadline = new Date(Date.parse(new Date())+ calcms)
initializeClock('clockdiv', deadline);
}
var buttoncl = document.querySelector("button")
buttoncl.onclick = function(){Start();}

