import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

def rotate_image(image, angle):
    print("Inside rotate_image")
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

if __name__ == "__main__":
    BASE_PATH = os.path.join(os.getcwd(), "input")
    OUTPUT_PATH = os.path.join(os.getcwd(), "output_rotation")

    image_name = input("Enter name of image (with extension): ")
    angle = int(input("Enter the angle (in degrees): "))

    orig_image = cv2.imread(os.path.join(BASE_PATH, image_name))
    result = rotate_image(orig_image, angle)
    # fig, (ax1, ax2) = plt.subplots(1, 2)
    # ax1.imshow(orig_image)
    # ax1.set_title("Original image")

    # ax2.imshow(result)
    # ax2.imshow("After rotation")

    # plt.show()
    cv2.imwrite(os.path.join(OUTPUT_PATH, image_name[:image_name.find(".")]+"_rotated.jpg"), result)
    print("Saved your result as {}".format(os.path.join(OUTPUT_PATH, image_name[:image_name.find(".")]+"_rotated.jpg")))    