from map_tooling import _generator_helper


def generate_overworld():
    width, height = 1024, 1024
    scale = 100.0  # Affects the "zoom" of the noise pattern
    octaves = 6  # Affects the detail of the map
    persistence = 0.5
    lacunarity = 2.0

    noise_map = _generator_helper.generate_noise_map(width, height, scale, octaves, persistence, lacunarity)
    normalized_map = _generator_helper.normalize_map(noise_map)
    _generator_helper.create_image(normalized_map, './saves/overworld_map.png')

