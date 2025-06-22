Arbol de carpetas

concordia_burger_club/
├── guia.md
├── main.py                      
├── gestion_productos.py         
├── gestion_combos.py            
├── gestion_pedidos.py
├── menu_pedidos.py
├── personalizacion.py           
├── reportes_cbc.py              
├── persistencia_cbc.py          
├── utils_cbc.py                 
├── datos/
│   ├── acompanamientos.json
│   ├── hamburguesas.json
│   ├── bebidas.json
│   ├── pedidos.json             
│   └── combos.json              

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