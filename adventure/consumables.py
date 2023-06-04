from rich.prompt import Prompt

def use_item(item, resource):

    maximum = 10

    if item == "med spray":
        if resource == maximum:
            print(f"Cannot use {item}, already at max HP!")
            return 0
        else:
            new_health = resource + 5
            if new_health > maximum:
                new_health = maximum
            print(f"You recovered {new_health - resource} HP!")
            return new_health
    elif item == "ration":
        if resource == maximum:
            print(f"Cannot use {item}, already at max SP!")
            return 0
        else:
            new_stamina = resource + 5
            if new_stamina > maximum:
                new_stamina = maximum
            print(f"You recovered {new_stamina - resource} SP!")
            return new_stamina


def item_selection(inv, health, stamina):
    while True:
        print("Items List:")
        for item in inv:
            print(f"{inv.index(item) + 1}. {item}")
        item = Prompt.ask("Please select an item you would like to use", default="return", show_default=False)
        if item == "med spray" and item in inv:
            inv.remove(item)
            hp = use_item(item, health)
            health = hp
            return health, stamina
        elif item == "ration" and item in inv:
            inv.remove(item)
            sp = use_item(item, stamina)
            stamina = sp
            return health, stamina
        elif item == "return":
            break
        else:
            print(f"You do not have a {item} in your inventory!")

    return health, stamina
