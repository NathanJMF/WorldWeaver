import customtkinter
from PIL import Image
from map_tooling import over_world_generator

app_window_name = "World Weaver"
app_window_width = 1920
app_window_height = 1080
app_window_resolution = f"{app_window_width}x{app_window_height}"
logo_path = "assets/logo.png"
icon_path = "assets/icon.ico"


class WorldWeaverWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.right_panel_width = None
        self.coloured_map_image = None
        self.height_map_image = None
        self.persistence_slider = None
        self.octaves_slider = None
        self.scale_slider = None
        self.lacunarity_slider = None
        self.map_preview_label = None
        self.map_name_entry = None
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

    # -----------------------------------------------------------------------------------------------------------------
    # HOME PAGE
    # -----------------------------------------------------------------------------------------------------------------
    def setup_home_page(self):
        create_world_button_text = "Create new world"
        open_world_button_text = "Open existing world"
        # Load the logo image
        self.logo_image = Image.open(logo_path)
        self.logo_photo_image = customtkinter.CTkImage(self.logo_image, size=(500, 500))
        # Create a label for the logo in the home page frame
        self.logo_label = customtkinter.CTkLabel(self.home_page, text="", image=self.logo_photo_image)
        self.logo_label.pack(pady=20)  # Use pack instead of grid
        # Create new world button in the home page frame
        customtkinter.CTkButton(self.home_page, text=create_world_button_text,
                                command=self.show_new_world_page).pack(pady=10)
        # Open existing world button in the home page frame
        customtkinter.CTkButton(self.home_page, text=open_world_button_text,
                                command=self.show_existing_world_page).pack(pady=10)

    def show_home_page(self):
        self.new_world_page.pack_forget()
        self.existing_world_page.pack_forget()
        self.home_page.pack(fill="both", expand=True)

    # -----------------------------------------------------------------------------------------------------------------
    # NEW WORLD PAGE
    # -----------------------------------------------------------------------------------------------------------------
    def setup_new_world_page(self):
        # Split the frame into 2 panels
        left_panel_screen_coverage = 0.2
        left_panel_input_coverage = 0.95

        left_panel_width = int(left_panel_screen_coverage * app_window_width)
        self.right_panel_width = int(app_window_width - left_panel_width)
        left_panel_input_width = int(left_panel_width * left_panel_input_coverage)
        back_button_padding = left_panel_width - left_panel_input_width

        left_panel = customtkinter.CTkFrame(self.new_world_page, width=left_panel_width,
                                            border_color="gray",
                                            border_width=2)
        left_panel.pack_propagate(False)
        right_panel = customtkinter.CTkFrame(self.new_world_page,
                                             border_color="gray",
                                             border_width=2)

        # Back Button
        back_button = customtkinter.CTkButton(left_panel, text="Back", command=self.show_home_page,
                                              width=left_panel_input_width)
        back_button.pack(pady=(back_button_padding, 5))
        # Map Name Field
        self.map_name_entry = customtkinter.CTkEntry(left_panel, placeholder_text="Enter map name",
                                                     width=left_panel_input_width)
        self.map_name_entry.pack(pady=5)
        # Sliders for noise map variables
        # Scale Slider
        customtkinter.CTkLabel(left_panel, text="World Size", anchor="w").pack(pady=(5, 0),
                                                                               padx=back_button_padding,
                                                                               fill="x")
        self.scale_slider = customtkinter.CTkSlider(left_panel, from_=10, to=500, width=left_panel_input_width)
        self.scale_slider.set(100)  # Default value
        self.scale_slider.pack(pady=(0, 5))

        # Octaves Slider
        customtkinter.CTkLabel(left_panel, text="Terrain Complexity", anchor="w").pack(pady=(5, 0),
                                                                                       padx=back_button_padding,
                                                                                       fill="x")
        self.octaves_slider = customtkinter.CTkSlider(left_panel, from_=1, to=10, width=left_panel_input_width)
        self.octaves_slider.set(6)  # Default value
        self.octaves_slider.pack(pady=5)

        # Persistence Slider
        customtkinter.CTkLabel(left_panel, text="Landscape Variation", anchor="w").pack(pady=(5, 0),
                                                                                        padx=back_button_padding,
                                                                                        fill="x")
        self.persistence_slider = customtkinter.CTkSlider(left_panel, from_=0, to=1, width=left_panel_input_width)
        self.persistence_slider.set(0.5)  # Default value
        self.persistence_slider.pack(pady=5)

        # Lacunarity Slider
        customtkinter.CTkLabel(left_panel, text="Geographical Roughness", anchor="w").pack(pady=(5, 0),
                                                                                           padx=back_button_padding,
                                                                                           fill="x")
        self.lacunarity_slider = customtkinter.CTkSlider(left_panel, from_=1, to=4, width=left_panel_input_width)
        self.lacunarity_slider.set(2.0)  # Default value
        self.lacunarity_slider.pack(pady=5)

        # Button to preview the noise map
        customtkinter.CTkButton(left_panel, text="Preview Map", command=self.preview_map,
                                width=left_panel_input_width).pack(pady=5)

        # Button to save the noise map
        customtkinter.CTkButton(left_panel, text="Save Map", command=self.save_map,
                                width=left_panel_input_width).pack(pady=5)

        # Placeholder for map preview in the right panel
        self.map_preview_label = customtkinter.CTkLabel(right_panel, text="Map Preview Here")
        self.map_preview_label.pack(expand=True)
        left_panel.pack(side='left', fill='y')
        right_panel.pack(side='right', fill='both', expand=True)

    def preview_map(self):
        scale_value = int(self.scale_slider.get())
        octaves_value = int(self.octaves_slider.get())
        persistence_value = self.persistence_slider.get()
        lacunarity_value = self.lacunarity_slider.get()
        # Generate the over_world map
        noise_map = over_world_generator.generate_noise_map(2048, 2048, scale_value, octaves_value,
                                                            persistence_value, lacunarity_value)
        normalized_map = over_world_generator.normalize_map(noise_map)
        self.height_map_image = over_world_generator.create_image(normalized_map)
        self.coloured_map_image = over_world_generator.create_coloured_image(normalized_map)

        # Calculate new height to maintain aspect ratio
        original_width, original_height = self.coloured_map_image.size
        display_width = self.right_panel_width
        aspect_ratio = original_height / original_width
        display_height = int(display_width * aspect_ratio)

        # Resize the image to fit in the display area while maintaining aspect ratio
        resized_height_map_image = self.height_map_image.resize((display_width, display_height),
                                                                Image.Resampling.LANCZOS)
        resized_coloured_map_image = self.coloured_map_image.resize((display_width, display_height),
                                                                    Image.Resampling.LANCZOS)

        # Convert the PIL image to a format that can be used in Tkinter
        tk_image = customtkinter.CTkImage(resized_coloured_map_image, size=(display_width, display_height))
        # Update the label to show the map
        self.map_preview_label.configure(text="")
        self.map_preview_label.configure(image=tk_image)
        self.map_preview_label.image = tk_image

    def save_map(self):
        file_name_to_use = self.map_name_entry.get()
        over_world_generator.save_height_map(self.height_map_image, file_name_to_use)
        over_world_generator.save_coloured_map(self.coloured_map_image, file_name_to_use)

    def show_new_world_page(self):
        self.home_page.pack_forget()
        self.new_world_page.pack(fill="both", expand=True)

    # -----------------------------------------------------------------------------------------------------------------
    # EXISTING WORLD PAGE
    # -----------------------------------------------------------------------------------------------------------------
    def setup_existing_world_page(self):
        customtkinter.CTkButton(self.existing_world_page, text="Back",
                                command=self.show_home_page).pack(pady=10)

    def show_existing_world_page(self):
        self.home_page.pack_forget()
        self.existing_world_page.pack(fill="both", expand=True)
    # -----------------------------------------------------------------------------------------------------------------
