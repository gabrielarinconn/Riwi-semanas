import datetime
# Importamos todas las funciones y datos de nuestro módulo de gestión de datos
import data_manager as dm 

# --- 1. Utility Function ---
def get_valid_input(prompt, data_type=str, min_val=None):
    """Handles basic input validation."""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("Error: Input cannot be empty.")
                continue
            
            # Conversion and validation logic...
            if data_type == int:
                value = int(user_input)
                if min_val is not None and value < min_val:
                    print(f"Error: Value must be at least {min_val}.")
                    continue
            # ... (Rest of int/float/str validation) ...
            elif data_type == float:
                value = float(user_input)
                if min_val is not None and value < min_val:
                    print(f"Error: Value must be at least {min_val}.")
                    continue
            else: 
                value = user_input
            
            return value
        except ValueError:
            print(f"Error: Invalid input. Please enter a valid {data_type.__name__}.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# --- 2. Inventory Management Functions ---

def register_product():
    """Adds a new product to the inventory and saves data."""
    # Obtenemos la referencia al diccionario de inventario
    INVENTORY = dm.get_inventory()
    
    print("\n--- Register New Product ---")
    name = get_valid_input("Enter product name: ")
    
    if name in INVENTORY:
        print(f"Error: Product '{name}' already exists.")
        return

    brand = get_valid_input("Enter product brand: ")
    category = get_valid_input("Enter product category: ")
    price = get_valid_input("Enter unit price (float): ", float, min_val=0.01)
    stock = get_valid_input("Enter quantity in stock (int): ", int, min_val=0)
    warranty = get_valid_input("Enter warranty in months (int): ", int, min_val=1)

    INVENTORY[name] = {
        "brand": brand,
        "category": category,
        "price": price,
        "stock": stock,
        "warranty_months": warranty
    }
    print(f"\nSUCCESS: Product '{name}' registered.")
    dm.save_data() # Guardamos datos usando la función del otro módulo

# ... (El resto de funciones de inventario: view_inventory, update_product, delete_product) ...
# ¡Deben usar dm.get_inventory() al inicio y dm.save_data() al final!


# --- 3. Sales Management Functions ---

def record_sale():
    """Records a new sale, validates stock, updates inventory, and saves data."""
    INVENTORY = dm.get_inventory()
    SALES_HISTORY = dm.get_sales_history()
    
    print("\n--- Record New Sale ---")
    
    # ... (Detalles y validación) ...
    client_name = get_valid_input("Enter customer name: ")
    
    customer_type = ""
    while customer_type not in dm.DISCOUNT_RATES:
        customer_type = get_valid_input("Enter customer type (Standard/Premium): ").capitalize()
        if customer_type not in dm.DISCOUNT_RATES:
            print("Invalid customer type.")

    product_name = get_valid_input("Enter product name sold: ")
    if product_name not in INVENTORY:
        print(f"Error: Product '{product_name}' not found.")
        return

    # 4. Calculation and Record
    product = INVENTORY[product_name]
    available_stock = product['stock']
    quantity_sold = get_valid_input(f"Enter quantity sold (max {available_stock}): ", int, min_val=1)
    
    if quantity_sold > available_stock:
        print(f"Error: Insufficient stock. Only {available_stock} units available.")
        return

    discount_rate = dm.DISCOUNT_RATES[customer_type]
    unit_price = product['price']
    calculate_discount_amount = lambda price, rate: price * rate
    
    discount_amount = calculate_discount_amount(unit_price * quantity_sold, discount_rate)
    final_sale_price = (unit_price * quantity_sold) - discount_amount

    # Update Inventory and Record Sale
    product['stock'] -= quantity_sold
    
    SALES_HISTORY.append({
        # ... (Resto de detalles de la venta) ...
        "client": client_name,
        "type": customer_type,
        "product": product_name,
        "quantity": quantity_sold,
        "unit_price": unit_price,
        "discount_applied": discount_amount,
        "final_price": final_sale_price,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    print(f"\nSUCCESS: Sale recorded. Total: ${final_sale_price:.2f}")
    dm.save_data() # Guardamos datos usando la función del otro módulo

# ... (El resto de funciones de ventas y reportes, utilizando dm.get_sales_history() y dm.get_inventory()) ...

def report_top_selling():
    """Calculates and prints the Top 3 products by quantity sold."""
    SALES_HISTORY = dm.get_sales_history()
    # ... (Logic remains the same) ...
    if not SALES_HISTORY:
        print("No sales data to generate report.")
        return
    
    sales_by_product = {}
    for sale in SALES_HISTORY:
        prod = sale['product']
        qty = sale['quantity']
        sales_by_product[prod] = sales_by_product.get(prod, 0) + qty
        
    sorted_sales = sorted(sales_by_product.items(), key=lambda item: item[1], reverse=True)
    
    print("\n--- Top 3 Bestselling Products ---")
    for i, (product, quantity) in enumerate(sorted_sales[:3]):
        print(f"{i+1}. {product}: {quantity} units sold")
    print("-" * 30)

# Incluir aquí todas las demás funciones de reporte y consulta
# view_inventory, update_product, delete_product, view_sales_history, generate_reports, etc.
# y asegúrate de que usen dm.get_inventory() y dm.get_sales_history()