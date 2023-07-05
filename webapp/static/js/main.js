// script.js

// Add JavaScript functionality here

// Example: Change the color of the heading on button click
const button = document.getElementById('changeColorButton');
const heading = document.querySelector('h1');

button.addEventListener('click', () => {
  heading.style.color = 'blue';
});

window.addEventListener('scroll', function() {
  var scrollingDiv = document.getElementById('scrollingDiv');
  var scrollTop = window.pageYOffset || document.documentElement.scrollTop;

  scrollingDiv.style.top = (100 - scrollTop / 10) + 'px';
});
