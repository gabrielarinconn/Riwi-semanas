## Prueba de Desempeño – Módulo 1 Python
# Título: 📖 🪼 Gabi JellyFish Library  🪼 📖
Sistema Integral de Gestión de Inventario y Ventas con Reportes Dinámicos

### Caso de uso (Épica):

Como encargado del área digital de una librería nacional, necesitas un sistema robusto que no solo permita registrar ventas y productos, sino también generar reportes detallados, aplicar descuentos por cliente, agrupar estadísticas por autor y evaluar el rendimiento del inventario con base en ventas.

# Requisitos Funcionales 📋

1. Gestión del inventario
    * Registrar, consultar, actualizar y eliminar productos.
    * Cada producto debe tener: título, autor, categoría, precio, cantidad en stock.
2. Registro y consulta de ventas
    * Permitir registrar ventas de productos, asociando: cliente, producto vendido, cantidad, fecha y descuento (si aplica).
    * Validar stock disponible y actualizarlo automáticamente.
3. Módulo de reportes
    * Mostrar el top 3 de productos más vendidos.
    * Generar reporte de ventas totales agrupado por autor.
    * Calcular ingreso neto y bruto (con y sin descuento).
4. Validaciones avanzadas
    * Validar entradas (números positivos, formatos correctos, campos obligatorios).
    * No permitir ventas con stock insuficiente.
5. Diseño modular con funciones
    * Cada funcionalidad debe estar encapsulada en funciones.
    * Se deben usar funciones con parámetros y retorno.
    * Uso de funciones lambda para cálculos agregados.

# Be a coder
6. Almacenamiento en estructuras de datos
    * Utilizar diccionarios anidados y listas para almacenar productos y ventas.
    * Agrupaciones y búsquedas deben usar métodos y estructuras eficientes.

# Criterios de Aceptación

* El sistema debe iniciar con al menos 5 productos pre-cargados.
* Todas las interacciones deben estar en inglés, incluidos comentarios, mensajes y documentación.
* Se deben aplicar buenas prácticas de codificación: funciones claras, uso de constantes, validaciones.
* El programa debe correr por consola y ofrecer un menú interactivo.
* El código debe manejar excepciones sin que el programa se detenga abruptamente.