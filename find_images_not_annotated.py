import os

def get_the_list_of_image_name():
    # initialize the empty list to collect the image names
    imagename = []

    # Specify the image folder path
    folder = os.path.join(os.getcwd(), r'<Enter the images path here>')
    # folder = r'<Enter the images path here>'

    # Iterate through all the files inside image folder
    for count, filename in enumerate(os.listdir(folder)):
        if filename == "labels":
            print("Do nothing")
        elif filename.rsplit('.', 1)[1] == "jpg":
            # if the extension is .jpg, then append the filename to the list
            print(f"\nAppending {filename}")
            imagename.append(filename.rsplit('.', 1)[0])
        else:
            print("Do nothing")
    return imagename

def delete_images(label_missing):
    # Iterate through the missing labels list
    for each in label_missing:
        # Get the corresponding path to the image
        imagename = str(each) + '.jpg'
        delete_path = os.path.join(r'<enter the image path here>', imagename)
        # Delete those images which are don't have labels text file
        os.remove(delete_path)

# Driver Code
if __name__ == '__main__':
    # Get the list of image names
    imagename = get_the_list_of_image_name()
    print("Total images present: ", len(imagename))

    # Specify the labels folder path
    labels = os.path.join(os.getcwd(), r'<Enter the labels path here>')
    # labels = r'<Enter the labels path here>'

    # Initialize a empty list to collect missing labels list.
    label_missing = []
    for each in imagename:
        labelname = str(each) + '.txt'
        print(os.path.join(labels, labelname))
        print(os.path.isfile(os.path.join(labels, labelname)))
        if not (os.path.isfile(os.path.join(labels, labelname))):
            # If the path to labels text file is not present, then move it to missing list
            print("labels text file not found")
            label_missing.append(each)
    print("\nMissing labels text file: ", label_missing)
    print("Total count of missing labels text file: ", len(label_missing))

    delete_images(label_missing)
