import pandas as pd
import os
from datetime import datetime

class DataManager:
    """
    Handles data processing, cleaning, and export operations (ETL).
    """
    def __init__(self):
        # Define storage directory
        self.data_dir = "data"
        os.makedirs(self.data_dir, exist_ok=True)

    def process_and_save(self, raw_data_list):
        """
        Converts raw data list to a DataFrame, cleans duplicates,
        and exports to CSV and Excel formats.
        """
        if not raw_data_list:
            print("⚠️ No data to process.")
            return

        print("\n⚙️  Starting data processing...")

        # 1. CONVERT TO DATAFRAME
        df = pd.DataFrame(raw_data_list)

        # 2. CLEANING & DEDUPLICATION
        count_initial = len(df)
        
        # Remove duplicates based on Name AND Phone
        df.drop_duplicates(subset=['business_name', 'phone'], keep='first', inplace=True)
        
        # Remove rows where Name is N/A
        df = df[df['business_name'] != "N/A"]

        count_final = len(df)
        removed = count_initial - count_final

        if removed > 0:
            print(f"🧹 Automatically removed {removed} duplicates.")
        else:
            print("✅ Data Clean: No duplicates found.")

        # 3. GENERATE FILENAME WITH TIMESTAMP
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"leads_{timestamp}"

        # 4. EXPORT TO CSV
        csv_path = os.path.join(self.data_dir, f"{filename}.csv")
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')

        # 5. EXPORT TO EXCEL
        excel_path = os.path.join(self.data_dir, f"{filename}.xlsx")
        
        with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Leads Miami')
            
        print(f"\n📂 FILES GENERATED:")
        print(f"   📄 CSV: {csv_path}")
        print(f"   📊 Excel: {excel_path}")
        print("-" * 30)