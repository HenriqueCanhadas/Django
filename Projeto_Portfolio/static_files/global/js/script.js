/*==================== toggle icon navbar ====================*/
let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () =>{
    menuIcon.classList.toggle('bxs-x-circle');
    navbar.classList.toggle('active');
}

/*==================== scroll sections active link ====================*/
let sections = document.querySelectorAll('section')
let navLinks = document.querySelectorAll('header nav a')

window.onscroll = () => {
    sections.forEach(sec =>{
        let top =window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(top >= offset && top < offset + height){
            navLinks.forEach(links=>{
                links.classList.remove('active');
                document.querySelector('header nav a[href*='+id+']').classList.add('active');
            })
        }
        });
    
    /*==================== sticky navbar ====================*/

    let header = document.querySelector('header')

    header.classList.toggle('sticky', window.scrollY > 100);

    /*==================== remove toggle icon and navbar when click navbar link (scroll) ====================*/
    menuIcon.classList.remove('bxs-x-circle');
    navbar.classList.remove('active');
};

/*==================== scroll reveal ====================*/
ScrollReveal({ 
    // reset: true,
    distance: '80px',
    duration: 2000,
    delay:200
});

ScrollReveal().reveal('.home-content, .heading', {origin:'top'});
ScrollReveal().reveal('.home-img, .services-container, .portfolio-box, .contact form', {origin:'bottom'});
ScrollReveal().reveal('.home-content h1, .about-img', {origin:'left'});
ScrollReveal().reveal('.home-content p, .about-content', {origin:'right'});
/*==================== typed js ====================*/
const typed = new Typed('.multipe-text', {
    strings:['Desenvolvedor Python','Analista de Redes' ,'Desenvolvedor Front-end','Programador', 'Desenvolvedor Back-end'],
    typeSpeed:100,
    backSpeed:100,
    backDelay:1000,
    loop:true
});

/*==================== LER MAIS ====================*/
function mostrarTextoCompleto() {
    var textoCompleto = document.getElementById("texto-completo");
    var botaoLeiaMais = document.getElementById("leia-mais");
    
    if (textoCompleto.style.display === "none") {
        textoCompleto.style.display = "block";
        botaoLeiaMais.style.display = "none"; // Esconde o botão após expandir o texto
    }
}