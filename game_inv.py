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

              

inventory = {"gold" : 25, "armor" : 9, "helmet": 4, "sword" : 5}
added_items = ['gold',"helmet","shoes","gold"]
removed_items = ["gold", "shoes", "shoes", "helmet"]
add_to_inventory(inventory,added_items)
remove_from_inventory(inventory, removed_items)
display_inventory(inventory)