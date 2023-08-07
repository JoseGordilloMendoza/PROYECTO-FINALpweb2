# PROYECTO-FINALpweb2

## Integrantes
Rommel Chambi
Ower Lopez
Jose Gordillo
ALejandro Phocco

## Tipo de Sistema
## Requisitos del sistema

1. **Inicio de sesión:**
   - La página web debe tener un sistema de inicio de sesión para diferenciar al administrador del usuario.
   - El administrador debe poder autenticarse con un nombre de usuario y contraseña.

2. **Páginas de administración:**
   - Después de iniciar sesión, el administrador debe tener acceso a una páginas de administración exclusivas.
   - En las páginas de administración, el administrador debe poder gestionar el catálogo de productos.

3. **Gestión del catálogo de productos:**
   - El administrador debe poder agregar, editar y eliminar productos del catálogo.
   - Cada producto debe tener atributos como nombre, descripción, precio, imagen y cantidad en stock.

4. **Mostrar catálogo de productos:**
   - La página web debe mostrar el catálogo completo de productos al público.
   - Los usuarios deben poder ver los detalles de cada producto, incluyendo su nombre, descripción, precio e imagen.

5. **Categorías de productos:**
   - Los productos deben poder clasificarse en diferentes categorías para facilitar la navegación.
   - Los usuarios deben poder filtrar los productos por categoría.

### Requerimientos No Funcionales:

1. **Interfaz de usuario amigable:**
   - La página web debe tener una interfaz de usuario intuitiva y atractiva.
   - Debe ser fácil para los usuarios navegar por el catálogo y buscar productos.

2. **Diseño responsivo:**
   - La página web debe ser compatible con dispositivos móviles y ofrecer una experiencia de usuario adecuada en diferentes tamaños de pantalla.

3. **Seguridad:**
   - La seguridad debe ser una prioridad, especialmente en el sistema de inicio de sesión del administrador.

## Modelo de datos


## Diccionario de datos

### Producto

| Atributo      | Tipo        | Nulo | Clave | Predeterminado | Descripción                       |
|---------------|-------------|------|------|----------------|-----------------------------------|
| id            | Entero      | No   | Sí   | Ninguno        | Clave primaria                    |
| nombre        | Char(100)   | No   | No   | Null           | Nombre de la categoría            |
| descripcion   | Texto       | No   | No   | Null           | Descripción del producto          |
| precio        | Entero      | No   | No   | Null           | Precio del producto               |
| imagen        | Imagen      | Sí   | No   | Null           | Ruta de la imagen asociada al producto|
| stock         | Entero      | No   | No   | Null           | Cantidad en stock del producto    |

### Categoria

| Atributo      | Tipo        | Nulo | Clave | Predeterminado | Descripción               |
|---------------|-------------|------|------|----------------|---------------------------|
| id            | Entero      | No   | Sí   | Ninguno        | Clave primaria            |
| nombre        | Char(100)   | No   | No   | Null           | Nombre de la categoría    |

## Diagrama Entidad-Relación
## Administración con Django
## Plantillas Bootstrap
## CRUD - Core Business - Clientes finales
## Servicios mediante una API RESTful
## Operaciones asíncronas AJAX
## Investigación: Email, Upload.






