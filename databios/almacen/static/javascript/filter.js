function obtenerSelect(selectElement) {
  var selected = selectElement.options[selectElement.selectedIndex].text;
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
    <div class="col-lg-4 col-md-6 col-sm-6">
      <div class="product__item">
        <div class="product__item__pic set-bg">
          <img src="${element.imagen}" alt="${element.nombre}">
        </div>
        <div class="product__item__text">
          <h6><a href="#">${element.nombre}</a></h6>
          <h5>$${element.precio}</h5>
        </div>
      </div>
    </div>
    `
  });
  div = document.querySelector('.content');
  div.innerHTML = texto;
}