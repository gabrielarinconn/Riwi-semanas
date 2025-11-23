import functions


inventary_list = []

def add_inventary():
    print("----1. Add Product in Inventary----")
    name = input("▶ Type name's Product: ").strip().title()
    brand = input("▶ Type brand's Product: ").strip().title()
    category = input("▶ Type category's Product: ").strip().title()
    
    
    # Loop for validate numbers in price, stock and warranty

    while True:
        try:
            price = float(input("▶ Type price's Product: "))
            if price <= 0:
                print("❌ The number can positive")
                continue
            break
        except ValueError:
            print("❌ Error: Please, enter the correct number")

    while True:
        try:
            stock = int(input("▶ Type stock's Product: "))
            if stock < 0:
                print("❌ The number can positive")
            break
        except ValueError:
            print("❌ Error: Please, enter the correct number")
        
    while True:
        try:
            warranty = int(input("▶ Type warranty's Product: "))
            if warranty < 0:
                print("❌ The number can positive")
            break
        except ValueError:
            print("❌ Error: Please, enter the correct number")


    # Create library
    inventary ={
        "name": name,
        "brand": brand,
        "category" : category ,
        "price" : price , 
        "stock" : stock, 
        "warranty" :warranty
    }


add_inventary()
