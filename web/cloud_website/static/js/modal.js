
// get modal elements by id and class
var modal = document.getElementById('simple-modal');
var button = document.getElementById('submit')
var close_btn = document.getElementsByClassName('close-btn')[0];

// Close modal when exit button is clicked 
close_btn.addEventListener('click', () => {
  modal.style.display = 'none';
  button.style.background = '#820041';
});

// Blank out button when modal opens
button.addEventListener('click', () => {
  button.style.background = '#FFF';
});