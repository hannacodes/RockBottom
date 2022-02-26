import  pygame, sys
from os import walk

def import_folder(path):
    surface_list = []
    for img_file in walk(path):
        for image in img_file:
            full_path = path + '/' + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
    return surface_list