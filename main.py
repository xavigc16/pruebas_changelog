import argparse
import logging
import sys
from datetime import datetime

# 1. Configuración de Logging para ver qué pasa en los logs de GitHub Actions
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def procesar_tarea(nombre_tarea, dry_run=False):
    """
    Aquí va la lógica principal de tu script.
    """
    logger.info(f"Iniciando tarea: {nombre_tarea}")
    
    if dry_run:
        logger.info("Modo 'dry-run' activo: No se realizarán cambios permanentes.")
        return

    # --- Simulación de lógica ---
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"Procesando datos a las {ahora}...")
    
    # Aquí podrías llamar a tus funciones de validación JSON o peticiones API
    return True

def main():
    # 2. Configuración de Argumentos (Argparse)
    parser = argparse.ArgumentParser(description="Script genérico para automatizaciones.")
    
    parser.add_argument(
        "--task-namename", 
        type=str, 
        default="Tarea-Default", 
        help="Nombre de la operación a realizar"
    )
    
    parser.add_argument(
        "--dry-run", 
        action="store_true", 
        help="Ejecuta el script sin aplicar cambios reales"
    )

    args = parser.parse_args()

    # 3. Ejecución principal con control de errores
    try:
        exito = procesar_tarea(args.name, args.dry_run)
        if exito:
            logger.info("✅ Proceso finalizado correctamente.")
        else:
            logger.warning("⚠️ El proceso terminó con advertencias.")
            
    except Exception as e:
        logger.error(f"❌ Error crítico durante la ejecución: {e}", exc_info=True)
        sys.exit(1) # Salida con error para que GitHub Actions marque el job como fallido

if __name__ == "__main__":
    main()