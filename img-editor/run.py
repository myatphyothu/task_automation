import os
import json
import argparse
from PIL import Image, ImageEnhance, ImageFilter


SETTINGS = 'settings.json'

def get_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-dir', '--dir', required=True, help='directory to photos and images')
    return parser.parse_args()


def load_settings():
    if not os.path.exists(SETTINGS):
        return None

    with open(SETTINGS, 'r') as f:
        return json.load(f)


def get_images(dir, img_file_types):
    files = []
    for f in os.listdir(dir):
        filename, extension = os.path.splitext(f)
        if extension.replace('.', '').lower() in img_file_types:
            files.append(f)
    return [f'{dir}/{f}' for f in files]

def main():
    args = get_cli_args()
    settings = load_settings()

    if settings is None:
        print('Error: unable to load settings.')
        exit()

    if args.dir:
        images = get_images(args.dir, settings['image-file-types'])
        print(images)


if __name__ == '__main__':
    main()


