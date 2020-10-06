
// getting elements by id
var menu = document.getElementById('menu');
var nav = document.getElementById('nav');
var exit = document.getElementById('exit');

// Open menu when hamburger is clicked
menu.addEventListener('click', (e) => {
  nav.classList.toggle('hide-mobile');
  e.preventDefault();
});

// Close menu when X is clicked
exit.addEventListener('click', (e) => {
  nav.classList.add('hide-mobile');
  e.preventDefault();
});