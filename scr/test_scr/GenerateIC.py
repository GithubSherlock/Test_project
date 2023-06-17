import os
import xml.etree.ElementTree as ET

#  Build a function for parsing the given XML files
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

#  Build a function for processing XML files in a given folder
def process_xml_files(folder_path):
    file_names = [f'frame_{i}' for i in range(10, 1411)]
    frame_data = {}

    for file_name in file_names:
        xml_file = os.path.join(folder_path, f'{file_name}.xml')
        if os.path.exists(xml_file):
            data = parse_xml_file(xml_file)
            frame_data[file_name] = data

    return frame_data

#  Build a function to compute image coordinates of pedestrian
def create_image_coordinate(frame_data):
    Location_frame = []
    Location_x = []
    Location_y = []

    for key in frame_data:
        frame_number = int(key.split('_')[1])  # Extracts the numeric part of the file name
        Location_frame.append(f'Location_{frame_number}')
        Location_x.append((frame_data[key][3] + frame_data[key][5]) / 2)
        Location_y.append(frame_data[key][6])
    Location = [Location_frame, [Location_x, Location_y]]

    return Location

# Generate data files as txt and XML file
def generate_txt_file(Location, file_path):
    with open(file_path, 'w') as file:
        for i in range(len(Location[0])):
            line = f"{Location[0][i]} {Location[1][0][i]} {Location[1][1][i]}\n"
            file.write(line)

def generate_xml_file(Location, file_path):
    root = ET.Element("root")

    for i in range(len(Location[0])):
        frame_element = ET.SubElement(root, "frame")
        frame_element.set("number", Location[0][i])

        x_element = ET.SubElement(frame_element, "x")
        x_element.text = str(Location[1][0][i])

        y_element = ET.SubElement(frame_element, "y")
        y_element.text = str(Location[1][1][i])

    tree = ET.ElementTree(root)
    tree.write(file_path, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    # Set the folder path
    folder_path = './annotation'

    # Process XML files and get frame data
    frame_data = process_xml_files(folder_path)

    # Extract xmin, ymin, xmax, ymax values. The coordinate information of the bounding box is extracted
    # and stored in four lists, xmin, ymin, xmax and ymax, respectively.
    xmin = []
    ymin = []
    xmax = []
    ymax = []
    for key in frame_data:
        xmin.append(frame_data[key][3])
        ymin.append(frame_data[key][4])
        xmax.append(frame_data[key][5])
        ymax.append(frame_data[key][6])

    # Create image coordinate data
    Locations = create_image_coordinate(frame_data)
    print(Locations)
    print(Locations[0][1])

    # # Generate TXT file
    # txt_file_path = "./person_IC/person_IC_data.txt"
    # generate_txt_file(Location, txt_file_path)
    # print(f"TXT file '{txt_file_path}' generated successfully.")
    #
    # # Generate XML file
    # xml_file_path = "./person_IC/person_IC_data.xml"
    # generate_xml_file(Location, xml_file_path)
    # print(f"XML file '{xml_file_path}' generated successfully.")

# The following is test codes
# first_location = Location[0][0]
# print(first_location)

# print(xmin)
# print(ymin)
# print(xmax)
# print(ymax)

# print(frame_data['frame_10'])
# print(frame_data['frame_20'])
# print(frame_data['frame_1410'])