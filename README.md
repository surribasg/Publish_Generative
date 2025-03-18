# 📊 Inteligencia de Mercado con CrewAI

Este proyecto utiliza **CrewAI**, **Ollama (Llama 3.1)** y **Streamlit** para analizar tendencias del mercado y generar estrategias basadas en datos reales de **Alpha Vantage**.

---

## 🚀 Características
✅ **Análisis de tendencias de mercado en tiempo real** con datos de **Alpha Vantage**.  
✅ **Generación de estrategias de marketing** basadas en IA.  
✅ **Evaluación de viabilidad financiera** de estrategias comerciales.  
✅ **Implementado con agentes de IA** mediante **CrewAI**.  
✅ **Interfaz interactiva con Streamlit**.

---

## 🔑 Configuración del Token de Alpha Vantage
Para utilizar datos de mercado en tiempo real, debes configurar tu **API Key** de **Alpha Vantage**.

### 1️⃣ Obtener tu API Key
- Ve a [Alpha Vantage](https://www.alphavantage.co/support/#api-key) y regístrate para obtener una API Key gratuita.

### 2️⃣ Configurar el Token en un Archivo `.env`
- En la raíz del proyecto (`Publish_Generative`), **crea un archivo llamado `.env`**.
- **Abre `.env` en un editor de texto** y agrega lo siguiente:
  ```plaintext
  ALPHA_VANTAGE_API_KEY=TU_API_KEY_AQUI

