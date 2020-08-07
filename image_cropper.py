import argparse
import cv2
import os

refPt = []
cropping = False
def click_and_crop(event, x, y, flags, param):
	global refPt, cropping
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True
	elif event == cv2.EVENT_LBUTTONUP:
		refPt.append((x, y))
		cropping = False
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 255), 2)
		cv2.imshow("image", image)

if __name__ == "__main__":
    INPUT_PATH = os.path.join(os.getcwd(), "input")
    OUTPUT_PATH = os.path.join(os.getcwd(), "output_crop")
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    ap.add_argument("-w", "--width", required=True, help="Width of image")
    ap.add_argument("--height", required=True, help="Height of image")
    args = vars(ap.parse_args())

    image_path = os.path.join(INPUT_PATH, args["image"])
    image_name = args['image']
    image = cv2.imread(image_path)
    image = cv2.resize(image, (int(args['width']), int(args['height'])))
    clone = image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
    
    while True:
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("r"):
            image = clone.copy()
        elif key == ord("s"):
            break
    flag = True
    while flag == True and len(refPt) == 2:
        roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        key_1 = cv2.waitKey(1) & 0xFF
        if key_1 == ord('s'):
            cv2.destroyAllWindows()
            while True:
                cv2.imshow("Do you want to save this?", roi)
                key_2 = cv2.waitKey(1) & 0xFF
                if key_2 == ord('y'):
                    print("Writing image to desired path: {}".format(os.path.join(OUTPUT_PATH, image_name[:image_name.find(".")]+"_cropped.jpg")))
                    cv2.imwrite(os.path.join(OUTPUT_PATH, image_name[:image_name.find(".")]+"_cropped.jpg"), roi)
                    flag = False
                    break
                elif key_2 == ord('n'):
                    flag = False
                    break   
        elif key_1 == ord('x'):
            break
    # # close all open windows
    cv2.destroyAllWindows()        