import json
import os

# --- Configuración de Archivos ---
DATA_FILE = 'store_data.json'

# --- Estructuras de Datos Globales ---
inventory = []
sales_history = []
next_product_id = 1
next_sale_id = 101

# --- Constantes de Negocio ---
DISCOUNT_RATES = {
    'regular': 0.0,
    'silver': 0.05,  # 5% discount
    'gold': 0.10     # 10% discount
}

def initialize_default_data():
    """
    Creates the 5 initial preloaded products if no data file is found.
    """
    global inventory, next_product_id, next_sale_id
    
    inventory.extend([
        {
            'id': 1,
            'name': 'LED Monitor 27"',
            'brand': 'TechView',
            'category': 'Peripherals',
            'price': 199.99,
            'stock': 15,
            'warranty_months': 24
        },
        {
            'id': 2,
            'name': 'Wireless Keyboard',
            'brand': 'ErgoKeys',
            'category': 'Peripherals',
            'price': 45.50,
            'stock': 30,
            'warranty_months': 12
        },
        {
            'id': 3,
            'name': 'Gaming Mouse Pro',
            'brand': 'GameMax',
            'category': 'Peripherals',
            'price': 79.99,
            'stock': 8,
            'warranty_months': 18
        },
        {
            'id': 4,
            'name': 'External SSD 1TB',
            'brand': 'FastStore',
            'category': 'Storage',
            'price': 120.00,
            'stock': 20,
            'warranty_months': 36
        },
        {
            'id': 5,
            'name': 'Noise Cancelling Headphones',
            'brand': 'SoundWave',
            'category': 'Audio',
            'price': 150.99,
            'stock': 12,
            'warranty_months': 12
        }
    ])
    next_product_id = 6
    next_sale_id = 101
    
    # Save default data immediately so it's persistent
    save_data()


def load_data():
    """
    Loads data from the JSON file. Initializes with default data if file is missing.
    """
    global inventory, sales_history, next_product_id, next_sale_id
    
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
                
                inventory.clear()
                inventory.extend(data.get('inventory', []))
                sales_history.clear()
                sales_history.extend(data.get('sales_history', []))
                next_product_id = data.get('next_product_id', 1)
                next_sale_id = data.get('next_sale_id', 101)
                
                print(f"✅ Data loaded successfully from {DATA_FILE}.")
                if not inventory:
                    print("📝 Inventory was empty in the file. Initializing default products.")
                    initialize_default_data()
                return True
        except json.JSONDecodeError:
            print(f"❌ Error decoding data from {DATA_FILE}. Initializing default data.")
        except Exception as e:
            print(f"❌ An error occurred during data loading: {e}. Initializing default data.")
            
    # If loading fails or file doesn't exist, initialize default data
    if not inventory:
        initialize_default_data()
        print("📝 Initializing with default preloaded products (and saving them).")
    return False

def save_data():
    """
    Saves the inventory, sales history, and counters to the JSON file.
    """
    data_to_save = {
        'inventory': inventory,
        'sales_history': sales_history,
        'next_product_id': next_product_id,
        'next_sale_id': next_sale_id
    }
    
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data_to_save, f, indent=4)
        print(f"\n💾 All data saved successfully to {DATA_FILE}.")
        return True
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR: Could not save data to file {DATA_FILE}. {e}")
        return False