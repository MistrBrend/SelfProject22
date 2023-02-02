const links = document.querySelectorAll(".link").classList;
console.log(links);

links.forEach(link => {
    link.addEventListener('click', function () {
        links.forEach(link => {
            link.classList.remove('active');
        });
        link.classList.add('active');
    });
});
