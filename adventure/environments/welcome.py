import tkinter as tk
from adventure.game import GameLogic

game = GameLogic("knife")

class WelcomeApp:
    def __init__(self, root, health, stamina, inventory):
        self.root = root
        self.create_widgets(health, stamina, inventory)

    def create_widgets(self, health, stamina, inventory):
        # Configure the root window background color
        self.root.configure(bg="black")

        # Set the highlight color and thickness for the root window
        self.root.configure(highlightbackground="white", highlightthickness=5)

        # Create a frame for the welcome label with a white border
        welcome_frame = tk.Frame(self.root, bg="black", bd=5, relief=tk.SOLID)
        welcome_frame.pack(pady=20)

        # Create the welcome label
        welcome_label = tk.Label(welcome_frame, text="During your travels in some environments, some situation happens!!", bg="black", fg="white")
        welcome_label.pack(pady=10, padx=10)

        # Create a frame for the white line
        line_frame = tk.Frame(self.root, bg="white", height=2)
        line_frame.pack(fill=tk.X, padx=10)

        # Create a frame for the decisions with a white border
        decisions_frame = tk.Frame(self.root, bg="black", bd=5, relief=tk.SOLID)
        decisions_frame.pack(pady=10)

        # Create three labels for the decisions
        decision1_label = tk.Label(decisions_frame, text="Decision 1", bg="black", fg="white")
        decision1_label.pack(side=tk.LEFT, padx=10)
        decision2_label = tk.Label(decisions_frame, text="Decision 2", bg="black", fg="white")
        decision2_label.pack(side=tk.LEFT, padx=10)
        decision3_label = tk.Label(decisions_frame, text="Decision 3", bg="black", fg="white")
        decision3_label.pack(side=tk.LEFT, padx=10)

        # Create a frame for health and stamina
        health_stamina_frame = tk.Frame(self.root, bg="black")
        health_stamina_frame.pack(anchor=tk.W, padx=10, pady=10)  # Align to the far left of the window

        # Create a frame for HP
        hp_frame = tk.Frame(health_stamina_frame, bg="black")
        hp_frame.pack(side=tk.LEFT)

        # Create the HP label
        hp_label = tk.Label(hp_frame, text="HP:", bg="black", fg="white")
        hp_label.pack(side=tk.LEFT)

        # Create labels for health using emojis
        health_emojis = "❤️" * health  # 10 red hearts emojis
        health_label = tk.Label(hp_frame, text=health_emojis, bg="black", fg="white")
        health_label.pack(side=tk.LEFT)

        # Create a frame for SP
        sp_frame = tk.Frame(health_stamina_frame, bg="black")
        sp_frame.pack(side=tk.LEFT, padx=(10, 0))

        # Create the SP label
        sp_label = tk.Label(sp_frame, text="SP:", bg="black", fg="white")
        sp_label.pack(side=tk.LEFT)

        # Create a frame for the SP meat emojis
        sp_meat_frame = tk.Frame(sp_frame, bg="black")
        sp_meat_frame.pack(side=tk.LEFT)

        # Create labels for meat using emojis
        meat_emojis = "🍖" * stamina  # 10 meat emojis
        meat_label = tk.Label(sp_meat_frame, text=meat_emojis, bg="black", fg="white")
        meat_label.pack(side=tk.LEFT)

        # Create a frame for items
        items_frame = tk.Frame(health_stamina_frame, bg="black")
        items_frame.pack(side=tk.LEFT, padx=(10, 0))

        # Create the items label
        items_label = tk.Label(items_frame, text="ITEMS:", bg="black", fg="white")
        items_label.pack(side=tk.LEFT)

        # Iterate over the inventory items and create labels dynamically
        for item in inventory:
            item_frame = tk.Frame(items_frame, bg="black", highlightbackground="white", highlightthickness=1,
                                  relief=tk.FLAT)
            item_frame.pack(side=tk.LEFT, padx=5)

            # Create the item label with emojis based on the item name
            if item == "knife":
                item_label = tk.Label(item_frame, text="🔪", bg="black", fg="white")
            elif item == "med spray":
                item_label = tk.Label(item_frame, text="💊", bg="black", fg="white")
            elif item == "ration":
                item_label = tk.Label(item_frame, text="🍗", bg="black", fg="white")
            elif item == "grappling_hook":
                item_label = tk.Label(item_frame, text="🪝", bg="black", fg="white")
            elif item == "rope":
                item_label = tk.Label(item_frame, text="🧵", bg="black", fg="white")
            else:
                item_label = tk.Label(item_frame, text=item, bg="black", fg="white")  # Use item name as a fallback
            item_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomeApp(root, game.health, game.stamina, game.inventory)
    root.mainloop()
