import customtkinter
from PIL import Image

app_window_name = "World Weaver"
app_window_resolution = "1366x768"
logo_path = "logo.png"
icon_path = "icon.ico"


class WorldWeaverWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.logo_label = None
        self.logo_photo_image = None
        self.logo_image = None
        self.title(app_window_name)
        self.geometry(app_window_resolution)
        self.iconbitmap(icon_path)
        # Initialise main frame that will hold the other frames
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)
        # Home Page
        self.home_page = customtkinter.CTkFrame(self.main_frame)
        self.setup_home_page()
        # New World Page
        self.new_world_page = customtkinter.CTkFrame(self.main_frame)
        self.setup_new_world_page()
        # Existing World Page
        self.existing_world_page = customtkinter.CTkFrame(self.main_frame)
        self.setup_existing_world_page()
        # Initially display the home page
        self.home_page.pack(fill="both", expand=True)

    def setup_home_page(self):
        # Load the logo image
        self.logo_image = Image.open(logo_path)
        self.logo_photo_image = customtkinter.CTkImage(self.logo_image, size=(500, 500))
        # Create a label for the logo in the home page frame
        self.logo_label = customtkinter.CTkLabel(self.home_page, text="", image=self.logo_photo_image)
        self.logo_label.pack(pady=20)  # Use pack instead of grid
        # Create new world button in the home page frame
        customtkinter.CTkButton(self.home_page, text="Create new world!",
                                command=self.show_new_world_page).pack(pady=10)
        # Open existing world button in the home page frame
        customtkinter.CTkButton(self.home_page, text="Open existing world!",
                                command=self.show_existing_world_page).pack(pady=10)

    def setup_new_world_page(self):
        customtkinter.CTkButton(self.new_world_page, text="Back",
                                command=self.show_home_page).pack(pady=10)

    def setup_existing_world_page(self):
        customtkinter.CTkButton(self.existing_world_page, text="Back",
                                command=self.show_home_page).pack(pady=10)

    def show_home_page(self):
        self.new_world_page.pack_forget()
        self.existing_world_page.pack_forget()
        self.home_page.pack(fill="both", expand=True)

    def show_new_world_page(self):
        self.home_page.pack_forget()
        self.new_world_page.pack(fill="both", expand=True)

    def show_existing_world_page(self):
        self.home_page.pack_forget()
        self.existing_world_page.pack(fill="both", expand=True)


# Create and run the application window
app = WorldWeaverWindow()
app.mainloop()
