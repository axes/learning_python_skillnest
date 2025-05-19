# Paso 1: Carga de datos
ventas = [
    {"fecha": "2024-01-01", "producto": "Lápiz", "cantidad": 10, "precio": 0.5},
    {"fecha": "2024-01-01", "producto": "Cuaderno", "cantidad": 5, "precio": 1.5},
    {"fecha": "2024-01-02", "producto": "Lápiz", "cantidad": 20, "precio": 0.55},
    {"fecha": "2024-01-02", "producto": "Goma", "cantidad": 15, "precio": 0.3},
    {"fecha": "2024-01-03", "producto": "Cuaderno", "cantidad": 10, "precio": 1.6},
    {"fecha": "2024-01-03", "producto": "Goma", "cantidad": 5, "precio": 0.35},
]

# Paso 2: Calcular ingresos totales
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

# Paso 3: Producto más vendido
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    if producto not in ventas_por_producto:
        ventas_por_producto[producto] = 0
    ventas_por_producto[producto] += cantidad

producto_mas_vendido = max(ventas_por_producto.items(), key=lambda x: x[1])

# Paso 4: Promedio de precio por producto
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    ingreso = venta["precio"] * venta["cantidad"]
    cantidad = venta["cantidad"]
    if producto not in precios_por_producto:
        precios_por_producto[producto] = [0, 0]  # [total ingreso, cantidad]
    precios_por_producto[producto][0] += ingreso
    precios_por_producto[producto][1] += cantidad

precio_promedio_por_producto = {}
for producto, (total_ingreso, total_cantidad) in precios_por_producto.items():
    precio_promedio_por_producto[producto] = total_ingreso / total_cantidad

# Paso 5: Ingresos por día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    if fecha not in ingresos_por_dia:
        ingresos_por_dia[fecha] = 0
    ingresos_por_dia[fecha] += ingreso

# Paso 6: Representación de datos - resumen_ventas
resumen_ventas = {}
for producto in ventas_por_producto:
    resumen_ventas[producto] = {
        "cantidad_total": ventas_por_producto[producto],
        "ingresos_totales": precios_por_producto[producto][0],
        "precio_promedio": precio_promedio_por_producto[producto]
    }

# Mostrar resultados
import pprint
resultados = {
    "Lista de Ventas": ventas,
    "Ingresos Totales": ingresos_totales,
    "Producto más Vendido": {
        "producto": producto_mas_vendido[0],
        "cantidad": producto_mas_vendido[1]
    },
    "Precio Promedio por Producto": precio_promedio_por_producto,
    "Ingresos por Día": ingresos_por_dia,
    "Resumen de Ventas": resumen_ventas
}

pprint.pprint(resultados)