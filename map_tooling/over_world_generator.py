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
