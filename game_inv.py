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


              

inventory = {"gold" : 25, "armor" : 9, "helmet": 4, "sword" : 5}
added_items = ('gold',"helmet","shoes")
add_to_inventory(inventory,added_items)
display_inventory(inventory)