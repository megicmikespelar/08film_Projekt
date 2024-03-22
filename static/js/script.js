let mybutton = document.getElementById("myBtn");

function getScrollPosition() {
  return Math.max(window.body ? window.body.scrollTop : 0, document.documentElement ? document.documentElement.scrollTop : 0);

}

function updateButtonVisibility() {
  const scrollPosition = getScrollPosition();
  const showButton = scrollPosition > 40;
  mybutton.style.display = showButton ? "block" : "none";

  // Store the visibility state in local storage
  localStorage.setItem("showButton", showButton);
}

function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

// Check local storage on page load and update button visibility
const showButtonFromStorage = localStorage.getItem("showButton") === "true";
mybutton.style.display = showButtonFromStorage ? "block" : "none";

// Update button visibility on scroll
window.onscroll = updateButtonVisibility;

// Update button visibility on button click (optional)
// mybutton.addEventListener("click", updateButtonVisibility);
