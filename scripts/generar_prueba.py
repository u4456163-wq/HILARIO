import pandas as pd
from pathlib import Path

# Definimos la ruta de salida (dentro del contenedor es /app/data/...)
OUTPUT_PATH = Path("data/output_excel/Reporte_Hilario_Abril.xlsx")

def generar_excel_prueba():
    print(" Iniciando generación de reporte de prueba...")
    
    # Inventamos datos de facturas de "Aetón" y "Pulsar"
    datos = [
        {"Fecha": "2026-04-01", "Concepto": "Motores Nema 17 - Aetón", "Monto": 1500.00, "Tipo": "Gasto", "Status": "PAGADA"},
        {"Fecha": "2026-04-02", "Concepto": "Sensores MAX30102 - Pulsar", "Monto": 450.00, "Tipo": "Gasto", "Status": "PAGADA"},
        {"Fecha": "2026-04-03", "Concepto": "Servicios Contables Hilario", "Monto": 2500.00, "Tipo": "Ingreso", "Status": "PENDIENTE"},
        {"Fecha": "2026-04-04", "Concepto": "Rodamientos 608RS", "Monto": 120.50, "Tipo": "Gasto", "Status": "PAGADA"},
    ]
    
    df = pd.DataFrame(datos)
    
    # Creamos el archivo Excel con formato profesional
    with pd.ExcelWriter(OUTPUT_PATH, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Integración SAT')
        
        # Aquí podrías agregar lógica de formato (colores, negritas) después
        
    print(f" ¡Éxito! El archivo se guardó en: {OUTPUT_PATH}")

if __name__ == "__main__":
    generar_excel_prueba()
