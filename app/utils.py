import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener la API Key desde el .env
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

def interpretar_rendimiento(valor):
    """
    Convierte un valor de rendimiento (ej: "+2.15%") en una categoría interpretativa.
    """
    try:
        porcentaje = float(valor.strip("%"))  # Convierte "+2.15%" en 2.15
        if porcentaje > 1.5:
            return "Muy positivo"
        elif porcentaje > 0:
            return "Positivo"
        elif porcentaje == 0:
            return "Neutro"
        else:
            return "Negativo"
    except ValueError:
        return "Información no disponible"

def obtener_tendencias(sector="Technology"):
    """
    Consulta la API de Alpha Vantage para obtener el rendimiento del sector especificado.
    Formatea la salida con interpretación del resultado.
    """
    url = f"https://www.alphavantage.co/query?function=SECTOR&apikey={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extraer el rendimiento del sector
        rendimiento = data.get("Rank A: Real-Time Performance", {}).get(sector, "Datos no disponibles")
        interpretacion = interpretar_rendimiento(rendimiento)

        return f"**Sector:** {sector}\n**Rendimiento:** {rendimiento}\n**Interpretación:** {interpretacion}"
    
    except requests.exceptions.RequestException as e:
        return f"Error al obtener datos de Alpha Vantage: {str(e)}"
