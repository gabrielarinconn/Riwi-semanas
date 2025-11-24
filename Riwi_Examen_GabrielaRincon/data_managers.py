import json
import os

# --- Configuración de Archivos ---
DATA_FILE = 'store_data.json'

# --- Estructuras de Datos Globales ---
inventory_ = []
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
    global inventory_, next_product_id, next_sale_id
    
    inventory_.extend([
        {
            'id': 1,
            'title': 'La Biblia',
            'author': 'Jesus',
            'category': 'Religion',
            'price': 199.99,
            'stock': 15,
        },
        {
            'id': 2,
            'title': 'Cien años de soledad',
            'author': 'Gabriel Garcia Marquez',
            'category': 'Magic Realism',
            'price': 45.50,
            'stock': 30,
        },
        {
            'id': 3,
            'title': 'La Hojarasca',
            'author': 'Laura Restrepo',
            'category': 'History',
            'price': 79.99,
            'stock': 8,
        },
        {
            'id': 4,
            'title': 'Memorias de una Geisha',
            'author': 'Arthur Golden',
            'category': 'Novel',
            'price': 120.00,
            'stock': 20,
        },
        {
            'id': 5,
            'title': 'Los mandamientos',
            'author': 'Jesus',
            'category': 'Religion',
            'price': 150.99,
            'stock': 12,
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
    global inventory_, sales_history, next_product_id, next_sale_id
    
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
                
                inventory_.clear()
                inventory_.extend(data.get('inventory_', []))
                sales_history.clear()
                sales_history.extend(data.get('sales_history', []))
                next_product_id = data.get('next_product_id', 1)
                next_sale_id = data.get('next_sale_id', 101)
                
                print(f"✅ Data loaded successfully from {DATA_FILE}.")
                if not inventory_:
                    print("📝 Inventory was empty in the file. Initializing default products.")
                    initialize_default_data()
                return True
        except json.JSONDecodeError:
            print(f"❌ Error decoding data from {DATA_FILE}. Initializing default data.")
        except Exception as e:
            print(f"❌ An error occurred during data loading: {e}. Initializing default data.")
            
    # If loading fails or file doesn't exist, initialize default data
    if not inventory_:
        initialize_default_data()
        print("📝 Initializing with default preloaded products (and saving them).")
    return False

def save_data():
    """
    Saves the inventory, sales history, and counters to the JSON file.
    """
    data_to_save = {
        'inventory_': inventory_,
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