const countdown = document.getElementById("countdown");

let seconds = 5;
for (let i = seconds; i > 0; i--) {
  setTimeout(function () {
    countdown.innerHTML = i;
  }, (seconds - i) * 1000);
}

setTimeout(function () {
  window.location.href = "\index";
}, seconds * 1000);
