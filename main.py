import customtkinter
from PIL import Image

app_window_name = "World Weaver"
app_window_resolution = "1366x768"
logo_path = "logo.png"  # Replace with the path to your logo image


class WorldWeaverWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title(app_window_name)
        self.geometry(app_window_resolution)

        # Load the logo image
        self.logo_image = Image.open(logo_path)
        self.logo_photo_image = customtkinter.CTkImage(self.logo_image, size=(500, 500))

        # Configure the grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        # Create a label for the logo
        self.logo_label = customtkinter.CTkLabel(self, text="", image=self.logo_photo_image)
        self.logo_label.grid(row=0, column=1, pady=20)

        # Create new world button
        self.new_world_button = customtkinter.CTkButton(self, text="Create new world!",
                                                        command=self.create_new_world_button)
        self.new_world_button.grid(row=1, column=1, padx=20, pady=5, sticky="nsew")

        # Open existing world button
        self.open_world_button = customtkinter.CTkButton(self, text="Open existing world!",
                                                         command=self.open_existing_world_button)
        self.open_world_button.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

    def create_new_world_button(self):
        print("Create new world!")

    def open_existing_world_button(self):
        print("Open existing world!")


# Create and run the application window
app = WorldWeaverWindow()
app.mainloop()
