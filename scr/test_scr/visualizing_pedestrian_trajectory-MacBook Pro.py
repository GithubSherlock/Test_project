import cv2
import os
import numpy as np
import xml.etree.ElementTree as ET

# Build a function for parsing the given XML files
def parse_xml_file(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data = []
    for child in root:
        if child.tag == 'filename':
            data.append(child.text)
        elif child.tag == 'path':
            data.append(child.text)
        elif child.tag == 'object':
            for obj_child in child:
                if obj_child.tag == 'name':
                    data.append(obj_child.text)
                elif obj_child.tag == 'bndbox':
                    bbox_data = []
                    for bbox in obj_child:
                        bbox_data.append(int(bbox.text))
                    data.extend(bbox_data)

    return data

# Build a function for processing XML files in a given folder
def process_xml_files(folder_path):
    file_names = [f'frame_{i}' for i in range(10, 1411)]
    frame_data = {}

    for file_name in file_names:
        xml_file = os.path.join(folder_path, f'{file_name}.xml')
        if os.path.exists(xml_file):
            data = parse_xml_file(xml_file)
            frame_data[file_name] = data

    return frame_data

# Build a function to compute image coordinates of pedestrians
def create_image_coordinates(frame_data):
    Location_frame = []
    Location_x = []
    Location_y = []

    for key in frame_data:
        frame_number = int(key.split('_')[1])  # Extract the numeric part of the file name
        Location_frame.append(f'Location_{frame_number}')
        Location_x.append((frame_data[key][3] + frame_data[key][5]) / 2)
        Location_y.append(frame_data[key][6])
    Location = [Location_frame, [Location_x, Location_y]]

    return Location

# Perform perspective transformations
def perform_perspective_transform(image_path, src, dest, width, height):
    image = cv2.imread(image_path, 1)
    mtx = cv2.getPerspectiveTransform(np.float32(src), np.float32(dest))
    output_image = cv2.warpPerspective(image, mtx, (width, height))
    return output_image

# Save the transformed image
def save_transformed_image(image, output_path):
    cv2.imwrite(output_path, image)
    print(f"Transformed image saved at: {output_path}")

# Display the original image and the transformed image
def display_images(original_image, transformed_image):
    cv2.imshow('Org map', original_image)
    cv2.imshow('Perspective transformed map', transformed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    # Set the folder path
    folder_path = './annotation'

    # Process XML files and get frame data
    frame_data = process_xml_files(folder_path)

    # Create image coordinate data
    Location = create_image_coordinates(frame_data)

    # Read input images and set the width and height of the output image
    image_path = './output/output_frames/frame_1450.png'
    image_org = cv2.imread(image_path, 1)
    width = 1280  # You can also try (1920, 1080)
    height = 720

    # Input the pixel coordinates of the reference point in the image
    src = [[458, 48], [1418, 32], [1588, 211], [542, 184]]
    dest = np.float32([[212, 214], [633, 236], [527, 474], [266, 405]])

    # Perform perspective transformations
    perspective_transformed_map = perform_perspective_transform(image_path, src, dest, width, height)

    # Specify the save path and file name and save the transformed image
    output_path = './output/output_transformed_image/perspective_transformed_map.png'
    save_transformed_image(perspective_transformed_map, output_path)

    # Display the original image and the transformed image
    display_images(image_org, perspective_transformed_map)

    # Organize the coordinates of the transformed person as a list and as integers
    Location_x = [int(x) for x in Location[1][0]]
    Location_y = [int(y) for y in Location[1][1]]

if __name__ == "__main__":
    main()
