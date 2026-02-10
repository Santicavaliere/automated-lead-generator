import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_real_estate_leads():
    print("🚀 Iniciando el Scraper de Real Estate...")

    # --- CONFIGURACIÓN DEL NAVEGADOR ---
    options = webdriver.ChromeOptions()
    # Esta línea mantiene el navegador abierto cuando termina el script (para que veas lo que hizo)
    options.add_experimental_option("detach", True) 
    # Esta línea evita errores comunes de certificados en algunos sitios
    options.add_argument('--ignore-certificate-errors')

    # Iniciamos Chrome (El "Titiritero")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # --- NAVEGACIÓN ---
    url = "https://www.yellowpages.com/miami-fl/real-estate-agents"
    print(f"🌐 Navegando a: {url}")
    driver.get(url)

    # Esperamos unos segundos para que cargue la página (Comportamiento Humano)
    time.sleep(random.uniform(3, 5))

    # --- EXTRACCIÓN DE DATOS ---
    leads = []
    
    # Buscamos todas las "tarjetas" de resultados. 
    # En YellowPages, cada negocio está en un div con la clase 'result'
    results = driver.find_elements(By.CLASS_NAME, "result")
    
    print(f"✅ Se encontraron {len(results)} agentes en esta página.\n")

    for card in results:
        try:
            # 1. Extraer Nombre (está dentro de un <a> con clase 'business-name')
            name_element = card.find_element(By.CLASS_NAME, "business-name")
            name = name_element.text
            
            # 2. Extraer Teléfono (está en un div con clase 'phones')
            try:
                phone_element = card.find_element(By.CLASS_NAME, "phones")
                phone = phone_element.text
            except:
                phone = "N/A" # Si no tiene teléfono, ponemos N/A

            # 3. Extraer Dirección (si existe)
            try:
                address_element = card.find_element(By.CLASS_NAME, "street-address")
                address = address_element.text
            except:
                address = "N/A"

            # Guardamos los datos en un diccionario (estructura de datos limpia)
            lead_data = {
                "business_name": name,
                "phone": phone,
                "address": address,
                "source": "YellowPages"
            }
            
            leads.append(lead_data)
            print(f"🔹 Extraído: {name} | 📞 {phone}")

        except Exception as e:
            print(f"⚠️ Error extrayendo una tarjeta: {e}")
            continue

    # Cerramos el navegador al terminar (Opcional, por ahora lo dejo comentado para que lo veas)
    # driver.quit()
    
    print("\n🎉 Extracción finalizada con éxito.")
    return leads

# Esto permite probar el script directamente si lo ejecutamos
if __name__ == "__main__":
    data = get_real_estate_leads()
    print(f"\n📊 Total Leads Recolectados: {len(data)}")