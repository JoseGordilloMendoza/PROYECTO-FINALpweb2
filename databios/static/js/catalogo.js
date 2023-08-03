// Obtener todos los enlaces de categorías
const categoriasEnlaces = document.querySelectorAll('.filtro a');

// Agregar un evento clic a cada enlace de categoría
categoriasEnlaces.forEach(enlace => {
    enlace.addEventListener('click', (event) => {
        event.preventDefault();

        // Obtener la categoría seleccionada
        const categoriaSeleccionada = event.target.dataset.categoria;

        // Ocultar todos los productos
        const productos = document.querySelectorAll('.producto');
        productos.forEach(producto => {
            producto.style.display = 'none';
        });

        // Mostrar solo los productos de la categoría seleccionada
        const productosFiltrados = document.querySelectorAll(`[data-categoria="${categoriaSeleccionada}"]`);
        productosFiltrados.forEach(producto => {
            producto.style.display = 'block';
        });
    });
});
