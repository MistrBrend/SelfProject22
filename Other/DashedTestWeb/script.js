 const open = document.querySelector("hamburger-menu-open");
 const close = document.querySelector("hamburger-menu-close");

 const menuList = document.querySelector(".menu-wrapper").classList;

 open.addEventListener("click", () => {
    menuList.toggle("opened");
    menuList.toggle("closed");
 })

 close.addEventListener("click", () => {
    menuList.toggle("closed");
    menuList.toggle("opened");
 })