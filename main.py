import json
import os
from pathlib import Path

# 1. Definimos un esquema sencillo para validar
# (Similar al que usamos con jsonschema, pero validación manual para este ejemplo)
def validar_datos(datos):
    campos_requeridos = ["id", "producto", "precio"]
    for campo in campos_requeridos:
        if campo not in datos:
            return False, f"Falta el campo: {campo}"
    return True, "OK"

def procesar_inventario(carpeta_nombre):
    print(f"--- Iniciando procesamiento en: {carpeta_nombre} ---")
    
    reporte = []
    ruta_carpeta = Path(carpeta_nombre)

    # 2. Crear carpeta si no existe (solo para el ejemplo)
    if not ruta_carpeta.exists():
        os.makedirs(ruta_carpeta)
        print(f"📁 Carpeta '{carpeta_nombre}' creada para la prueba.")

    # 3. Iterar sobre archivos .json
    for archivo in ruta_carpeta.glob("*.json"):
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                contenido = json.load(f)
            
            # Validación
            es_valido, msj = validar_datos(contenido)
            
            if es_valido:
                reporte.append(f"✅ {archivo.name}: {contenido['producto']} - ${contenido['precio']}")
            else:
                reporte.append(f"❌ {archivo.name}: Error -> {msj}")
                
        except json.JSONDecodeError:
            reporte.append(f"⚠️ {archivo.name}: No es un JSON válido")

    # 4. Mostrar reporte final
    if not reporte:
        print("No se encontraron archivos para procesar.")
    else:
        print("\n".join(reporte))

# --- Ejecución del ejemplo ---
if __name__ == "__main__":
    # Creamos un archivo de prueba rápido
    with open("datos_prueba.json", "w") as f:
        json.dump({"id": 1, "producto": "Laptop", "precio": 1200}, f)

    # Ejecutamos la lógica
    procesar_inventario(".")