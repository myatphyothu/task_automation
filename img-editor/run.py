import os
import json
import argparse
from image_editor import ImageEditor


SETTINGS = 'settings.json'

def get_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-input', '--input', required=True, help='directory to photos and images')
    parser.add_argument('-output', '--output', required=True, help='directory where edited images will be saved')
    return parser.parse_args()


def get_user_input():
    input = input('Enter path to photos or images:')
    output = input('Enter path where edited images will be saved:')
    return input, output


def load_settings():
    if not os.path.exists(SETTINGS):
        return None

    with open(SETTINGS, 'r') as f:
        return json.load(f)


def main():
    args = get_cli_args()
    settings = load_settings()

    if settings is None:
        print('Error: unable to load settings.')
        exit()

    if args.input and args.output:
        editor = ImageEditor(args.input, args.output)
        editor.accept_file_types = settings['image-file-types']
        editor.edit_options = settings['edit-options']

        editor.apply_edits()
        editor.save()

    else:
        print('error: args.input and args.output have to be specified.')
        print(f'args.input: {args.input if args.input else "empty"} ')
        print(f'args.output: {args.output if args.output else "empty"}')


if __name__ == '__main__':
    main()


