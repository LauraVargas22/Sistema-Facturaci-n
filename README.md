# SISTEMA DE FACTURACIÓN
Este programa permite generar una factura básica ingresando hasta 10 productos con su nombre y precio.
El sistema calcula el subtotal, aplica un 10% de descuento si el total supera los $100.

## 🧠 Características principales

- Solicita el nombre y precio de cada producto.

- Calcula el subtotal, descuento (10%) y total final.

- Muestra los resultados en una factura.

- Usa Programación Orientada a Objetos (POO) para una estructura clara y extensible.

## 🛠️ Tecnologías utilizadas  
- [Python 3.x](https://www.python.org/)  
- [Rich-pyfiglet](https://pypi.org/project/rich-pyfiglet/) - para la interfaz de consola

### ▶️ Instalación y uso
1. Clonar el repositorio
```bash
git clone https://github.com/LauraVargas22/Sistema-Facturaci-n.git
cd Sistema-Facturaci-n
```

2. Instalación de librerías
- Numpy
```bash
pip install numpy
```
- Matplotlib
```bash
pip install matplotlib
```
- Rich y Pyfiglet
```bash
pip install rich pyfiglet
```

3. Uso
```
python main.py
```

## 📂 Estructura del proyecto  
```
graficador-funciones/
├── modules/                 
│   ├── invoice.py       # Lógica para el sistema de facturación
│   ├── menus.py               # Menús de navegación en consola
│   ├── exit.py               # Opción para salir del programa
│   ├── titles.py              # Títulos y subtítulos personalizados
│   ├── customs.py             # Estilos y configuraciones
│   └── messages.py            # Mensajes de ayuda y notificaciones
├── main.py                    # Archivo principal para ejecutar el programa
└── README.md                  # Documentación del proyecto
```

## Referencias
- [Documentación Rich](https://rich.readthedocs.io/en/latest/index.html)
