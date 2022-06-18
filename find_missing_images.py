import os

# Encoded label details: (Consider total 3 categories)
# cat = 0
# dog = 1
# cow = 2

def get_the_list_of_image_name():
    imagename_cat = []
    imagename_dog = []
    imagename_cow = []
    
    # Specify the path where the labels text file is present
    folder = r'<Enter your lables text file path here>'
    # folder = os.path.join(os.getcwd(), r'<Enter your lables text file path here>')
    
    # Iterate through all the files inside the label text file folder
    for count, filename in enumerate(os.listdir(folder)):
        # Read each label text file
        file1 = open(os.path.join(folder, filename), 'r')
        print(f"\nReading {filename}")
        Lines = file1.readlines()
        
        for line in Lines:
            # Extract the encoded value from the labels text file
            encoded_value = line.strip().split(' ', 1)[0]
            print("Encoded value: ", encoded_value)
            encoded_value = int(encoded_value)
            
            # Append the filename of the text file to corresponding category with
            # help of encoded value.
            if encoded_value == 0:
                print(f"Appending the filename for cat - {filename.split('.', 1)[0]}")
                imagename_cat.append(filename.split('.', 1)[0])
            elif encoded_value == 1:
                print(f"Appending the filename for dog - {filename.split('.', 1)[0]}")
                imagename_dog.append(filename.split('.', 1)[0])
            elif encoded_value == 2:
                print(f"Appending the filename for cow - {filename.split('.', 1)[0]}")
                imagename_cow.append(filename.split('.', 1)[0])
            else:
                print("Perform nothing")
    return imagename_cat, imagename_dog, imagename_cow

def deleting_the_labels(image_missing):
    # finding out the duplicates
    res = []
    for i in image_missing:
        if i not in res:
            res.append(i)
    print("Missing images (without duplicates) : ", res)
    print("Total count of missing images (without duplicates) : ", len(res))
    
    # Remove those labels text files which doesn't have images.
    for each in res:
        labelname = str(each) + '.txt'
        delete_path = os.path.join(r'<Enter your lables text file path here>', labelname)
        os.remove(delete_path)
        
def main():
    imagename_cat, imagename_dog, imagename_cow = get_the_list_of_image_name()

    # Specify the image path:
    images = os.path.join(os.getcwd(), r'<Enter the path to the image folder>')
    # images = r'<Enter the path to the image folder>'

    # Now check if the image file name exists in the specified image path or not.
    cat_image_missing = []
    for each in imagename_cat:
        imagename = str(each) + '.jpg'
        if not (os.path.isfile(os.path.join(images, imagename))):
            # If image is not found, then append it to the missing list.
            # print("Image not found")
            cat_image_missing.append(each)
    print("\nMissing images of awake: ", cat_image_missing)
    print("Total count of missing images: ", len(cat_image_missing))
    
    deleting_the_labels(cat_image_missing)

    dog_image_missing = []
    for each in imagename_dog:
        imagename = str(each) + '.jpg'
        if not(os.path.isfile(os.path.join(images, imagename))):
            #print("Image not found")
            dog_image_missing.append(each)
    print("Missing images of empty cup: ", dog_image_missing)
    print("Total count of missing images: ", len(dog_image_missing))

    deleting_the_labels(dog_image_missing)

    cow_image_missing = []
    for each in imagename_cow:
        imagename = str(each) + '.jpg'
        if not(os.path.isfile(os.path.join(images, imagename))):
            #print("Image not found")
            cow_image_missing.append(each)
    print("Missing images of open book: ", cow_image_missing)
    print("Total count of missing images: ", len(cow_image_missing))
    
    deleting_the_labels(cow_image_missing)

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
