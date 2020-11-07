from pathlib import Path
import csv

def display_inventory(inventory):
    for key, value in inventory.items():
        print(key+":",value)

def add_to_inventory(inventory, added_items):
    for elements in added_items:
        for key in inventory:
            if key == elements:
                inventory[key] += 1
    for elements in added_items:
        if elements not in inventory:
            inventory[elements] = 1

def remove_from_inventory(inventory, removed_items):
    check_if_null = []
    for elements in removed_items:
        for key in inventory:
            if key == elements:
                inventory[key] -= 1
    for key, value in inventory.items():
        if value <= 0:
            check_if_null.append(key)
    for elements in check_if_null:
        inventory.pop(elements)

def print_table(inventory, order=""):
    #do porawy inteligentne formatowanie zależne od długości najdłuższego key w inventory

    if order == "desc":
        sorted_inventory = {key: value for key,value in sorted(inventory.items(), key=lambda x: x[1], reverse=True)}
    elif order == "asc":
        sorted_inventory = {key: value for key,value in sorted(inventory.items(), key=lambda x: x[1], reverse=False)}
    else :
        sorted_inventory = inventory    
    print(20*"-")
    print("{:>8} | {:<5}".format("item","count"))
    print(20*"-")
    for key,value in sorted_inventory.items():
        print("{:>8} | {:<5}".format(key,value))
    print(20*"-")

def import_inventory(inventory, filename=""):
    import_items = []
    if filename == "":
        filename = "import_inventory.csv"
    path = Path(__file__).parent
    with open (f'{path}//{filename}') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            for element in row:
                import_items.append(element)
    add_to_inventory(inventory,import_items)
                

inventory = {"gold" : 25, "armor" : 9, "helmet": 4, "sword" : 5, "wood" : 3}
filename = ""
added_items = ['gold',"helmet","shoes","gold"]
removed_items = ["gold", "shoes", "shoes", "helmet"]
add_to_inventory(inventory,added_items)
remove_from_inventory(inventory, removed_items)
order = "asc"
import_inventory(inventory)
print_table(inventory)
