const border = document.querySelector(".all-links");
const links = document.querySelectorAll(".links");

console.log(links);

links.forEach(link => {
    link.addEventListener("click", () => {
        border.querySelector(".active").classList.remove("active");
        link.classList.add("active");
    });

});
