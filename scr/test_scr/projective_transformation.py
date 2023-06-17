import cv2
import numpy as np

# Create pedestrian's image coordinates
person_IC = []
with open("./person_IC/person_IC_data.txt", "r") as file:
    for line in file:
        line = line.strip()  # Remove whitespace characters at the beginning and end of a line
        parts = line.split()  # Splitting rows of data into individual elements
        x = float(parts[1])
        y = float(parts[2])
        person_IC.append((x, y))
# print(person_IC)

# There are control points in GC and IC, we use cp1, cp2, cp4 and cp5. src from IC adn dest from GC
# control_point_1 52.3886490260812 9.713147791957878 458 48
# control_point_2 52.388525085182486 9.713204782219282 542 184
# control_point_3 52.38851989771664 9.713406150903857 1243 149
# control_point_4 52.3886334302395 9.713598558748062 1418 32
# control_point_5 52.38848022131623 9.71348175170328 1588 211
# control_point_6 52.38851730101191 9.713599692467046 1756 129

# Read input images and set the width and height of output image
image = cv2.imread('./output/output_frames/frame_1450.png', 1)
image_org = cv2.imread('./output/output_frames/frame_1450.png', 1)
width = 1920  #1280
height = 1080  #720

# Input the pixel coordinates of the reference point in the image
src = [[458, 48], [1418, 32], [1588, 211], [542, 184]]
dest = np.float32([[212, 214], [633, 236], [527, 474], [266, 405]])

# Compute the projective transformation matrix and geographic coordinates of pedestrian people from the control points
mtx = cv2.getPerspectiveTransform(np.float32(src), np.float32(dest))
original = np.float32([person_IC])
converted = cv2.perspectiveTransform(original, mtx)

# Performing Perspective Transformations
output_image = cv2.warpPerspective(image, mtx, (width, height))

# Specify the save path and file name and save the transformed image
output_path = './output/output_image.png'
cv2.imwrite(output_path, output_image)
print(f"Transformed image saved at: {output_path}")

# Display the original image and the transformed image
cv2.imshow('Org Image', image_org)
cv2.imshow('Transformed Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Organize the coordinates of the transformed person as a list and as an integer
Location_x = []
Location_y = []
for i in range(len(converted[0])):
    x = converted[0][i][0]  # Extract the x coordinate of the i-th location
    y = converted[0][i][1]  # Extract the y coordinate of the i-th location
    Location_x.append(x)  # Add the x coordinate to the Location_x list
    Location_y.append(y)  # Add the y coordinate to the Location_y list
Location_x = [int(x) for x in Location_x]  # Convert to integer
Location_y = [int(y) for y in Location_y]  # Convert to integer

# # Generate TXT file
# txt_file_path = "./person_GC/person_GC_data.txt"
# with open(txt_file_path, "w") as txt_file:
#     for x, y in zip(Location_x, Location_y):
#         txt_file.write(f"{x} {y}\n")
#
# # Generate XML file
# xml_file_path = "./person_GC/person_GC_data.xml"
# with open(xml_file_path, "w") as xml_file:
#     xml_file.write("<data>\n")
#     for x, y in zip(Location_x, Location_y):
#         xml_file.write(f"  <location>\n")
#         xml_file.write(f"    <x>{x}</x>\n")
#         xml_file.write(f"    <y>{y}</y>\n")
#         xml_file.write(f"  </location>\n")
#     xml_file.write("</data>")
