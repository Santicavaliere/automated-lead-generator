from src.scraper import get_real_estate_leads
from src.data_manager import DataManager
import time

def main():
    print("🤖 --- INICIANDO BOT DE GENERACIÓN DE LEADS ---")
    start_time = time.time()

    # PASO 1: EXTRAER (Scraping)
    # Llamamos a la función que creaste en la Fase 2
    raw_leads = get_real_estate_leads()

    # PASO 2: TRANSFORMAR Y CARGAR (ETL)
    # Instanciamos nuestra clase de datos
    dm = DataManager()
    # Le pasamos los datos sucios para que los limpie y guarde
    dm.process_and_save(raw_leads)

    end_time = time.time()
    duration = round(end_time - start_time, 2)
    print(f"🏁 Proceso completado exitosamente en {duration} segundos.")

if __name__ == "__main__":
    main()