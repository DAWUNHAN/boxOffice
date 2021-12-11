function checkMenu() {
    if (yOffset > 44) {
        document.body.classList.add('local-nav-sticky');
    } else {
        document.body.classList.remove('local-nav-sticky');
    }
}