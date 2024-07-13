from PIL import Image, ImageEnhance, ImageFilter


class ImageOperations(object):

    @staticmethod
    def sharpen(original_img, **xargs):
        return original_img.filter(ImageFilter.SHARPEN)

    @staticmethod
    def convert(original_img, **xargs):
        return original_img.convert(xargs['param'])

    @staticmethod
    def rotate(original_img, **xargs):
        return original_img.rotate(float(xargs['param']))

    @staticmethod
    def contrast(original_img, **xargs):
        factor = float(xargs['param'])
        enhancer = ImageEnhance.Contrast(original_img)
        return enhancer.enhance(factor)
