def use_item(item, resource):

    maximum = 10

    if item == "med spray":
        if resource == maximum:
            print(f"Cannot use {item}, already at max HP!")
        else:
            new_health = resource + 5
            if new_health > maximum:
                new_health = maximum
            print(f"You recovered {new_health - resource} HP!")
            return new_health
    elif item == "ration":
        if resource == maximum:
            print(f"Cannot use {item}, already at max SP!")
        else:
            new_stamina = resource + 5
            if new_stamina > maximum:
                new_stamina = maximum
            print(f"You recovered {new_stamina - resource} SP!")
            return new_stamina
