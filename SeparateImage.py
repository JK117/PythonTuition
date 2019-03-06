from PIL import Image


def crop_save(img, img_num, img_prefix):
    x = (img_num - 1) * 512
    box = (x, 0, x+3840, 2048)
    cropped_img = img.crop(box)
    cropped_img.save(img_prefix + str(img_num) + '.jpg')


if __name__ == "__main__":
    input_img_path = "ow.jpg"
    output_img_prefix = input_img_path.split('.')[0] + '_'
    input_img = Image.open(input_img_path)

    for i in range(1, 17):
        crop_save(input_img, i, output_img_prefix)
