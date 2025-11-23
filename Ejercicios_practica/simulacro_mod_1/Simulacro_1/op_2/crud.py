


inventary_list = []

p1= {
'Name': 'Laptop ProBook X',
'Brand': 'TechCorp',
'Category': 'Computers',
'Price': 1250.00,
'Stock': 15,
'Warranty': 24
}
p2= {
'Name': 'Headphones',
'Brand': 'AudioMax',
'Category': 'Audio',
'Price': 199.99,
'Stock': 45,
'Warranty': 12
}

p3= {
'Name': '4K Smart TV 55"',
'Brand': 'ViewStar',
'Category': 'Televisions',
'Price': 789.50,
'Stock': 20,
'Warranty': 36
}
p4= {
'Name': 'Gaming Mouse',
'Brand': 'GameOn',
'Category': 'Peripherals',
'Price': 45.99,
'Stock': 110,
'Warranty': 6
}
p5= {
'Name': 'Power Bank',
'Brand': 'ChargeQuick',
'Category': 'Accessories',
'Price': 35.00,
'Stock': 75,
'Warranty': 3
}
def check_number_positive(text):
    while True:
        try:
            value = float(input(text))
            if value <= 0:
                print("❌ The number needs to be positive")
                continue
            break
        except ValueError:
            print("❌ Error: Please, enter the correct number")
    return value

def check_number_in_list(text,number_):
    while True:
        try:
            value = int(input(text))
            if value < 0 or value > number_ -1:
                print("❌ The number needs to be in list")
                continue
            break
        except ValueError:
            print("❌ Error: Please, enter the correct number")
    return value

def add_inventary():
    print("----1. Add Product in Inventary----")
    name = input("▶ Type name's Product: ").strip().title()
    brand = input("▶ Type brand's Product: ").strip().title()
    category = input("▶ Type category's Product: ").strip().title()
    
    # Create library
    inventary ={
        "Name": name,
        "Brand": brand,
        "Category" : category ,
        "Price" : check_number_positive("▶ Type price's Product: ") , 
        "Stock" : check_number_positive("▶ Type stock's Product: "), 
        "Warranty" : check_number_positive("▶ Type warranty's Product: ")
    }
    return inventary


title_product = ["Name","Brand","Category","Price" ,"Stock","Warranty"]

def title_row(list_):
    text = str(f"Index{"":<10}")
    for i in list_: 
        text += str(f"{i:<20}")
    print(text)




inventary_list.append(p1)
inventary_list.append(p2)
inventary_list.append(p3)
inventary_list.append(p4)
inventary_list.append(p5)




def dict_row(dict_, list_):
    text = str(f"{0:<10}")
    for j,x in enumerate (dict_):
        for n in list_:
            text +=  str(f"{x[n]:<20}")
        print (text)
        text = str(f"{j+1:<10}")

title_row(title_product)
dict_row(inventary_list,title_product)

def eraser(list_):
    erase_ = check_number_in_list("Type the index you want to delete: ",len(list_))
    inventary_list.pop(erase_)

eraser(inventary_list) 
 
title_row(title_product)
dict_row(inventary_list,title_product)

#inventary_list.append(add_inventary())



