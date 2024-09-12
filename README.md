            Forensic Image Metadata Extraction Tool


This Python-based tool extracts metadata from images in a specified folder, including camera settings, timestamps, and GPS location if available. It generates a Google Maps link for the location data and saves all extracted metadata to a text file for forensic or educational purposes.


Features
    Extracts EXIF metadata such as camera model, ISO, exposure, and more.
    Retrieves GPS data if available and converts it to a Google Maps link for easy visualization of the image's location.
    Supports multiple image formats such as .jpg, .jpeg, .png, .tiff, .bmp, and .gif.
    Offers automatic folder detection (defaulting to an "images" folder in the same directory as the script).
    Saves the extracted metadata in a human-readable text file.

Warning
    This tool is intended for educational purposes only. Images sourced from social media platforms like Instagram or Snapchat may have their metadata stripped to protect user privacy, which could result in less or no data being available.

Installation
    Prerequisites
        Make sure you have Python installed (version 3.6 or above). You'll also need to install the following Python libraries:

        Pillow for image manipulation
        ExifRead for extracting EXIF metadata
        pyfiglet for ASCII art (optional for decoration)
        Install the required libraries using pip:

        ## pip install exifread Pillow pyfiglet

    Clone the Repository
        Clone this repository to your local machine:
        ## git clone https://github.com/your-username/Forensic-Metadata-Extractor.git
        cd Forensic-Metadata-Extractor

Usage
    1. Place your images inside an images folder located in the same directory as the script, or specify a custom folder path.
    2. Run the Python script:

    # python metadata_extractor.py

    3. You will be presented with the following options:

    Press 1 for automatic selection of the images folder.
    Press 2 to provide a custom folder path.
    Press 3 to exit.
    4. The extracted metadata will be saved in a file named metadata_output.txt in the same directory as the script.

Example Output
    Here’s an example of how the metadata might look:

    # 
    Metadata for example.jpg:
    Image Make: Canon
    Image Model: EOS 5D Mark III
    Image DateTime: 2021:08:12 10:30:45
    GPS Latitude: 37.7749
    GPS Longitude: -122.4194
    Google Maps URL: https://www.google.com/maps/?q=37.7749,-122.4194
    #

Contributing
    Contributions are welcome! Feel free to open issues or submit pull requests. Please make sure your contributions align with the goals of the project and follow the code of conduct.
