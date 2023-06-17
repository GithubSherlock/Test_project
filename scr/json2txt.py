import os
import json

def extract_labelme_info(folder_path, output_file):
    with open(output_file, 'w') as f:
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.json'):
                json_path = os.path.join(folder_path, file_name)
                with open(json_path) as json_file:
                    data = json.load(json_file)
                    image_name = data['imagePath']
                    annotations = data['shapes']
                    for annotation in annotations:
                        label = annotation['label']
                        points = annotation['points']
                        # Extract any other required information from the annotation

                        # # Write the extracted information to the output file
                        # f.write(f"Image: {image_name}\n")
                        # f.write(f"Label: {label}\n")
                        # f.write(f"Points: {points}\n")
                        # f.write('\n')

                        # Write the extracted information to the output file in a single line
                        f.write(f"Image: {image_name}, Label: {label}, Points: {points}\n")

# Specify the folder path containing LabelMe JSON files
folder_path = './ann'

# Specify the output file path for storing the extracted information
output_file = 'output.txt'

# Call the function to extract information and generate the output file
extract_labelme_info(folder_path, output_file)
