"""
File: stanCodoshop.py
Name: Emilie Chen
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


# Milestone 1
def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    red_avg = red
    green_avg = green
    blue_avg = blue
    dist = ((red_avg - pixel.red) ** 2 + (green_avg - pixel.green) ** 2 + (blue_avg - pixel.blue) ** 2) ** (1 / 2)
    return dist
    # pixel list

def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # list of pixels
    sum_red = 0
    sum_green = 0
    sum_blue = 0
    for pixel in range(len(pixels)):
        sum_red += pixels[pixel].red
        sum_green += pixels[pixel].green
        sum_blue += pixels[pixel].blue
    rgb = [sum_red//len(pixels), sum_green//len(pixels), sum_blue//len(pixels)]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    avg_rgb = get_average(pixels)
    best_pixel = 390  # 比較標準
    best = [0, 0, 0]  # 要return的, # 與均值距離最近的pixel
    # 不同張圖片中的rgb
    for pixel in pixels:
        #  get_pixel_dist(pixel, red, green, blue)
        each_dist = get_pixel_dist(pixel, avg_rgb[0], avg_rgb[1], avg_rgb[2])
        # 如果該張圖片color distance的距離 比前一張距離還要短時
        if best_pixel > each_dist:
            best = pixel  # the pixel that has the smallest "color distance"
            best_pixel = each_dist
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    # Milestone 1 測試 v
    # green_im = SimpleImage.blank(20, 20, 'green')
    # green_pixel = green_im.get_pixel(0, 0)
    # print(get_pixel_dist(green_pixel, 5, 255, 10))

    # # Milestone 2 測試 v
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))

    # Milestone 3 測試 v
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # green_pixel = SimpleImage.blank(20,20,'green').get_pixel(0,0)
    # blue_pixel = SimpleImage.blank(20,20,'blue').get_pixel(0,0)
    # best1 = get_best_pixel([red_pixel, green_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)

    # Milestone 4 刪除紅框code v
    for x in range(result.width):
        for y in range(result.height):
            pixel = []
            pixels = []  # AttributeError: 'Pixel' object has no attribute 'append'
            for i in images:
                pixel = i.get_pixel(x, y)
                pixels.append(pixel)
            result.set_pixel(x, y, get_best_pixel(pixels))
    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()

