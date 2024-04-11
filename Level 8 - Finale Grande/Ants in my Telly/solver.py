import cv2
import os
import numpy as np
from PIL import Image

def extract_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    # Read the video frames
    success, frame = cap.read()
    frame_count = 0

    # Loop through frames
    while success:
        # Save frame as an image
        frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)

        # Read next frame
        success, frame = cap.read()
        frame_count += 1

    # Release the video capture object
    cap.release()
    print("Frames extracted successfully.")


def calculate_average_image(folder_path):
    images = []
    
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.jpg'):  # Assuming images are jpg or png
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)
            if image is not None:
                images.append(image)
    
    # Calculate average image
    if len(images) > 0:
        average_image = np.mean(images, axis=0).astype(np.uint8)
        return average_image
    else:
        print("No images found in the folder.")
        return None
    

def parse_grid_in_binary_file(image_path):
    # Open the image
    image = Image.open(image_path)
    
    # Convert image to grayscale
    gray_image = image.convert('L')
    
    # Get width and height of the image
    width, height = gray_image.size
    
    cipher = []
    # Iterate through each row of the image
    for y in range(height):
        # Get the pixel values of the current row
        row_pixels = list(gray_image.getdata())[y * width: (y + 1) * width]
        
        # Find the index of the whitest pixel (pixel with maximum value)
        white_index = row_pixels.index(max(row_pixels))
        
        # Initialize a list to store the binary values
        binary_values = []
        
        # Iterate through each pixel in the row
        for x, pixel_value in enumerate(row_pixels):
            # Append '0' if the pixel is not the whitest, otherwise append '1'
            binary_values.append('1' if x == white_index else '0')
        
        # Write the binary values of the row to the text file
        cipher.append(''.join(binary_values))
    return cipher


def get_known_key_values(cipher_lines):
    key = []
    for i, t in enumerate("he2024{"):
        entry = {
            "index": cipher_lines[i].index('1'),
            "value": t
        }
        if entry not in key:
            key.append(entry)
    
    key.append({
        "index": cipher_lines[len(cipher_lines)-1].index('1'),
        "value": "}"
    })

    key.append({  # From frequency analysis
        "index": 16,
        "value": "_"
    })

    key.append({  # Assume because of ending too
        "index": 13,
        "value": "t"
    })

    # 1_w0nder_who_
    key.append({  # Test
        "index": 0,
        "value": "1"
    })

    key.append({  # Test
        "index": 10,
        "value": "w"
    })

    key.append({  # Test
        "index": 18,
        "value": "n"
    })

    key.append({  # Test
        "index": 17,
        "value": "d"
    })

    key.append({  # Test
        "index": 8,
        "value": "3"
    })

    key.append({  # Test
        "index": 26,
        "value": "r"
    })

    key.append({  # Test
        "index": 19,
        "value": "o"
    })

    key.append({  # Test
        "index": 36,
        "value": "5"
    })

    key.append({  # Test
        "index": 21,
        "value": "p"
    })

    key.append({  # Test
        "index": 15,
        "value": "b"
    })

    key.append({  # Test
        "index": 11,
        "value": "a"
    })

    key.append({  # Test
        "index": 33,
        "value": "j"
    })

    key.append({  # Test
        "index": 29,
        "value": "u"
    })

    return key


def print_frequency_anaylsis(cipher_lines):
    frequencies = []
    for line, line_value in enumerate(cipher_lines):
        value = cipher_lines[line].index('1')
        found = False
        for index, entry in enumerate(frequencies):
            if not found:
                if entry["value"] == value:
                    frequencies[index]["count"] = frequencies[index]["count"] + 1
                    found = True

        if not found:
            frequencies.append({
                "value": value,
                "count": 1
            })

    sorted_frequencies = sorted(frequencies, key=lambda d: d['count'], reverse=True)
    for entry in sorted_frequencies:
        print(entry)
                



def main():
    # change working directory to script location
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    video_path = "./working_files/only_codes_from_video/cutted_video.mp4"
    image_frame_folder = "./working_files/only_codes_in_video_as_images/"
    # extract_frames(video_path, image_frame_folder)
    
    avg_image = calculate_average_image(image_frame_folder)
    if avg_image is not None:
        cv2.imwrite("average_image.jpg", avg_image)
        print("Average image saved as average_image.jpg")

    # Open the image
    image = Image.open("average_image.jpg")
    # Resize the image to width 40 and height 55
    resized_image = image.resize((40, 55))
    # Save the resized image
    resized_image.save("average_image_resized.jpg")

    cipher_lines = parse_grid_in_binary_file("average_image_resized.jpg")

    solution = []
    key = get_known_key_values(cipher_lines)

    
    print(key)

    print_frequency_anaylsis(cipher_lines)


    for row, line in enumerate(cipher_lines):
        one_index = cipher_lines[row].index('1')
        for key_index, key_entry in enumerate(key):
            if key[key_index]["index"] == one_index:
                line = line.replace("0", "")
                line = line.replace("1", key_entry["value"])
        print("{0},     {1}".format(one_index, line))


if __name__ == '__main__':
    main()