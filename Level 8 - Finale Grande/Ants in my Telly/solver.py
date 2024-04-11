import cv2
import os
import numpy as np

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


if __name__ == '__main__':
    main()