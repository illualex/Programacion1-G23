# 👨‍💻 Grupo 23 - Programación 1 - UNER (Facultad de Ciencias de la Administración)

## 👥 Miembros

- Alejo Daniel Paniagua
- Nicolas Brasuna

---

## 📝 Descripción del trabajo

Para nuestro Trabajo Final Integrador de _Programación 1_, desarrollamos un sistema de pedidos para un local de comida rápida, con inspiración en franquicias como McDonald’s o Burger King.

Nuestro enfoque fue implementar todas las **funcionalidades obligatorias** solicitadas en la consigna del trabajo:

- Menú interactivo por consola.
- ABM (Alta, Baja y Modificación) de productos y combos.
- Gestión de pedidos.
- Reportes simples.
- Uso de archivos `.json` para guardar los datos.

⚠️ Debido al tiempo limitado y a que somos solo dos integrantes, **decidimos enfocarnos exclusivamente en las funcionalidades obligatorias**, dejando fuera las opcionales como interfaz gráfica o exportación de tickets.

Además, al no tener conocimientos previos en Python, tuvimos que aprender a medida que desarrollábamos. Para eso, **recurrimos a foros, videos, documentación oficial e Inteligencia Artificial (IA)** para entender mejor cómo resolver los desafíos y aprovechar el lenguaje al máximo.

---

## ⚙️ Funcionamiento del programa

El sistema se ejecuta completamente por **consola**, utilizando un menú interactivo numérico. Todas las acciones se manejan con opciones numeradas y una mínima cantidad de entrada de texto, para hacerlo ágil y claro. Pensado como un sistema real, donde la velocidad es requerida a la hora de tomar pedidos y otras funciones.

Se agregaron múltiples validaciones para evitar errores, como:

- Verificar que los datos no estén vacíos.
- Validar que los precios sean números válidos.
- Mensajes de error amigables.
- Opción de **salida rápida escribiendo "x"** en cualquier momento.

⚠️ El proyecto puede ser mas escalable aun, dejando la posibilidad de algo mas fiable a la realidad.

---

## 📁 Estructura de archivos del proyecto

concordia_burger_club/
├── datos/
│ ├── acompanamientos.json # Datos de productos tipo acompañamiento.
│ ├── bebidas.json # Datos de productos tipo bebida.
│ ├── combos.json # Datos de combos creados.
│ ├── hamburguesas.json # Datos de productos tipo hamburguesa.
│ └── pedidos.json # Pedidos realizados (cliente, productos, ticket, etc.).
│
├── .gitignore # Archivos a ignorar por Git (como pycache).
│
├── gestion_combos.py # Alta, baja y modificación de combos con productos seleccionados.
├── gestion_pedidos.py # Gestión de pedidos: creación, búsqueda y eliminación por número de ticket.
├── gestion_productos.py # ABM de productos individuales (hamburguesas, bebidas, acompañamientos).
│
├── main.py # Menú principal del sistema. Permite acceder a todas las funcionalidades.
│
├── persistencia_cbc.py # Módulo para leer y guardar datos en archivos .json.
├── reportes_cbc.py # Muestra reportes de ventas, productos más vendidos y promedios.
├── utils_cbc.py # Funciones auxiliares (limpiar consola, cancelar, mensajes de error).
│
├── README.md # Documentación del proyecto (este archivo).

---

## 🔎 ¿Qué hace cada archivo?

- `main.py`: Punto de entrada. Muestra el menú principal con acceso a productos, combos, pedidos y reportes.
- `gestion_productos.py`: Permite crear, modificar y eliminar productos por categoría.
- `gestion_combos.py`: Permite crear, modificar y eliminar combos combinando productos existentes.
- `gestion_pedidos.py`: Se usa para crear pedidos, revisar por ticket o eliminarlos. Incluye personalización de tamaño y aderezos.
- `reportes_cbc.py`: Genera reportes por consola: ventas de la semana, productos más vendidos y promedio por pedido.
- `persistencia_cbc.py`: Se encarga de la lectura y guardado de todos los archivos `.json`. Centraliza la persistencia.
- `utils_cbc.py`: Contiene funciones reutilizables como `limpiar_consola`, `mensaje_error` y `cancelacion_rapida`.
- Carpeta `datos/`: Contiene todos los archivos `.json` que almacenan la información del sistema: productos, combos y pedidos.

---
