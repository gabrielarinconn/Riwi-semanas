# list of all elements of inventary

p1  = ["Camera",   "Sony",     "Device",         500,  10, 12]
p2  = ["Keyboard", "Keychron", "Device",         20,   50, 6]
p3  = ["Mouse",    "Logitech", "Device",         10,   70, 3 ]
p4  = ["ThinkBook","Lenovo",   "Computer",       1500, 15, 24]
p5  = ["Roku TV",  "Roku",     "Entertainment",  30,   80, 3] 


# list to do the matrix
inventary =[p1,p2,p3,p4,p5]

for i,x in enumerate(inventary):
    print(f'{i},{x}')
    for j,y in enumerate(inventary[i]):
        print(f"{j},{y}")
