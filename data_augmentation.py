import albumentations as A
import cv2
import os
from matplotlib import pyplot as plt

def visualize(image):
    # Divide all values by 65535 so we can display the image using matplotlib
    image = image / 65535
    plt.figure(figsize=(10, 10))
    plt.axis('off')
    plt.imshow(image)

# Declare an augmentation pipeline
transform = A.Compose([
    A.ToFloat(max_value=65535.0),
    A.RandomRotate90(),
    A.Flip(),
    A.OneOf([
        A.MotionBlur(p=0.2),
        A.MedianBlur(blur_limit=3, p=0.1),
        A.Blur(blur_limit=3, p=0.1),
    ], p=0.2),
    A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.2, rotate_limit=45, p=0.2),
    A.OneOf([
        A.OpticalDistortion(p=0.3),
        A.GridDistortion(p=0.1),
    ], p=0.2),
    A.HueSaturationValue(hue_shift_limit=20, sat_shift_limit=0.1, val_shift_limit=0.1, p=0.3),

    A.FromFloat(max_value=65535.0),
])

# Read an image with OpenCV and convert it to the RGB colorspace
images = os.path.join(os.getcwd(), r'data/images')

image = cv2.imread(os.path.join(images, r'cat.jpg'))
visualize(image)
cv2.imshow("orginal image", image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
visualize(image)
cv2.imshow("color image", image)

# Augment an image
transformed = transform(image=image)
transformed_image = transformed["image"]
visualize(transformed["image"])
cv2.imwrite("transformedimage.jpg", transformed["image"])

transform = A.HorizontalFlip(p=0.5)
augmented_image = transform(image=image)['image']
cv2.imwrite("transformedimage_1.jpg", transformed["image"])
