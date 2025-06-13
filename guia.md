Arbol de carpetas

concordia_burger_club/
├── main.py                      # Punto de entrada con el menú interactivo
├── gestion_productos.py         # ABM de productos del menú
├── gestion_pedidos.py           # ABM de pedidos
├── reportes_cbc.py              # Reportes por consola
├── persistencia_cbc.py          # Lectura y escritura de archivos JSON
├── utils_cbc.py                 # Funciones auxiliares
├── datos/
│   ├── productos.json           # Datos de productos
│   ├── pedidos.json             # Datos de pedidos
│   └── combos.json              # Datos de combos predefinidos (opcional)

----------------------------------------------------------------------------------

🗂 Estructura general del proyecto
📁 main.py
Es el punto de entrada del programa. Muestra el menú principal por consola y permite al usuario elegir entre gestionar productos, pedidos o ver reportes. Llama a las funciones de los otros módulos.

📁 gestion_productos.py
Maneja el ABM (Alta, Baja, Modificación) de los productos del menú, como hamburguesas, papas o bebidas. Usa listas y diccionarios para organizar los datos de cada producto.

📁 gestion_pedidos.py
Administra los pedidos de los clientes. Permite crear, modificar, eliminar y ver pedidos, calculando automáticamente el total según los productos elegidos.

📁 reportes_cbc.py
Genera reportes simples por consola, como el total de ventas, el producto más vendido o un listado de pedidos realizados.

📁 persistencia_cbc.py
Se encarga de leer y guardar los datos en archivos JSON. Así los productos y pedidos se mantienen aunque cerremos el programa.

📁 utils_cbc.py
Contiene funciones auxiliares como generación de IDs únicos o validaciones de entrada. Ayuda a no repetir código.

📁 datos/
Carpeta donde se guardan los archivos:

productos.json: Lista de productos disponibles.

pedidos.json: Lista de pedidos realizados.