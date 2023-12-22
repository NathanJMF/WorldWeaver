import noise
import numpy as np
from PIL import Image


def generate_overworld(scale, octaves, persistence, lacunarity):
    width, height = 1024, 1024
    noise_map = generate_noise_map(width, height, scale, octaves, persistence, lacunarity)
    normalized_map = normalize_map(noise_map)
    return create_image(normalized_map)


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


def save_image(image, file_name):
    file_name = f"./saves/{file_name}.png"
    image.save(file_name)
