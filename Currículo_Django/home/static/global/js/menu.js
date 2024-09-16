document.addEventListener('click', function(event) {
    // Seleciona o menu, o ícone do menu e o checkbox
    const menu = document.querySelector('.menu');
    const menuToggle = document.querySelector('#menu_toggle');
    const menuIcon = document.querySelector('.menu_icon');

    // Se o checkbox está marcado (menu está aberto)
    if (menuToggle.checked) {
        // Verifica se o clique foi fora do menu e do ícone
        if (!menu.contains(event.target) && !menuIcon.contains(event.target)) {
            // Desmarca o checkbox para fechar o menu
            menuToggle.checked = false;
        }
    }

    // Previne que o menu feche imediatamente ao clicar no ícone do menu
    menuIcon.addEventListener('click', function(event) {
        event.stopPropagation(); // Evita que o clique feche o menu imediatamente
    });
});
