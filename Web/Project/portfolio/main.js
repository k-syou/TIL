let arr_el_nav_link = document.querySelectorAll(".nav-link")
arr_el_nav_link.forEach((el) => {
    el.addEventListener('click', () => {
        console.log('click')
        let el_active = document.querySelector('.nav-bar.active')
        el_active.classList.remove('active')
        el_active.ariaCurrent = ''
        el.classList.add('active')
        el.ariaCurrent = 'page'
    })
})