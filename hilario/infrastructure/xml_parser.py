import lxml.etree as etree
import pandas as pd
from pathlib import Path

class SATParser:
    def __init__(self):
        # Namespaces estándar del SAT para CFDI 4.0
        self.ns = {
            'cfdi': 'http://www.sat.gob.mx/cfd/4',
            'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital'
        }

    def extraer_datos(self, ruta_xml):
        try:
            tree = etree.parse(ruta_xml)
            root = tree.getroot()

            # Extraer datos principales
            emisor = root.xpath('//cfdi:Emisor', namespaces=self.ns)[0]
            receptor = root.xpath('//cfdi:Receptor', namespaces=self.ns)[0]
            timbre = root.xpath('//tfd:TimbreFiscalDigital', namespaces=self.ns)[0]
            
            datos = {
                'UUID': timbre.get('UUID'),
                'Fecha': root.get('Fecha'),
                'RFC_Emisor': emisor.get('Rfc'),
                'Nombre_Emisor': emisor.get('Nombre'),
                'RFC_Receptor': receptor.get('Rfc'),
                'Total': float(root.get('Total')),
                'MetodoPago': root.get('MetodoPago') # PUE o PPD
            }
            return datos
        except Exception as e:
            return {"error": f"No se pudo procesar {ruta_xml}: {e}"}

# Prueba rápida
if __name__ == "__main__":
    print("Parser de HILARIO listo para la acción.")
