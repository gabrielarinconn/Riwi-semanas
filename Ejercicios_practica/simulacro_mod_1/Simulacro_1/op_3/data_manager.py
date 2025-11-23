import os
import json

# --- Configuración de Archivos ---
INVENTORY_FILE = "inventory_data.json"
SALES_FILE = "sales_data.json"

# --- Variables Globales de Datos ---
INVENTORY = {}
SALES_HISTORY = []

DISCOUNT_RATES = {
    "Standard": 0.00,
    "Premium": 0.10
}

# --- Funciones de Persistencia ---

def load_data():
    """Carga inventario y ventas de archivos JSON al iniciar."""
    global INVENTORY, SALES_HISTORY
    
    # Intenta cargar el inventario
    if os.path.exists(INVENTORY_FILE):
        try:
            with open(INVENTORY_FILE, 'r') as f:
                INVENTORY = json.load(f)
            print(f"Loaded {len(INVENTORY)} products.")
        except json.JSONDecodeError:
            print("Warning: Inventory file corrupted. Initializing empty.")
            INVENTORY = {}
    else:
        # Inicialización con 5 productos precargados (Requisito)
        print("Inventory file not found. Initializing with default products.")
        INVENTORY = {
            "Laptop X1": {"brand": "TechCorp", "category": "Computers", "price": 1200.00, "stock": 10, "warranty_months": 24},
            "Smartphone Z": {"brand": "MobilePro", "category": "Phones", "price": 750.00, "stock": 25, "warranty_months": 12},
            "Wireless Mouse A": {"brand": "AccessoryCo", "category": "Peripherals", "price": 25.00, "stock": 100, "warranty_months": 6},
            "Monitor 4K": {"brand": "ViewMaster", "category": "Peripherals", "price": 450.00, "stock": 15, "warranty_months": 36},
            "Earbuds Pro": {"brand": "SoundWave", "category": "Audio", "price": 150.00, "stock": 50, "warranty_months": 18}
        }

    # Intenta cargar el historial de ventas
    if os.path.exists(SALES_FILE):
        try:
            with open(SALES_FILE, 'r') as f:
                SALES_HISTORY = json.load(f)
            print(f"Loaded {len(SALES_HISTORY)} sales records.")
        except json.JSONDecodeError:
            print("Warning: Sales file corrupted. Initializing empty.")
            SALES_HISTORY = []
    
def save_data():
    """Guarda el inventario y las ventas en archivos JSON."""
    try:
        with open(INVENTORY_FILE, 'w') as f:
            json.dump(INVENTORY, f, indent=4)
        
        with open(SALES_FILE, 'w') as f:
            json.dump(SALES_HISTORY, f, indent=4)
            
        # print("DATA SAVED.") # Se puede comentar para no saturar la consola
    except IOError as e:
        print(f"CRITICAL ERROR: Could not write data to files. {e}")

# --- Función de Acceso ---
def get_inventory():
    """Retorna la referencia actual del inventario."""
    return INVENTORY

def get_sales_history():
    """Retorna la referencia actual del historial de ventas."""
    return SALES_HISTORY