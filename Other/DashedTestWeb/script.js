const open = document.querySelector(".hamburger-menu-open");
const close = document.querySelector(".hamburger-menu-close");
const menuPage = document.querySelector(".menu-wrapper").classList;

const menuContainer = document.querySelector(".menu-list");
const menuLinks = document.querySelectorAll(".link");
const menuLists = document.querySelectorAll(".list");

// Home button on menu which makes u go back.
menuLists[0].addEventListener("click", () => {
  menuPage.toggle("closed");
})

// Makes the background of each menu button change color upon clicking
menuLinks.forEach(link => {
  link.addEventListener("click", () => {
    menuContainer.querySelector(".active").classList.remove("active");
    link.classList.add("active");
    
    // Opens de list under the link
    const linkNumber = link.id - 1;
    menuContainer.querySelector(".nonhidden").classList.remove("nonhidden");
    menuLists[linkNumber].classList.add("nonhidden");
  })
})



// Open menu button
open.addEventListener('click', () => {
  menuPage.toggle("opened");
  menuPage.remove("closed");
})

// Close menu button
close.addEventListener("click", () => {
  menuPage.toggle("closed");
  menuPage.remove("opened");
})
