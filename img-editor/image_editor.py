import os
from PIL import Image, ImageEnhance, ImageFilter


DEFAULT_IMAGE_FILE_TYPES = ['jpg', 'jpeg', 'png', 'gif']
DEFAULT_EDIT_OPTIONS = ['sharpen']


class ImageEditor(object):
    def __init__(
            self, path, output_path,
            accept_file_types=DEFAULT_IMAGE_FILE_TYPES, edit_options=DEFAULT_EDIT_OPTIONS
    ):
        self._path = path
        self._output_path = output_path
        self._accept_file_types = accept_file_types
        self._edit_options = edit_options

        self._edit_img_operations = {
            'sharpen': self._sharpen
        }

        self.edited_images = {}

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, new_path):
        self._path = new_path

    @property
    def output_path(self):
        return self._output_path

    @output_path.setter
    def output_path(self, new_output_path):
        self._output_path = new_output_path

    @property
    def accept_file_types(self):
        return self._accept_file_types

    @accept_file_types.setter
    def accept_file_types(self, new_accept_file_types):
        self._accept_file_types = new_accept_file_types

    @property
    def edit_options(self):
        return self._edit_options

    @edit_options.setter
    def edit_options(self, new_edit_options):
        self._edit_options = new_edit_options

    def _get_image_files(self):
        files = []
        for file in os.listdir(self.path):
            filename, extension = os.path.splitext(file)
            if extension.replace('.', '').lower() in self._accept_file_types:
                files.append(file)
        return [f'{self._path}/{file}' for file in files]

    def _sharpen(self, original_img):
        return original_img.filter(ImageFilter.SHARPEN)

    def _edit_an_image(self, original_img):
        final_img = original_img

        for operation, apply_edit in self._edit_img_operations.items():
            if operation in self._edit_options:
                final_img = apply_edit(final_img)

        return final_img

    def _edit_images(self, image_files):
        edited_images = {}
        for img_file in image_files:
            img = Image.open(img_file)
            edited_img = self._edit_an_image(img)
            edited_images[img_file] = edited_img
        return edited_images

    def _save_images(self):
        os.makedirs(self._output_path, exist_ok=True)
        for filename, img in self.edited_images.items():
            base_filename = os.path.basename(filename)
            name, ext = os.path.splitext(base_filename)
            img.save(f'{self.output_path}/{name}_edited{ext}')

    def apply_edits(self):
        image_files = self._get_image_files()
        self.edited_images = self._edit_images(image_files)

    def save(self):
        if len(self.edited_images) == 0:
            print('Nothing to save -> no pictures were edited.')
        else:
            self._save_images()





