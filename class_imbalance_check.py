import os
import shutil
import numpy as np
import matplotlib.pyplot as plt

# Encoded label details: (Total 4 categories)
# cat = 0
# dog = 1
# cow = 2
# bird = 3

def main():
    count_cat = 0
    count_dog = 0
    count_cow = 0
    count_bird = 0
    
    folder = os.path.join(os.getcwd(), r'labels')
    
    for count, filename in enumerate(os.listdir(folder)):
        file1 = open(os.path.join(folder, filename), 'r')
        print(f"\nReading {filename}")
        
        Lines = file1.readlines()
        for line in Lines:
            encoded_value = line.strip().split(' ', 1)[0]
            # print("Encoded value: ", encoded_value)
            encoded_value = int(encoded_value)
            if encoded_value == 0:
                count_cow += 1
            elif encoded_value == 1:
                count_dog += 1
            elif encoded_value == 2:
                count_cow += 1
            else:
                count_bird += 1

    print("\nDataset Distribution: ")
    print("Total cat: ", count_cat)
    print("Total dog: ", count_dog)
    print("Total cow: ", count_cow)
    print("Total bird: ", count_bird)

    data = {'cat': count_cat,
            'dog': count_dog,
            'cow': count_cow,
            'bird': count_bird}
            
    classes = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(classes, values, color='maroon', width=0.4)

    plt.xlabel("Classes")
    
    plt.ylabel("No. of instance")
    plt.title("Dataset Distribution")
    plt.show()

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
