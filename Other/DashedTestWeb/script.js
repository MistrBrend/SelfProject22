const open = document.querySelector(".hamburger-menu-open");
const close = document.querySelector(".hamburger-menu-close");
const menuPage = document.querySelector(".menu-wrapper").classList;

const menuListChilds = document.querySelector("ul li a").classList;
console.log(menuListChilds);


open.addEventListener('click', () => {
  menuPage.toggle("opened");
  menuPage.remove("closed");
})

close.addEventListener("click", () => {
  menuPage.toggle("closed");
  menuPage.remove("opened");
})
