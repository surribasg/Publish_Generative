# 📊 Inteligencia de Mercado con CrewAI

Este proyecto utiliza **CrewAI**, **Ollama (Llama 3.1)** y **Streamlit** para analizar tendencias del mercado y generar estrategias basadas en datos reales de **Alpha Vantage**.

---

## 🚀 Características

- **Enfoque multiagente:** Orquestación de múltiples agentes de IA especializados que colaboran en un flujo de trabajo autónomo para el análisis de mercado.
- **Integración con Alpha Vantage:** Consulta en tiempo real de datos bursátiles mediante su API.
- **Uso de modelos de lenguaje (LLM):** Llama 3.1, ejecutado localmente con **Ollama**, analiza los datos financieros obtenidos.
- **Arquitectura modular:** Código organizado en agentes, tareas y utilidades para facilitar la extensibilidad.
- **Automatización del flujo de trabajo:** Desde la obtención de datos hasta la generación de reportes de análisis financiero.

---

## 🔑 Configuración del token de Alpha Vantage

Para utilizar datos de mercado en tiempo real, debes configurar tu **API Key** de **Alpha Vantage**.

### 1️⃣ Obtener tu API Key
- Ve a [Alpha Vantage](https://www.alphavantage.co/support/#api-key) y regístrate para obtener una API Key gratuita.

### 2️⃣ Configurar el token en un archivo `.env`
- En la raíz del proyecto (`Publish_Generative`), **crea un archivo llamado `.env`**.
- **Abre `.env` en un editor de texto** y agrega lo siguiente:  
  ```plaintext
  ALPHA_VANTAGE_API_KEY=TU_API_KEY_AQUI
  ```

---

## 📂 Estructura del Proyecto

La siguiente estructura muestra cómo están organizados los archivos dentro del proyecto `Publish_Generative`.

```plaintext
PUBLISH_GENERATIVE/        # Directorio raíz del proyecto
│-- app/                   # Carpeta principal de la aplicación
│   │-- __pycache__/       # Archivos compilados de Python
│   │-- __init__.py        # Marca el directorio como un paquete de Python
│   │-- agents.py          # Define los agentes de IA en CrewAI
│   │-- main.py            # Script principal para ejecutar la aplicación
│   │-- tasks.py           # Define las tareas asignadas a los agentes
│   │-- utils.py           # Funciones utilitarias para el proyecto
│-- data/                  # Carpeta para almacenar archivos de datos
│-- venv/                  # Entorno virtual (debe incluirse en .gitignore)
│-- .env                   # Archivo de variables de entorno (API keys, configuraciones)
│-- .gitignore             # Archivo para excluir elementos innecesarios en Git
│-- estructura.md          # Documento que explica la estructura del proyecto
│-- README.md              # Archivo principal de documentación
│-- requirements.txt       # Lista de dependencias necesarias para el proyecto
```

---

## 📥 Instalación y Ejecución del Proyecto

Para ejecutar este proyecto en tu entorno local, sigue estos pasos:

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/surribasg/Publish_Generative.git
cd Publish_Generative
```

### 2️⃣ Crear un entorno virtual e instalar dependencias
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3️⃣ Ejecutar la aplicación
```bash
streamlit run app.py
```




