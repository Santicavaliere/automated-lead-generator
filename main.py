from src.scraper import get_real_estate_leads
from src.data_manager import DataManager
import time

def main():
    """
    Main entry point for the Lead Generation Bot.
    Orchestrates the scraping and data processing workflow.
    """
    print("🤖 --- STARTING LEAD GENERATION BOT ---")
    start_time = time.time()

    # STEP 1: EXTRACT (Scraping)
    raw_leads = get_real_estate_leads()

    # STEP 2: TRANSFORM & LOAD (ETL)
    dm = DataManager()
    dm.process_and_save(raw_leads)

    end_time = time.time()
    duration = round(end_time - start_time, 2)
    print(f"🏁 Process completed successfully in {duration} seconds.")

if __name__ == "__main__":
    main()