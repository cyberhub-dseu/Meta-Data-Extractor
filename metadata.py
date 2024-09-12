import os
import exifread
import pyfiglet

# Create an ASCII art text
ascii_art = pyfiglet.figlet_format("Cyber Hub")

# Print the ASCII art text
print(ascii_art)

# Print an underline (adjust the length to match the text)
underline = '-' * len(ascii_art.split('\n')[0])
print(underline)

# Warning message
warning_message = '''WARNING: 
This tool is intended for educational purposes only. 
It extracts metadata from images, including GPS data, when available.

Please note: 
Images taken from social media platforms like Instagram, Snapchat, and similar apps 
often have metadata stripped to protect user privacy, so there may be limited or no metadata available.
'''
print(warning_message)

# User choice menu
userchoice = int(input('''Press 1 for auto-select images folder 
2 for custom path of images folder
3 for Exit
'''))


# Function to convert GPS coordinates into decimal format
def convert_to_degrees(value):
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den) / 60.0
    s = float(value.values[2].num) / float(value.values[2].den) / 3600.0
    return d + m + s


# Function to extract metadata from a single image, including GPS data
def extract_metadata(image_path):
    with open(image_path, 'rb') as image_file:
        tags = exifread.process_file(image_file, details=False)

    metadata = {}
    gps_data = {}

    for tag in tags.keys():
        metadata[tag] = str(tags[tag])
        # Check for GPS data
        if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
            latitude = convert_to_degrees(tags['GPS GPSLatitude'])
            longitude = convert_to_degrees(tags['GPS GPSLongitude'])
            if 'GPS GPSLatitudeRef' in tags and tags['GPS GPSLatitudeRef'].values != 'N':
                latitude = -latitude
            if 'GPS GPSLongitudeRef' in tags and tags['GPS GPSLongitudeRef'].values != 'E':
                longitude = -longitude
            gps_data = {
                'Latitude': latitude,
                'Longitude': longitude,
                'Google Maps URL': f'https://www.google.com/maps/?q={latitude},{longitude}'
            }

    return metadata, gps_data


# Function to extract metadata from all images in a folder
def extract_metadata_from_folder(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.gif']
    image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(tuple(image_extensions))]

    folder_metadata = {}

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        metadata, gps_data = extract_metadata(image_path)
        folder_metadata[image_file] = {'Metadata': metadata, 'GPS Data': gps_data}

    return folder_metadata


# Function to save metadata to a text file
def save_metadata_to_file(metadata_dict, output_file):
    with open(output_file, 'w') as file:
        for image, data in metadata_dict.items():
            file.write(f"Metadata for {image}:\n")
            metadata = data['Metadata']
            for tag, value in metadata.items():
                file.write(f"{tag}: {value}\n")
            gps_data = data['GPS Data']
            if gps_data:
                file.write(f"\nGPS Data:\n")
                for key, value in gps_data.items():
                    file.write(f"{key}: {value}\n")
            file.write("\n")  # Separate entries with a newline


# Option 1: Auto-select 'images' folder in the same directory as the script
if userchoice == 1:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir, 'images')

    if not os.path.exists(folder_path):
        print(f"Error: The 'images' folder does not exist in {script_dir}")
    else:
        metadata_dict = extract_metadata_from_folder(folder_path)

        # Specify the output file path in the same directory as the script
        output_file = os.path.join(script_dir, 'metadata_output.txt')

        # Save metadata to file
        save_metadata_to_file(metadata_dict, output_file)

        print(f"Metadata has been saved to {output_file}")

# Option 2: User specifies a custom folder path
elif userchoice == 2:
    folder_path = input("Enter the path to the folder containing images: ")

    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
    else:
        metadata_dict = extract_metadata_from_folder(folder_path)

        # Save metadata to a file in the specified folder
        output_file = os.path.join(folder_path, 'metadata_output.txt')

        # Save metadata to file
        save_metadata_to_file(metadata_dict, output_file)

        print(f"Metadata has been saved to {output_file}")

# Option 3: Exit the program
elif userchoice == 3:
    print("Exiting the program.")
    exit()

else:
    print("Invalid choice. Please run the program again.")
