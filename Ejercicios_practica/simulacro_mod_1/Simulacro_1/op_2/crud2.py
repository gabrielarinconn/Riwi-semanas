# ----------------------------------------------------------------------
# 📚 Global Data and Initialization (NO external libraries like pandas)
# ----------------------------------------------------------------------

# Global list to store product dictionaries
inventory_list = [
    # Pre-loaded products
    {
        'id': 101,
        'name': 'Laptop ProBook X',
        'brand': 'TechCorp',
        'category': 'Computers',
        'price': 1250.00,
        'stock': 15,
        'warranty': 24
    },
    {
        'id': 102,
        'name': 'Noise Cancelling Headphones',
        'brand': 'AudioMax',
        'category': 'Audio',
        'price': 199.99,
        'stock': 45,
        'warranty': 12
    },
    {
        'id': 103,
        'name': '4K Smart TV 55"',
        'brand': 'ViewStar',
        'category': 'Televisions',
        'price': 789.50,
        'stock': 20,
        'warranty': 36
    },
    {
        'id': 104,
        'name': 'Wireless Gaming Mouse',
        'brand': 'GameOn',
        'category': 'Peripherals',
        'price': 45.99,
        'stock': 110,
        'warranty': 6
    },
    {
        'id': 105,
        'name': 'Portable Power Bank',
        'brand': 'ChargeQuick',
        'category': 'Accessories',
        'price': 35.00,
        'stock': 75,
        'warranty': 3
    }
]

# Simple ID management
def get_next_id():
    """Generates a sequential unique ID for new products."""
    if not inventory_list:
        return 101
    return max(p['id'] for p in inventory_list) + 1

# ----------------------------------------------------------------------
# 🔧 Helper Function for Input Validation
# ----------------------------------------------------------------------

def get_validated_input(prompt, value_type, min_value=0, allow_zero=True):
    """Handles repeated input until a valid number is provided."""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                raise ValueError("Input cannot be empty.")
            
            value = value_type(user_input)
            
            if not allow_zero and value <= min_value:
                print(f"❌ Error: Value must be positive (greater than {min_value}).")
                continue
            elif allow_zero and value < min_value:
                print(f"❌ Error: Value cannot be negative.")
                continue
                
            return value
        except ValueError:
            print(f"❌ Error: Invalid input. Please enter a correct {value_type.__name__}.")
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")

# ----------------------------------------------------------------------
# 1. Add Product Function (Create)
# ----------------------------------------------------------------------

def add_inventory():
    """Adds a new product to the inventory list with input validation."""
    print("\n---- 1. Add Product to Inventory ----")
    
    # Collecting string inputs
    name = input("▶ Type product Name: ").strip().title()
    brand = input("▶ Type product Brand: ").strip().title()
    category = input("▶ Type product Category: ").strip().title()
    
    # Collecting validated numerical inputs
    price = get_validated_input("▶ Type Unit Price (e.g., 1250.00): ", float, min_value=0, allow_zero=False)
    stock = get_validated_input("▶ Type Quantity in Stock: ", int, min_value=0, allow_zero=True)
    warranty = get_validated_input("▶ Type Warranty in Months: ", int, min_value=0, allow_zero=True)

    # Create product dictionary
    new_product ={
        "id": get_next_id(),
        "name": name,
        "brand": brand,
        "category": category,
        "price": round(price, 2), 
        "stock": stock, 
        "warranty": warranty
    }
    
    inventory_list.append(new_product)
    print(f"\n✅ SUCCESS: Product '{name}' (ID: {new_product['id']}) added to inventory.")

# ----------------------------------------------------------------------
# 2. List Inventory Function (Read) - PURE PYTHON TABLE
# ----------------------------------------------------------------------

def list_inventory():
    """Displays the entire inventory in a clean, tabular format using only Python string formatting."""
    print("\n---- 2. Current Product Inventory ----")
    if not inventory_list:
        print("The inventory is currently empty.")
        return

    # Determine the required width for each column based on the longest data/header
    col_widths = {
        'ID': 4, 'Name': 10, 'Brand': 8, 'Category': 10, 'Price': 12, 'Stock': 5, 'Warranty': 8
    }

    # Recalculate widths based on actual data
    for product in inventory_list:
        col_widths['ID'] = max(col_widths['ID'], len(str(product['id'])))
        col_widths['Name'] = max(col_widths['Name'], len(product['name']))
        col_widths['Brand'] = max(col_widths['Brand'], len(product['brand']))
        col_widths['Category'] = max(col_widths['Category'], len(product['category']))
        col_widths['Price'] = max(col_widths['Price'], len(f"${product['price']:.2f}"))
        col_widths['Stock'] = max(col_widths['Stock'], len(str(product['stock'])))
        col_widths['Warranty'] = max(col_widths['Warranty'], len(f"{product['warranty']}m"))
        
    # Add padding for visual appeal
    padding = 2
    for key in col_widths:
        col_widths[key] += padding

    # Define the format string using the calculated widths
    header_format = (
        f"{{:<{col_widths['ID']}}}"  # ID (Left Align)
        f"{{:<{col_widths['Name']}}}"  # Name (Left Align)
        f"{{:<{col_widths['Brand']}}}" # Brand (Left Align)
        f"{{:<{col_widths['Category']}}}" # Category (Left Align)
        f"{{:>{col_widths['Price']}}}" # Price (Right Align)
        f"{{:>{col_widths['Stock']}}}" # Stock (Right Align)
        f"{{:>{col_widths['Warranty']}}}" # Warranty (Right Align)
    )
    
    # 1. Print Header
    header = header_format.format('ID', 'Name', 'Brand', 'Category', 'Price (USD)', 'Stock', 'Warranty (M)')
    print(header)
    
    # 2. Print Separator
    print("-" * (len(header) + 1))
    
    # 3. Print Data Rows
    for p in inventory_list:
        print(header_format.format(
            p['id'],
            p['name'],
            p['brand'],
            p['category'],
            f"${p['price']:.2f}",
            p['stock'],
            f"{p['warranty']}m"
        ))
    
    print("-" * (len(header) + 1))


# ----------------------------------------------------------------------
# 3. Update Product Function (Update)
# ----------------------------------------------------------------------

def update_product():
    """Updates stock or price for an existing product."""
    print("\n---- 3. Update Product Details ----")
    list_inventory()
    
    try:
        product_id = int(input("▶ Enter the ID of the product to update: "))
        product_found = next((p for p in inventory_list if p['id'] == product_id), None)
        
        if product_found is None:
            print(f"⚠️ Product with ID {product_id} not found.")
            return

        print(f"\nFound: {product_found['name']} (Stock: {product_found['stock']}, Price: ${product_found['price']:.2f})")
        
        print("Which detail do you want to update?")
        print("  S: Stock")
        print("  P: Price")
        
        choice = input("Enter S or P: ").strip().upper()

        if choice == 'S':
            new_stock = get_validated_input("▶ Enter new Stock Quantity: ", int, min_value=0, allow_zero=True)
            product_found['stock'] = new_stock
            print(f"\n✅ SUCCESS: Stock for '{product_found['name']}' updated to {new_stock}.")
        
        elif choice == 'P':
            new_price = get_validated_input("▶ Enter new Unit Price: ", float, min_value=0, allow_zero=False)
            product_found['price'] = round(new_price, 2)
            print(f"\n✅ SUCCESS: Price for '{product_found['name']}' updated to ${new_price:.2f}.")
        
        else:
            print("⚠️ Invalid choice. Update cancelled.")
            
    except ValueError:
        print("❌ Invalid input. Please enter a valid number for ID.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# ----------------------------------------------------------------------
# 4. Delete Product Function (Delete)
# ----------------------------------------------------------------------

def delete_product():
    """Removes a product from the inventory based on its ID."""
    global inventory_list
    print("\n---- 4. Delete Product ----")
    list_inventory()
    
    try:
        product_id = int(input("▶ Enter the ID of the product to delete: "))
        
        # Filter out the product to be deleted
        initial_length = len(inventory_list)
        inventory_list = [p for p in inventory_list if p['id'] != product_id]
        
        if len(inventory_list) < initial_length:
            print(f"\n✅ SUCCESS: Product with ID {product_id} successfully deleted.")
        else:
            print(f"⚠️ Product with ID {product_id} not found.")

    except ValueError:
        print("❌ Invalid input. Please enter a valid number for the ID.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# ----------------------------------------------------------------------
# ⚙️ Main Application Loop
# ----------------------------------------------------------------------

def display_main_menu():
    """Displays the main interactive menu."""
    print("\n=======================================================")
    print("     🛒 ELECTRONICS INVENTORY MANAGEMENT SYSTEM (EIMS)    ")
    print("=======================================================")
    print("1. Add New Product (Create)")
    print("2. Display Inventory (Read)")
    print("3. Update Product Details (Update)")
    print("4. Delete Product (Delete)")
    print("5. Exit System")
    print("-------------------------------------------------------")

def main():
    """Main function to run the application."""
    while True:
        display_main_menu()
        choice = input("▶ Enter your choice (1-5): ").strip()
        
        try:
            if choice == '1':
                add_inventory()
            elif choice == '2':
                list_inventory()
            elif choice == '3':
                update_product()
            elif choice == '4':
                delete_product()
            elif choice == '5':
                print("\n👋 Exiting system. Goodbye!")
                break
            else:
                print("\n⚠️ Invalid choice. Please select an option from 1 to 5.")
                
        except Exception as e:
            # Catch any unexpected critical errors
            print(f"\n❌ A critical error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()