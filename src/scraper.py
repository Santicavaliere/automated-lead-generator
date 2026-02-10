from src.config import BASE_URL
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_real_estate_leads():
    """
    Initializes the Chrome WebDriver and scrapes real estate agent data
    from the target URL.
    
    Returns:
        list: A list of dictionaries containing agent details (Name, Phone, Address).
    """
    print("🚀 Starting Real Estate Scraper...")

    # --- BROWSER CONFIGURATION ---
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # Keeps browser open after script ends
    options.add_argument('--ignore-certificate-errors')

    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # --- NAVIGATION ---
    print(f"🌐 Navigating to: {BASE_URL}")
    driver.get(BASE_URL)

    # Human-like delay to ensure page load
    time.sleep(random.uniform(3, 5))

    # --- DATA EXTRACTION ---
    leads = []
    
    # Locate all result cards on the page
    results = driver.find_elements(By.CLASS_NAME, "result")
    
    print(f"✅ Found {len(results)} agents on this page.\n")

    for card in results:
        try:
            # 1. Extract Name
            name_element = card.find_element(By.CLASS_NAME, "business-name")
            name = name_element.text
            
            # 2. Extract Phone
            try:
                phone_element = card.find_element(By.CLASS_NAME, "phones")
                phone = phone_element.text
            except:
                phone = "N/A"

            # 3. Extract Address
            try:
                address_element = card.find_element(By.CLASS_NAME, "street-address")
                address = address_element.text
            except:
                address = "N/A"

            lead_data = {
                "business_name": name,
                "phone": phone,
                "address": address,
                "source": "YellowPages"
            }
            
            leads.append(lead_data)
            print(f"🔹 Extracted: {name} | 📞 {phone}")

        except Exception as e:
            print(f"⚠️ Error extracting card: {e}")
            continue

    print("\n🎉 Scraping completed successfully.")
    return leads

if __name__ == "__main__":
    data = get_real_estate_leads()
    print(f"\n📊 Total Leads Collected: {len(data)}")