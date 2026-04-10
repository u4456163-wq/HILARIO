import time
import os
import logging
import xml.etree.ElementTree as ET
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Asumiendo que tu estructura de carpetas es correcta
from hilario.infrastructure.xml_parser import SATParser

# Configuración de Logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

INPUT_DIR = "data/input_xml"

class XMLHandler(FileSystemEventHandler):
    def __init__(self):
        self.parser = SATParser()

    def on_created(self, event):
        # Filtro básico: ignorar carpetas y archivos que no sean .xml
        if event.is_directory or not event.src_path.endswith('.xml'):
            return
        
        print(f"\n DEBUG: Detectado movimiento en: {os.path.basename(event.src_path)}")
        self.procesar_archivo(event.src_path)

    def procesar_archivo(self, file_path):
        # Pausa para que el SO termine de escribir el archivo
        time.sleep(0.5)
        
        try:
            # 1. Analizamos el ADN del archivo (el Root Tag)
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            # Limpiamos el tag por si trae Namespaces (ej: {http://...}Comprobante)
            tag_limpio = root.tag.split('}')[-1].lower() 

            # 2. SECCIÓN CONTABILIDAD (Facturas SAT)
            if tag_limpio == 'comprobante':
                print(f" [SAT] Procesando factura para el abuelo...")
                datos = self.parser.extraer_datos(file_path)
                
                if datos:
                    emisor = datos.get('Nombre_Emisor', 'Desconocido')
                    total = datos.get('Total', 0.0)
                    cfdi = datos.get('CFDI', 'N/A')
                    rfc = datos.get('RFC_Emisor', 'N/A')
                    regimen_fiscal = datos.get('Regimen_Fiscal', 'N/A')
                    sub_total = datos.get('SubTotal', 0.0)
                    tipo_de_moneda = datos.get('TipoDeMoneda', 'N/A')
                    emisor_rfc = datos.get('RFC_Emisor', 'N/A')
                    regimen_fiscal_emisor = datos.get('Regimen_Fiscal_Emisor', 'N/A')
                    uso_cfdi = datos.get('UsoCFDI', 'N/A')
                    nombre_receptor = datos.get('Nombre_Receptor', 'Desconocido')
                    rfc_receptor = datos.get('RFC_Receptor', 'N/A')
                    Domicilio_Fiscal_Receptor = datos.get('Domicilio_Fiscal_Receptor', 'N/A')
                    cfdi_Impuestos = datos.get('CFDI_Impuestos', [])
                    TotalImpuestosTrasladados=datos.get('TotalImpuestosTrasladados', '0.00')
                    TotalImpuestosRetenidos=datos.get('TotalImpuestosRetenidos', '0.00')
                    cfdi_conceptos = datos.get('CFDI_Conceptos', [])
                    cfdi_complemento = datos.get('CFDI_Complemento', {})
                    cfdi_retenciones = datos.get('CFDI_Retenciones', [])
                    Base = datos.get('Base', '0.00') 
                    Impuesto = datos.get('Impuesto', '0.00')
                    TipoFactor = datos.get('TipoFactor', 'N/A')
                    TasaOCuota = datos.get('TasaOCuota', '0.00')
                    Importe= datos.get('Importe', '0.00')
                    traslados = datos.get('Traslados', [])
                    retenciones = datos.get('Retenciones', [])
                    cfdi_Traslado = datos.get('CFDI_Traslado', {})
                    Base = datos.get('Base', '0.00')
                    Impuesto = datos.get('Impuesto', '0.00')
                    TipoFactor = datos.get('TipoFactor', 'N/A')
                    TasaOCuota = datos.get('TasaOCuota', '0.00')
                    cfdi_Concepto = datos.get('CFDI_Concepto', {}) 
                    ClaveProdServ=datos.get('ClaveProdServ', 'N/A')
                    Cantidad = datos.get('Cantidad', '0.00')
                    ClaveUnidad = datos.get('ClaveUnidad', 'N/A')
                    Unidad = datos.get('Unidad', 'N/A')
                    Descripcion=datos.get('Descripcion', 'N/A')
                    ValorUnitario = datos.get('ValorUnitario', '0.00')
                    Importe = datos.get('Importe', '0.00')
                    ObjetoImpuesto = datos.get('ObjetoImpuesto', 'N/A')

                    print(f" EXCEL LISTO: {emisor} por ${total:.2f}")
                else:
                    print(" El parser no pudo extraer datos de esta factura.")

            # 3. SECCIÓN ROBÓTICA (ROS / URDF)
            elif tag_limpio in ['package', 'robot']:
                # Buscamos el nombre en el XML o usamos el nombre del archivo
                nombre_proyecto = root.findtext('name') or os.path.basename(file_path)
                print(f" [ROBÓTICA] Detectado componente: {nombre_proyecto}")
                print(f" Tipo de archivo: {tag_limpio.upper()}")
            
            # 4. OTROS
            else:
                print(f" XML detectado pero no clasificado: <{tag_limpio}>")

        except Exception as e:
            print(f" Error analizando el archivo {os.path.basename(file_path)}: {e}")

if __name__ == "__main__":
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)
        print(f" Carpeta creada: {INPUT_DIR}")

    print(f" HILARIO activo y blindado. Vigilando: {INPUT_DIR}")

    event_handler = XMLHandler()
    observer = Observer()
    observer.schedule(event_handler, INPUT_DIR, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n Deteniendo HILARIO...")
        observer.stop()
    
    observer.join()