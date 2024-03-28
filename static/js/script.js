let mybutton = document.getElementById("myBtn");

function getScrollPosition() {
  return Math.max(window.body ? window.body.scrollTop : 0, document.documentElement ? document.documentElement.scrollTop : 0);

}

function updateButtonVisibility() {
  const scrollPosition = getScrollPosition();
  const showButton = scrollPosition > 400;
  mybutton.style.display = showButton ? "block" : "none";

  // sparar knappens tillstånd 
  localStorage.setItem("showButton", showButton);
}

function topFunction() {
  document.body.scrollTop = 0; // för safari 
  document.documentElement.scrollTop = 0; // för andra webbläsare
}

// kollar i localstorage och uppdaterar
const showButtonFromStorage = localStorage.getItem("showButton") === "true";
mybutton.style.display = showButtonFromStorage ? "block" : "none";

// uppdaterar om knappen ska synas eller inte
window.onscroll = updateButtonVisibility;


