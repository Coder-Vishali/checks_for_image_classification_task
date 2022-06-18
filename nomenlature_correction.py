import os

# Function to rename multiple files
def main():
    folder = r"<Enter the image path here>"
    txt_folder = r"<Enter the labels path here>"
    counter = 0
    
    # Iterate through the images folder
    for count, filename in enumerate(os.listdir(folder)):
        # If the extension is jpg - this is to confirm whether it is a image
        if filename.rsplit('.',1)[1] == "jpg":
            print("first filename", filename)
            # Provide proper naming convention here
            dst = f"cat_{str(counter)}.jpg"
            src = f"{folder}\{filename}"  # foldername/filename, if .py file is outside folder
            dst = f"{folder}\{dst}"
            # rename() function will
            # rename all the files
            os.rename(src, dst)
            
            # Iterate through the labels text file folder
            for count_txt, filename_txt in enumerate(os.listdir(txt_folder)):
                # Identify whether the filename matches or not
                if filename.rsplit('.',1)[0] == filename_txt.rsplit('.',1)[0]:
                    print("filename", filename.split('.',1)[0])
                    print("filename_txt", filename_txt.split('.',1)[0])
                    # Provide similar naming convention here
                    dst = f"cat_{str(counter)}.txt"
                    txt_src = f"{txt_folder}\{filename_txt}"  # foldername/filename, if .py file is outside folder
                    txt_dst = f"{txt_folder}\{dst}"
                    os.rename(txt_src, txt_dst)
            counter += 1

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
