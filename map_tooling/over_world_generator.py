import noise
import numpy as np
from PIL import Image
from map_tooling import _helpers


def generate_noise_map(width, height, scale, octaves, persistence, lacunarity):
    world_map = np.zeros((height, width))
    for y in range(height):
        for x in range(width):
            world_map[y][x] = noise.pnoise2(x / scale,
                                            y / scale,
                                            octaves=octaves,
                                            persistence=persistence,
                                            lacunarity=lacunarity)
    return world_map


def normalize_map(noise_map):
    max_val = np.max(noise_map)
    min_val = np.min(noise_map)
    return (noise_map - min_val) / (max_val - min_val) * 255


def create_image(noise_map):
    image = Image.fromarray(noise_map)
    image = image.convert('L')  # Convert to grayscale
    return image


def save_height_map(image, save_name):
    image_type = "height_map"
    _helpers.create_save(image, save_name, image_type)


def save_coloured_map(image, save_name):
    image_type = "coloured_map"
    _helpers.create_save(image, save_name, image_type)


def create_coloured_image(noise_map):
    height, width = noise_map.shape
    coloured_image = Image.new("RGB", (width, height))
    pixels = coloured_image.load()

    # Define height range thresholds
    dark_water_upper = 70
    water_upper = 90
    sand_upper = 120
    dirt_upper = 140
    forest_upper = 200
    stone_upper = 220
    # Mountain/Stone is everything above forest_upper
    for y in range(height):
        for x in range(width):
            height_value = noise_map[y, x]
            if height_value <= dark_water_upper:  # Dark Water
                colour = (0, 0, 180)
            elif height_value <= water_upper:  # Water
                colour = (0, 0, 255)
            elif height_value <= sand_upper:  # Sand
                colour = (194, 178, 128)
            elif height_value <= dirt_upper:  # Dirt
                colour = (139, 69, 19)
            elif height_value <= forest_upper:  # Forest
                colour = (34, 139, 34)
            elif height_value <= stone_upper:  # Stone
                colour = (169, 169, 169)
            else:  # Snow
                colour = (255, 255, 255)
            pixels[x, y] = colour
    return coloured_image

