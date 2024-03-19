# import cv2
# import os

# # Define the fixed size
# fixed_width = 100
# fixed_height = 100

# # Path to the folder containing the images
# folder_path = "Fingers"

# # Get the list of filenames in the folder
# file_list = os.listdir(folder_path)

# # Iterate over each image file
# for file_name in file_list:
#     # Construct the full path to the image file
#     file_path = os.path.join(folder_path, file_name)
    
#     # Read the image
#     image = cv2.imread(file_path)
    
#     # Resize the image to the fixed size
#     resized_image = cv2.resize(image, (fixed_width, fixed_height))
    
#     # Write the resized image back to the same file
#     cv2.imwrite(f"new_{file_name}", resized_image)

# print("Done")


# # import cv2
# # import os

# # file_list = os.listdir("Fingers")
# # for file in file_list:
# #     file_path = os.path.join("Fingers", file)
# #     image = cv2.imread(file_path)
# #     print(image.shape)


# list1 = ['5.png', '4.png', '1.png', '3.png', '6.png', '2.png']

# list2 = sorted(list1)

# print(list2)


import cv2
img = cv2.imread('/home/neosoft/Documents/OpenCV/Finger Counter Using Hand tracking/Fingers/1.jpg')
print(img.shape)