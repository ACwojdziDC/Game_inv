def display_inventory(inventory):

    for key, value in inventory.items():
        print(key+":",value)








inventory = {"gold" : 25, "armor" : "silver", "helmet": "wood", "sword" : "strengthened"}
display_inventory(inventory)