function tgPreview(event) {
  if (event.target.tagName === "P") {
    event.target.parentNode.classList.toggle("active");
  }
  if (event.target.classList.contains("active")) {
    event.target.classList.toggle("active");
  }
  if (event.target.textContent === "инструкция к составлению заданий") {
    event.target.textContent = "закрыть";
  } else {
    event.target.textContent = "инструкция к составлению заданий";
  }
}
function init() {
  document.querySelector(".help-a").addEventListener("click", tgPreview);
}

window.addEventListener("DOMContentLoaded", init);
