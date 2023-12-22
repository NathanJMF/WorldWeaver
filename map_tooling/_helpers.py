import os.path


def delete_save(save_name):
    pass


def create_save(image, save_name, image_type):
    current_save_location = f"./saves/{save_name}"
    # Check if save directory exists, create directory if not
    if not check_directory_exist(current_save_location):
        os.mkdir(current_save_location)
    # Save the image
    save_name = f"./saves/{save_name}/{image_type}.png"
    image.save(save_name)


def check_directory_exist(directory):
    return os.path.exists(directory)
