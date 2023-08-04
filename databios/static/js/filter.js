function obtenerCategory(element) {
  let selected = element.options[element.selectedIndex].text;
  console.log(selected);

  apiUrl = '/api/?';

  apiUrl+= 'categorias=' + selected;
  
  fetch(apiUrl)
  .then(response => {
     return response.json()}).then(data => {console.log(data);
     toHtml(data)});
}
hj
function toHtml(data) {
  texto = ''

  data.forEach(element => {
    texto += `
    <div class="product">
      <div class="img-container">
        <img src='${element.imagen}' alt='${element.nombre}' class="product-image">
      </div>
      <h1 class="product-title">${element.nombre}</h1>
      <h2 class="product-description">${element.descripcion}</h2>
      <h2>Stock: ${element.stock}</h2>
      <h1 class="product-price">Precio: S/${element.precio}</h1>
      <button class="buy-button">VER MAS</button>
    </div>
    `
  });
  div = document.querySelector('.products-container');
  div.innerHTML = texto;
}