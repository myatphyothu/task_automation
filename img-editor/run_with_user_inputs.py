import os
import json
import argparse
from image_editor import ImageEditor
from jproperties import Properties


SETTINGS = 'settings.json'
DOCKER_PROPERTIES = 'docker.properties'


def line_break():
    print('_' * 100)


def load_docker_settings():
    config = Properties()
    with open(DOCKER_PROPERTIES, 'rb') as properties_file:
        config.load(properties_file)
    return config


def load_settings():
    if not os.path.exists(SETTINGS):
        print('error: Settings file missing...')
        exit()

    with open(SETTINGS, 'r') as f:
        settings = json.load(f)
        return settings

def input_images_and_edited_paths():
    input_path = input('Enter path to photos or images: ')
    output_path = input('Enter path where edited images will be saved: ')
    return input_path, output_path


def input_edit_options(settings):
    available_edit_options = settings['available-edit-options']
    print(f'Available edit options: {",".join(available_edit_options)}')

    edit_options_input = input('Enter edit options(separate with commas for more than one): ')
    return edit_options_input


def input_edit_details(edit_type):
    while True:
        value = input(f'Enter {edit_type} value: ')
        try:
            float(value)
            return value
        except ValueError:
            print(f'error: {edit_type} value must be a number.')


def main():
    settings = load_settings()
    docker_properties = load_docker_settings()

    input_path, output_path = input_images_and_edited_paths()
    input_path = f'{docker_properties.get("docker_mnt_input_path").data}/{input_path}'
    output_path = f'{docker_properties.get("docker_mnt_output_path").data}/{output_path}'

    line_break()
    edit_options = input_edit_options(settings)
    full_edit_options = []

    for edit_type in edit_options.split(','):
        edit_type = edit_type.strip().lower()
        if edit_type == 'sharpen':
            full_edit_options.append(edit_type)
        elif edit_type in ['rotate', 'contrast']:
            value = input_edit_details(edit_type)
            full_edit_options.append(f'{edit_type},{value}')
        else:
            print(f'error: {edit_type} is neither valid nor implemented.')

    # print(f'edit_options: {full_edit_options}')
    line_break()

    editor = ImageEditor(input_path, output_path)
    editor.accept_file_types = settings['image-file-types']
    editor.edit_options = full_edit_options
    editor.apply_edits()
    editor.save()


if __name__ == '__main__':
    main()
