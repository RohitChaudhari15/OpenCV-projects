import cv2

# Load images
image1 = cv2.imread('/home/neosoft/Documents/OpenCV/Finger Counter Using Hand tracking/OUTPUT/1.png')
image2 = cv2.imread('/home/neosoft/Documents/OpenCV/Finger Counter Using Hand tracking/OUTPUT/2.png')
image3 = cv2.imread('/home/neosoft/Documents/OpenCV/Finger Counter Using Hand tracking/OUTPUT/3.png')
image4 = cv2.imread('/home/neosoft/Documents/OpenCV/Finger Counter Using Hand tracking/OUTPUT/4.png')
image5 = cv2.imread('/home/neosoft/Documents/OpenCV/Finger Counter Using Hand tracking/OUTPUT/5.png')
image6 = cv2.imread('/home/neosoft/Documents/OpenCV/Finger Counter Using Hand tracking/OUTPUT/6.png')


# Resize images (optional)
image1 = cv2.resize(image1, (512,512))
image2 = cv2.resize(image2, (512,512))
image3 = cv2.resize(image3, (512,512))
image4 = cv2.resize(image4, (512,512))
image5 = cv2.resize(image5, (512,512))
image6 = cv2.resize(image6, (512,512))


# Combine images horizontally
h_combined_image1 = cv2.hconcat([image1, image2, image3])
h_combined_image2 = cv2.hconcat([image4, image5, image6])
v_Combined_image = cv2.vconcat([h_combined_image1,h_combined_image2])

# v_Combined_image = cv2.resize(v_Combined_image, (1080,720))
# Display or save the combined image
cv2.imshow('Combined Image', v_Combined_image)
cv2.imwrite("output_image.jpg", v_Combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# To save the combined image
# cv2.imwrite('combined_image.png', combined_image)
