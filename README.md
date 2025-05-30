[Video explicativo](https://youtu.be/Z5xzdK_V3G4)

# Script para guardar tus compras de robosats en Google Sheets

Este script permite actualizar una hoja de cálculo de Google Sheets con los archivos JSON generados de una compra en RoboSats.

## Requisitos previos

### 1. Instalación de Python y pip

Asegúrate de tener Python 3 y pip instalados en tu máquina. Si no los tienes, puedes descargarlos desde:

- [Descargar Python](https://www.python.org/downloads/)

### 2. Crear un entorno virtual

Es recomendable crear un entorno virtual para manejar las dependencias del proyecto. Puedes hacer esto ejecutando los siguientes comandos:

#### **En Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

#### **En Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar las dependencias

Una vez que tengas el entorno virtual activado, instala las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

### 4. Crear el archivo `credenciales.json`

Descarga las credenciales de la API de Google Sheets desde [Google Cloud Console](https://console.cloud.google.com/), y guarda el archivo como `credenciales.json` en el mismo directorio que el script.

### 5. Modifica config.json

### 6. Ejecución del script

Para ejecutar el script, usa el siguiente comando:

```bash
python btc.py
```

### 7. Eliminación de archivos (opcional)

El script preguntará si deseas eliminar los archivos JSON después de procesarlos. Puedes confirmar o cancelar esta acción.

---



[Plantilla en Google SpreadSheets](https://docs.google.com/spreadsheets/d/1pGe8Pw-z-nSJa9FYEgPOqKPJCPZD6ao4GPaWX1034ZQ/edit?usp=sharing)
