import os
import albumentations as A
import cv2

# Encoded label details: (Total 4 categories)
# cat = 1
# dog = 3

def get_the_list_of_image_name():
    imagename_cat = []
    imagename_dog = []
    
    folder = os.path.join(os.getcwd(), r'data/labels')
    for count, filename in enumerate(os.listdir(folder)):
        file1 = open(os.path.join(folder, filename), 'r')
        print(f"\nReading {filename}")
        Lines = file1.readlines()
        for line in Lines:
            encoded_value = line.strip().split(' ', 1)[0]
            print("Encoded value: ", encoded_value)
            encoded_value = int(encoded_value)
            if encoded_value == 1:
                print(f"Appending the filename for cat - {filename.split('.', 1)[0]}")
                imagename_cat.append(filename.split('.', 1)[0])
            elif encoded_value == 3:
                print(f"Appending the filename for dog - {filename.split('.', 1)[0]}")
                imagename_dog.append(filename.split('.', 1)[0])
            else:
                print("Perform nothing")
    print("\nResults: ")
    print("Total cat: ", imagename_cat)
    print("\nTotal dog: ", imagename_dog)
    return imagename_cat, imagename_dog
  
# Function to iterate all the files inside a folder
def main():
    imagename_cat, imagename_dog = get_the_list_of_image_name()

    # Now perform data augmentation:
    count_reqd_for_cat = 187
    count_reqd_for_dog = 255
    images = os.path.join(os.getcwd(), r'data\images')
    new_cat = os.path.join(os.getcwd(), r'data\cat')
    new_dog = os.path.join(os.getcwd(), r'data\dog')
    count_cat = 0
    count_dog = 0

    cat_image_missing = []

    for each in imagename_cat:
        if count_cat < count_reqd_for_cat:
            imagename = str(each) +'.jpg'
            if os.path.isfile(os.path.join(images, imagename)):
                print("imagename", os.path.join(images, imagename))
                image = cv2.imread(os.path.join(images, imagename))
                # cv2.imshow("orginal_image", image)

                # Color change
                #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                #cv2.imshow("color image", image)

                # Augment an image
                transform = A.HorizontalFlip(p=0.5)
                augmented_image = transform(image=image)['image']
                count_cat += 1
                cv2.imwrite(os.path.join(new_cat, each + '_' + str(count_cat) + '.jpg'), augmented_image)

                transform = A.RandomRotate90()
                augmented_image = transform(image=image)['image']
                count_cat += 1
                cv2.imwrite(os.path.join(new_cat, each + '_' + str(count_cat) + '.jpg'), augmented_image)

                transform = A.OneOf([
                                        A.MotionBlur(p=0.2),
                                        A.MedianBlur(blur_limit=3, p=0.1),
                                        A.Blur(blur_limit=3, p=0.1),
                                    ], p=0.2)
                augmented_image = transform(image=image)['image']
                count_cat += 1
                cv2.imwrite(os.path.join(new_cat, each + '_' + str(count_cat) + '.jpg'), augmented_image)

                transform = A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.2, rotate_limit=45, p=0.2)
                augmented_image = transform(image=image)['image']
                count_cat += 1
                cv2.imwrite(os.path.join(new_cat, each + '_' + str(count_cat) + '.jpg'), augmented_image)
            else:
                print("Image not found")
                cat_image_missing.append(each)
    print("Missing images of cat: ", cat_image_missing)
    print("Total count of missing images: ", len(cat_image_missing))

    dog_image_missing=[]
    for each in imagename_dog:
        if count_dog < count_reqd_for_dog:
            imagename = str(each) +'.jpg'
            if os.path.isfile(os.path.join(images, imagename)):
                print("imagename", os.path.join(images, imagename))
                image = cv2.imread(os.path.join(images, imagename))
                # cv2.imshow("orginal_image", image)

                # Color change
                #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                #cv2.imshow("color image", image)

                # Augment an image
                transform = A.HorizontalFlip(p=0.5)
                augmented_image = transform(image=image)['image']
                count_dog += 1
                cv2.imwrite(os.path.join(new_dog, each + '_' + str(count_dog) + '.jpg'), augmented_image)

                transform = A.RandomRotate90()
                augmented_image = transform(image=image)['image']
                count_dog += 1
                cv2.imwrite(os.path.join(new_dog, each + '_' + str(count_dog) + '.jpg'), augmented_image)

                transform = A.OneOf([
                                        A.MotionBlur(p=0.2),
                                        A.MedianBlur(blur_limit=3, p=0.1),
                                        A.Blur(blur_limit=3, p=0.1),
                                    ], p=0.2)
                augmented_image = transform(image=image)['image']
                count_dog += 1
                cv2.imwrite(os.path.join(new_dog, each + '_' + str(count_dog) + '.jpg'), augmented_image)

                transform = A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.2, rotate_limit=45, p=0.2)
                augmented_image = transform(image=image)['image']
                count_dog += 1
                cv2.imwrite(os.path.join(new_dog, each + '_' + str(count_dog) + '.jpg'), augmented_image)

                transform = A.OneOf([
                                    A.OpticalDistortion(p=0.3),
                                    A.GridDistortion(p=0.1),
                                     ], p=0.2)
                augmented_image = transform(image=image)['image']
                count_dog += 1
                cv2.imwrite(os.path.join(new_dog, each + '_' + str(count_dog) + '.jpg'), augmented_image)

                transform = A.FromFloat(max_value=65535.0)
                augmented_image = transform(image=image)['image']
                count_dog += 1
                cv2.imwrite(os.path.join(new_dog, each + '_' + str(count_dog) + '.jpg'), augmented_image)

                transform = A.HueSaturationValue(hue_shift_limit=20, sat_shift_limit=0.1, val_shift_limit=0.1, p=0.3)
                augmented_image = transform(image=image)['image']
                count_dog += 1
                cv2.imwrite(os.path.join(new_dog, each + '_' + str(count_dog) + '.jpg'), augmented_image)
            else:
                print("Image not found")
                dog_image_missing.append(each)
    print("Missing images of dog: ", dog_image_missing)
    print("Total count of missing images: ", len(dog_image_missing))

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
