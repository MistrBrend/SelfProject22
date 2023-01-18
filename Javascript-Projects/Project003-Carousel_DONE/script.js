// initialize every object from the html document
const track = document.querySelector('.carousel__track');
const slides = Array.from(track.children);
const rightButton = document.querySelector('.carousel__button--right');
const leftButton = document.querySelector('.carousel__button--left');
const dotsNav = document.querySelector('.carousel__nav');
const dots = Array.from(dotsNav.children);

const slideWith = slides[0].getBoundingClientRect().width;

// adds current-slide to the first slide
slides[0].classList.add('current-slide');

// arrange the slides next to each other
const setSlidePosition = (slide, index) => {
    slide.style.left = slideWith * index + 'px';
}
slides.forEach(setSlidePosition);

const moveToSlide = (track, currentSlide, targetSlide) => {
    track.style.transform = 'translateX(-'+ targetSlide.style.left +')';
    currentSlide.classList.remove('current-slide');
    targetSlide.classList.add('current-slide');
}
const updateDots = (currentDot, targetDot) => {
    currentDot.classList.remove('current-slide');
    targetDot.classList.add('current-slide');
}
const hideShowArrows = (slides, leftButton, rightButton, targetIndex) => {
    if (targetIndex === 0) {
        leftButton.classList.add('is-hidden');
        rightButton.classList.remove('is-hidden');
        // console.log('1')
    } else if (targetIndex === slides.length - 1) {
        leftButton.classList.remove('is-hidden');
        rightButton.classList.add('is-hidden');
        // console.log('2');
    } else {
        leftButton.classList.remove('is-hidden');
        rightButton.classList.remove('is-hidden');
        // console.log('3')
    }
}

// When you click on the left '<' button
leftButton.addEventListener('click', e => {
    const currentSlide = track.querySelector('.current-slide');
    const prevSlide = currentSlide.previousElementSibling;
    const currentDot = dotsNav.querySelector('.current-slide');
    const prevDot = currentDot.previousElementSibling;
    const prevIndex = slides.findIndex(slide => slide === prevSlide);

    moveToSlide(track, currentSlide, prevSlide);
    updateDots(currentDot, prevDot);
    hideShowArrows(slides, leftButton, rightButton, prevIndex);
})

// When you click on the right '>' button
rightButton.addEventListener('click', e => {
    const currentSlide = track.querySelector('.current-slide');
    const nextSlide = currentSlide.nextElementSibling;
    const currentDot = dotsNav.querySelector('.current-slide');
    const nextDot = currentDot.nextElementSibling;
    const nextIndex = slides.findIndex(slide => slide === nextSlide);

    moveToSlide(track, currentSlide, nextSlide);
    updateDots(currentDot, nextDot);
    hideShowArrows(slides, leftButton, rightButton, nextIndex);

})

// when i click to change slide, the indicators change with it.
dotsNav.addEventListener('click', e => {
    const targetDot = e.target.closest('button');
    
    const currentSlide = track.querySelector('.current-slide');
    const currentDot = dotsNav.querySelector('.current-slide');

    // finds which dot he clicks
    const targetIndex = dots.findIndex(dot => dot === targetDot);
    const targetSlide = slides[targetIndex];

    moveToSlide(track, currentSlide, targetSlide);
    updateDots(currentDot, targetDot);
    hideShowArrows(slides, leftButton, rightButton, targetIndex);
})

