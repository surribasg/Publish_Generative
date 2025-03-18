# Estructura del Proyecto - Publish_Generative

Este documento describe la estructura del proyecto **Publish_Generative**, incluyendo los archivos y carpetas clave.

## 📁 Estructura de Carpetas y Archivos

```plaintext
Publish_Generative/
│── venv/                   # Entorno virtual (ya creado)
│── app/                    # Código fuente principal
│   │── __init__.py         # Permite tratar 'app' como un módulo
│   │── main.py             # Archivo principal (Streamlit + Crew)
│   │── agents.py           # Configuración de agentes Crew
│   │── tasks.py            # Configuración de tareas Crew
│── data/                   # Datos externos o generados (opcional)
│── .gitignore              # Para ignorar archivos innecesarios
│── requirements.txt        # Dependencias del proyecto
│── README.md               # Descripción del proyecto
