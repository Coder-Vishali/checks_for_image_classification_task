import os

# Function to rename multiple files
def main():
    folder = r"<Enter the path here"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"image_{str(count)}.jpg"
        src = f"{folder}/{filename}" 
        dst = f"{folder}/{dst}"
        # rename() function will
        # rename all the files
        os.rename(src, dst)

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
