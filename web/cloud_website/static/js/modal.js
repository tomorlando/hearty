
// get modal elements by id
var modal = document.getElementById('simple-modal');
var button = document.getElementById('submit')
var form_submit = document.getElementById('form-submit');
var close_btn = document.getElementsByClassName('close-btn')[0];

// listen for click
form_submit.addEventListener('submit', openModal);
close_btn.addEventListener('click', closeModal);
button.addEventListener('click', colourBtn);
//window.addEventListener('click', clickOutside);

// functions for use
function openModal(e){
  e.preventDefault();
  modal.style.display = 'block';
  
}

function closeModal(){
  modal.style.display = 'none'
  button.style.background = '#820041';
}

function colourBtn(){
  button.style.background = '#FFF';
}

//function clickOutside(e){
//  if(e.target == modal){
//    modal.style.display = 'none';
//  } 
//}
