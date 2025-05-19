# Análisis de Tarifas de Energía - Ruitoque

Aplicación web para el análisis comparativo de tarifas de energía entre RUITOQUE y otros comercializadores.

## 🚀 Características

- Carga y procesamiento de archivos Excel con tarifas
- Comparación de CU entre comercializadores
- Visualización interactiva de resultados
- Exportación de resultados a Excel
- Interfaz intuitiva y amigable

## 📋 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🔧 Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/analisis_tarifas_app.git
cd analisis_tarifas_app
```

2. Crear un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate     # En Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## 🎮 Uso

1. Ejecutar la aplicación:
```bash
streamlit run app.py
```

2. Abrir el navegador en la dirección indicada (generalmente http://localhost:8501)

3. Seguir las instrucciones en la interfaz para:
   - Cargar archivo de tarifas (.xlsm)
   - Seleccionar mercado y comercializador
   - Ejecutar comparación
   - Visualizar y exportar resultados

## 📦 Estructura del Proyecto

```
analisis_tarifas_app/
├── assets/                    # Recursos estáticos
├── config/                    # Configuraciones
├── utils/                     # Utilidades y funciones
├── requirements.txt          # Dependencias
└── app.py                    # Aplicación principal
```

## 🔍 Formato del Archivo de Entrada

El archivo Excel (.xlsm) debe contener:
- Hoja llamada "Hojadedatos"
- Tabla llamada "TablaDatos"
- Columnas requeridas: MERCADO, AÑO, FECHA, COMERCIALIZADOR, NT, G, C, CU

## 👥 Autores

- Andrés Badillo - [andresbadillo.co](https://www.andresbadillo.co/)

## 📄 Licencia

© 2025 Ruitoque Energía - Todos los derechos reservados 