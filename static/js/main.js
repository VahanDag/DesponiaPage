stickybits('.navgez', {
    useStickyClasses: true
});

const headerHeight = document.querySelector('.navgez').offsetHeight;

stickybits('.marquee-div', {
    stickyBitStickyOffset: headerHeight
})