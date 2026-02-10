import pandas as pd
import os
from datetime import datetime

class DataManager:
    def __init__(self):
        # Definimos dónde se guardarán los archivos
        self.data_dir = "data"
        # Esto crea la carpeta 'data' automáticamente si no existe (muy Pro)
        os.makedirs(self.data_dir, exist_ok=True)

    def process_and_save(self, raw_data_list):
        if not raw_data_list:
            print("⚠️ No hay datos para procesar.")
            return

        print("\n⚙️  Iniciando procesamiento de datos...")

        # 1. CONVERTIR A DATAFRAME (La tabla mágica de Pandas)
        df = pd.DataFrame(raw_data_list)

        # 2. LIMPIEZA Y DEDUPLICACIÓN (El Factor Wow)
        count_initial = len(df)
        
        # Eliminamos si el Nombre Y el Teléfono son idénticos (duplicado exacto)
        df.drop_duplicates(subset=['business_name', 'phone'], keep='first', inplace=True)
        
        # Eliminamos filas donde todo sea N/A (basura)
        df = df[df['business_name'] != "N/A"]

        count_final = len(df)
        removed = count_initial - count_final

        if removed > 0:
            print(f"🧹 Se eliminaron {removed} duplicados automáticamente.")
        else:
            print("✅ Datos limpios: No se encontraron duplicados.")

        # 3. GENERAR NOMBRE DE ARCHIVO CON FECHA
        # Ejemplo: leads_2026-02-10_15-30.xlsx
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"leads_{timestamp}"

        # 4. GUARDAR EN CSV (Respaldo rápido)
        csv_path = os.path.join(self.data_dir, f"{filename}.csv")
        df.to_csv(csv_path, index=False, encoding='utf-8-sig') # utf-8-sig es vital para que Excel lea tildes bien

        # 5. GUARDAR EN EXCEL (Formato Final para el Cliente)
        excel_path = os.path.join(self.data_dir, f"{filename}.xlsx")
        
        # Usamos un "ExcelWriter" para tener control profesional
        with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Leads Miami')
            
        print(f"\n📂 ARCHIVOS GENERADOS:")
        print(f"   📄 CSV: {csv_path}")
        print(f"   📊 Excel: {excel_path}")
        print("-" * 30)