import datetime
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
            
            if data_type == int:
                value = int(user_input)
                if min_val is not None and value < min_val:
                    print(f"Error: Value must be at least {min_val}.")
                    continue
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
        "brand": brand, "category": category, "price": price, 
        "stock": stock, "warranty_months": warranty
    }
    print(f"\nSUCCESS: Product '{name}' registered.")
    dm.save_data()

def view_inventory():
    """Displays all products in the inventory."""
    INVENTORY = dm.get_inventory()
    if not INVENTORY:
        print("\nInventory is empty.")
        return
    print("\n--- Current Inventory Status ---")
    for name, data in INVENTORY.items():
        print(f"Product: {name}")
        print(f"  Brand: {data['brand']}, Category: {data['category']}")
        print(f"  Price: ${data['price']:.2f}, Stock: {data['stock']}, Warranty: {data['warranty_months']} months")
    print("-" * 30)

def update_product():
    """Updates the stock or price of an existing product and saves data."""
    INVENTORY = dm.get_inventory()
    print("\n--- Update Product Details ---")
    name = get_valid_input("Enter product name to update: ")
    if name not in INVENTORY:
        print(f"Error: Product '{name}' not found.")
        return
    print(f"Current Stock: {INVENTORY[name]['stock']}, Current Price: ${INVENTORY[name]['price']:.2f}")
    try:
        choice = get_valid_input("Update (S)tock or (P)rice? [S/P]: ", str).upper()
        if choice == 'S':
            new_stock = get_valid_input("Enter new stock quantity (int): ", int, min_val=0)
            INVENTORY[name]['stock'] = new_stock
            print(f"SUCCESS: Stock for '{name}' updated to {new_stock}.")
            dm.save_data()
        elif choice == 'P':
            new_price = get_valid_input("Enter new price (float): ", float, min_val=0.01)
            INVENTORY[name]['price'] = new_price
            print(f"SUCCESS: Price for '{name}' updated to ${new_price:.2f}.")
            dm.save_data()
        else:
            print("Invalid choice. No updates performed.")
    except Exception as e:
        print(f"An error occurred during update: {e}")

def delete_product():
    """Deletes a product from the inventory and saves data."""
    INVENTORY = dm.get_inventory()
    print("\n--- Delete Product ---")
    name = get_valid_input("Enter product name to delete: ")
    if name in INVENTORY:
        del INVENTORY[name]
        print(f"SUCCESS: Product '{name}' deleted.")
        dm.save_data()
    else:
        print(f"Error: Product '{name}' not found.")


# --- 3. Sales Management Functions ---

def record_sale():
    """Records a new sale, validates stock, updates inventory, and saves data."""
    INVENTORY = dm.get_inventory()
    SALES_HISTORY = dm.get_sales_history()
    print("\n--- Record New Sale ---")
    
    client_name = get_valid_input("Enter customer name: ")
    customer_type = ""
    while customer_type not in dm.DISCOUNT_RATES:
        customer_type = get_valid_input("Enter customer type (Standard/Premium): ").capitalize()
        if customer_type not in dm.DISCOUNT_RATES:
            print("Invalid customer type. Choose 'Standard' or 'Premium'.")

    product_name = get_valid_input("Enter product name sold: ")
    if product_name not in INVENTORY:
        print(f"Error: Product '{product_name}' not found.")
        return

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

    product['stock'] -= quantity_sold
    
    SALES_HISTORY.append({
        "client": client_name, "type": customer_type, "product": product_name, 
        "quantity": quantity_sold, "unit_price": unit_price, "discount_applied": discount_amount,
        "final_price": final_sale_price, "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    print(f"\nSUCCESS: Sale recorded. Total: ${final_sale_price:.2f}")
    dm.save_data()

def view_sales_history():
    """Displays all sales records."""
    SALES_HISTORY = dm.get_sales_history()
    if not SALES_HISTORY:
        print("\nNo sales recorded yet.")
        return

    print("\n--- Sales History ---")
    for i, sale in enumerate(SALES_HISTORY):
        print(f"Sale #{i+1} ({sale['date']})")
        print(f"  Client: {sale['client']} ({sale['type']})")
        print(f"  Product: {sale['product']} x{sale['quantity']}")
        print(f"  Discount: ${sale['discount_applied']:.2f}, Final Total: ${sale['final_price']:.2f}")
    print("-" * 30)

# --- 4. Reporting Functions (Reportes solo implementan Top Selling para ejemplo de modularidad) ---

def report_top_selling():
    """Calculates and prints the Top 3 products by quantity sold."""
    SALES_HISTORY = dm.get_sales_history()
    if not SALES_HISTORY:
        print("No sales recorded yet.")