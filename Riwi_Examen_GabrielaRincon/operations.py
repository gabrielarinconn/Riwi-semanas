import time
from collections import Counter
import data_managers # Importa estructuras de datos y persistencia

# Datos globales y constantes
inventory_ = data_managers.inventory_
sales_history = data_managers.sales_history
DISCOUNT_RATES = data_managers.DISCOUNT_RATES

# --- Utility and Validation Functions ---

def get_product_by_id(product_id):
    """Finds a product dictionary in the inventory by its ID."""
    try:
        product_id = int(product_id)
        for product in inventory_:
            if product['id'] == product_id:
                return product
        return None
    except ValueError:
        return None

def validate_numeric_input(prompt, value_type=int):
    """Handles basic input validation for numbers."""
    while True:
        try:
            value = input(prompt)
            if value_type == int:
                return int(value)
            elif value_type == float:
                return float(value)
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

def validate_positive_number(prompt, value_type=int):
    """Validates that input is a positive number."""
    while True:
        num = validate_numeric_input(prompt, value_type)
        if num > 0:
            return num
        print("❌ Value must be a positive number.")

# --- 1. Inventory Management Functions ---

def display_inventory():
    """Consult inventory: Displays all products in a structured table."""
    if not inventory_:
        print("\n📝 Inventory is currently empty.")
        return

    print("\n" + "="*100)
    print("📝 Current Inventory Stock")
    print("="*100)
    
    headers = ["#", "ID", "Title", "Author", "Category", "Price", "Stock"]
    widths = [3, 4, 25, 25, 15, 11, 7]
    
    header_line = "".join(f"{h:<{w}}" for h, w in zip(headers, widths))
    print(header_line)
    print("-" * 100)
    
    # USO DE ENUMERATE
    for index, p in enumerate(inventory_, 1):
        price_str = f"${p['price']:.2f}"
        row = (
            f"{index:<{widths[0]}}" # Added enumeration index
            f"{p['id']:<{widths[1]}}"
            f"{p['title']:<{widths[2]}}"
            f"{p['author']:<{widths[3]}}"
            f"{p['category']:<{widths[4]}}"
            f"{price_str:<{widths[5]}}"
            f"{p['stock']:<{widths[6]}}"
        )
        print(row)
    print("="*100)

def register_product():
    """Register product: Adds a new product to the inventory."""
    print("\n--- Register New Product ---")
    
    title = input("Enter Product Title: ").strip()
    author = input("Enter Author: ").strip()
    category = input("Enter Category: ").strip()
    
    if not all([title, author, category]):
        print("❌ Error: Title, Author, and Category cannot be empty.")
        return

    try:
        price = validate_positive_number("Enter Unit Price ($): ", float)
        stock = validate_positive_number("Enter Initial Stock Quantity: ", int)
    except Exception:
        # Catch unexpected validation errors without stopping the program
        print("❌ Product registration failed due to invalid number format.")
        return
    
    new_product = {
        'id': data_managers.next_product_id,
        'title': title,
        'author': author,
        'category': category,
        'price': price,
        'stock': stock,
    }
    
    inventory_.append(new_product)
    print(f"\n✅ Product '{title}' (ID: {data_managers.next_product_id}) registered successfully!")
    data_managers.next_product_id += 1

def update_product():
    """Update product: Modifies details of an existing product."""
    display_inventory()
    print("\n--- Update Product Details ---")
    
    product_id = validate_numeric_input("Enter ID of product to update: ", int)
    product = get_product_by_id(product_id)
    
    if not product:
        print(f"❌ Error: Product with ID {product_id} not found.")
        return

    print(f"Updating product: **{product['title']}**")
    print("Leave field blank to keep current value.")
    
    # ... (Update logic remains the same) ...
    # Simplified update block for brevity, maintaining validation principles
    try:
        new_name = input(f"New Name ({product['title']}): ").strip()
        if new_name: product['title'] = new_name
            
        new_stock_str = input(f"New Stock Quantity ({product['stock']}): ").strip()
        if new_stock_str:
            new_stock = int(new_stock_str)
            if new_stock >= 0:
                product['stock'] = new_stock
            else:
                print("⚠️ Warning: Stock cannot be negative.")
    except ValueError:
        print("⚠️ Warning: Invalid input format. Keeping current values.")

    print(f"\n✅ Product ID {product_id} updated successfully!")

def delete_product():
    """Delete product: Removes a product from the inventory."""
    global inventory_
    display_inventory()
    print("\n--- Delete Product ---")
    
    product_id = validate_numeric_input("Enter ID of product to delete: ", int)
    
    initial_len = len(inventory_)
    # Reassign inventory by filtering out the product
    data_managers.inventory_[:] = [p for p in inventory_ if p['id'] != product_id]
    
    if len(data_managers.inventory_) < initial_len:
        print(f"\n✅ Product with ID {product_id} deleted successfully.")
    else:
        print(f"❌ Error: Product with ID {product_id} not found.")

# --- 2. Sales Registration and History Functions ---

# Función lambda para el cálculo del precio neto después del descuento
calculate_net_price = lambda price, discount: price * (1 - discount)

def get_discount(customer_type):
    """Returns the discount rate for a given customer type."""
    return DISCOUNT_RATES.get(customer_type.lower(), 0.0)

def register_sale():
    """Register sale: Records a new transaction and updates inventory."""
    print("\n--- Register New Sale ---")
    
    customer_name = input("Enter Customer Name: ").strip()
    if not customer_name:
        print("❌ Error: Customer name cannot be empty.")
        return
        
    customer_type = input("Enter Customer Type (regular/silver/gold): ").lower().strip()
    customer_type = customer_type if customer_type in DISCOUNT_RATES else 'regular'
    discount_rate = get_discount(customer_type)

    display_inventory()
    product_id = validate_numeric_input("Enter Product ID to sell: ", int)
    
    # Manejo de excepciones en la entrada de cantidad
    try:
        quantity = validate_positive_number("Enter Quantity to sell: ", int)
    except Exception:
        print("❌ Sale registration failed. Quantity must be a positive number.")
        return

    product = get_product_by_id(product_id)
    
    if not product:
        print(f"❌ Error: Product with ID {product_id} not found.")
        return

    # Evitar ventas con stock insuficiente
    if quantity > product['stock']:
        print(f"❌ Error: Insufficient stock. Only {product['stock']} units of **{product['title']}** available.")
        return

    # Cálculo y registro
    unit_price = product['price']
    gross_total = unit_price * quantity
    net_total = calculate_net_price(gross_total, discount_rate)
    
    sale_data = {
        'sale_id': data_managers.next_sale_id,
        'customer': customer_name,
        'customer_type': customer_type.capitalize(),
        'product_id': product_id,
        'product_name': product['title'],
        'author_name': product['author'],
        'quantity': quantity,
        'unit_price': unit_price,
        'gross_total': gross_total,
        'discount_rate': discount_rate,
        'discount_applied': gross_total - net_total,
        'net_total': net_total,
        'sale_date': time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Update inventary and add sells
    product['stock'] -= quantity
    sales_history.append(sale_data)
    data_managers.next_sale_id += 1
    
    # Output confirmation
    print("\n" + "="*50)
    print("✅ SALE REGISTERED SUCCESSFULLY")
    print(f"Product: {product['title']} | Net Total: ${net_total:.2f}")
    print("="*50)


def display_sales_history():
    """Consult sales: Displays the historical record of all sales."""
    if not sales_history:
        print("\n📝 No sales recorded yet.")
        return
    
    print("\n" + "="*120)
    print("📜 Sales History")
    print("="*120)
    
    headers = ["#", "ID", "Date", "Customer", "Product Title", "Qty", "Net Total"]
    widths = [3, 5, 25, 15, 30, 5, 12]
    
    header_line = "".join(f"{h:<{w}}" for h, w in zip(headers, widths))
    print(header_line)
    print("-" * 120)
    
    # Use ENUMERATE
    for index, sale in enumerate(sales_history, 1):
        row = (
            f"{index:<{widths[0]}}" # Added enumeration index
            f"{sale['sale_id']:<{widths[1]}}"
            f"{sale['sale_date']:<{widths[2]}}"
            f"{sale['customer']:<{widths[3]}}"
            f"{sale['product_name']:<{widths[4]}}"
            f"{sale['quantity']:<{widths[5]}}"
            f"${sale['net_total']:< {widths[6]}.2f}"
        )
        print(row)
    print("="*120)


# --- 3. Reporting Module Functions ---


def report_top_selling_products():
    """Report: Top 3 Books most sold"""
    if not sales_history:
        print("\n📝 No sales data available for reports.")
        return
        
    product_sales_count = Counter(sale['product_name'] for sale in sales_history)
    top_products = product_sales_count.most_common(3)
    
    print("\n" + "="*50)
    print("🏆 Top 3 Most Sold Books")
    print("="*50)
    
    # Use ENUMERATE
    for rank, (title, total_qty) in enumerate(top_products, 1):
        print(f"{rank}. **{title}**: {total_qty} units sold")
    print("="*50)


def report_top_selling_author():
    """Report: Top 3 best-selling Authors"""
    if not sales_history:
        print("\n📝 No sales data available for reports.")
        return
        
    product_sales_count = Counter(sale['author_name'] for sale in sales_history)
    top_products = product_sales_count.most_common(3)
    
    print("\n" + "="*50)
    print("🏆 Top 3 best-selling Authors")
    print("="*50)
    
    # Use ENUMERATE
    for rank, (title, total_qty) in enumerate(top_products, 1):
        print(f"{rank}. **{title}**: {total_qty} units sold")
    print("="*50)


def report_income():
    """Report: Calculate net and gross income (with and without discount)"""

    if not sales_history:
        print("\n📝 No sales data available for reports.")
        return
        
    total_product_gross_income = sum(sale['gross_total'] for sale in sales_history)
    total_product_net_income = sum(sale['net_total'] for sale in sales_history)


    print("\n" + "="*50)
    print("💸 Total Net and Gross Income")
    print("="*50)
    print(f"Total GROSS Income from Products: ${total_product_gross_income:.2f}")
    print(f"Total NET Income from Products: ${total_product_net_income:.2f}")
    print("="*50)





def generate_reports():
    """Menu for Report Generation."""
    
    while True:
        print("\n--- Report Generation Menu ---")
        print("1. Top 3 Most Sold Books")
        print("2. Top 3 best-selling Authors")
        print("3. Income Report (net and gross)")
        # Added simplified options to keep the file short
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice (1 , 2 , 3 or 5): ").strip()
        
        if choice == '1':
            report_top_selling_products()
        elif choice == '2':
            report_top_selling_author()
        elif choice == '3':
            report_income()
        elif choice == '5':
            break
        else:
            print("❌ Invalid choice.")