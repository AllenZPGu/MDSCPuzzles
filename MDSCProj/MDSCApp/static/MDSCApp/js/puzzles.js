// Set the date we're counting down to
var countDownDate = new Date("Jun 27, 2022 09:00:00").getTime();

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  var p1c = document.getElementById("puzzle-btn1-countdown");
  var p2c = document.getElementById("puzzle-btn2-countdown");
  var p3c = document.getElementById("puzzle-btn3-countdown");
  var p4c = document.getElementById("puzzle-btn4-countdown");

  // Display the result in the element with id="demo"
  if (!!p1c) {if (days >= 0) {
    p1c.innerHTML = "Released in <br>" + days + "d " + hours + "h " + minutes + "m " + seconds + "s ";
  } else {
    p1c.innerHTML = "Released NOW<br>Please refresh";
  }}
  if (!!p2c) {if (days+1 >= 0) {
    p2c.innerHTML = "Released in <br>" + (days+1) + "d " + hours + "h " + minutes + "m " + seconds + "s ";
  } else {
    p2c.innerHTML = "Released NOW<br>Please refresh";
  }}
  if (!!p3c) {if (days+2 >= 0) {
    p3c.innerHTML = "Released in <br>" + (days+2) + "d " + hours + "h " + minutes + "m " + seconds + "s ";
  } else {
    p3c.innerHTML = "Released NOW<br>Please refresh";
  }}
  if (!!p4c) {if (days+3 >= 0) {
    p4c.innerHTML = "Released in <br>" + (days+3) + "d " + hours + "h " + minutes + "m " + seconds + "s ";
  } else {
    p4c.innerHTML = "Released NOW<br>Please refresh";
  }}
}, 200);

var changeHeight = function(){
  var maxH = 0;
  for (i = 1; i <= 4; i++) {
    var x = getComputedStyle(document.getElementById(`puzzle-btn${i}`)).height;
    var y = parseFloat(x.substring(0, x.length-2));
    if (y > maxH) {maxH = y;}
  }
  for (i = 1; i <= 4; i++) {
    document.getElementById(`puzzle-btn${i}`).style.height = maxH+'px';
  }
}

changeHeight();