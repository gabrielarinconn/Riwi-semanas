# main.py
import data_manager # Importa funciones de carga/guardado
import operations   # Importa funciones de lógica de negocio (inventario, ventas, reportes)
import sys

def main_menu():
    """Displays the main interactive menu."""
    
    # 1. Load data at startup
    data_manager.load_data() 
    
    while True:
        print("\n" + "#"*40)
        print("📦 E-Store Inventory & Sales System")
        print("#"*40)
        
        print("--- 1. Inventory Management ---")
        print("11. Register New Product")
        print("12. Consult/Display Inventory")
        print("13. Update Product Details")
        print("14. Delete Product")
        
        print("\n--- 2. Sales Operations ---")
        print("21. Register New Sale")
        print("22. Consult Sales History")
        
        print("\n--- 3. Reporting ---")
        print("30. Generate Dynamic Reports")
        
        print("\n0. Exit System")
        print("#"*40)
        
        choice = input("Enter your choice: ").strip()
        
        try:
            if choice == '11':
                operations.register_product()
            elif choice == '12':
                operations.display_inventory()
            elif choice == '13':
                operations.update_product()
            elif choice == '14':
                operations.delete_product()
            elif choice == '21':
                operations.register_sale()
            elif choice == '22':
                operations.display_sales_history()
            elif choice == '30':
                operations.generate_reports()
            elif choice == '0':
                # 2. Save data at shutdown
                data_manager.save_data()
                print("\n👋 Exiting the system. Thank you!")
                sys.exit(0) # Use sys.exit to ensure clean termination
            else:
                print("❌ Invalid option. Please enter a valid menu number.")
                
        except Exception as e:
            # Global exception handler
            print(f"\n🛑 An unexpected error occurred: {e}. Returning to main menu.")

if __name__ == "__main__":
    main_menu()