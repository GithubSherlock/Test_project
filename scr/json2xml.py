import os
import json
import xml.etree.ElementTree as ET


def extract_info_from_json(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)

    root = ET.Element("annotations")

    image_filename = data["imagePath"]
    image_width = data["imageWidth"]
    image_height = data["imageHeight"]

    image_element = ET.SubElement(root, "image")
    filename_element = ET.SubElement(image_element, "filename")
    width_element = ET.SubElement(image_element, "width")
    height_element = ET.SubElement(image_element, "height")

    filename_element.text = image_filename
    width_element.text = str(image_width)
    height_element.text = str(image_height)

    for shape in data["shapes"]:
        label = shape["label"]
        points = shape["points"]

        annotation = ET.SubElement(root, "annotation")
        label_element = ET.SubElement(annotation, "label")
        points_element = ET.SubElement(annotation, "points")

        label_element.text = label
        points_element.text = str(points)

    return root


def generate_xml(json_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    root = ET.Element("dataset")

    for file in os.listdir(json_folder):
        if file.endswith(".json"):
            json_path = os.path.join(json_folder, file)
            annotation = extract_info_from_json(json_path)
            root.append(annotation)

    tree = ET.ElementTree(root)
    xml_path = os.path.join(output_folder, "annotations.xml")
    tree.write(xml_path, encoding="utf-8", xml_declaration=True)


# 指定包含 JSON 文件的文件夹路径
json_folder = "./ann"

# 指定输出文件夹路径
output_folder = "./XML_output"

# 生成 XML 文件
generate_xml(json_folder, output_folder)
