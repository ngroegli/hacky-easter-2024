import os
import cv2
import re

# Function to calculate similarity between two images using ORB feature matching
def image_similarity(image1, image2):
    # Convert images to grayscale
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Resize images to a common size
    size = (min(image1.shape[1], image2.shape[1]), min(image1.shape[0], image2.shape[0]))
    image1_resized = cv2.resize(image1_gray, size)
    image2_resized = cv2.resize(image2_gray, size)

    # Calculate Structural Similarity Index (SSI)
    similarity_index = cv2.matchTemplate(image1_resized, image2_resized, cv2.TM_CCOEFF_NORMED)
    
    return similarity_index

# Function to find the best matching sample for an image
def find_best_match(image, samples):
    best_match = None
    max_similarity = -1  # Initialize maximum similarity to a minimum value
    
    # Ensure the image is not empty
    if image is None:
        return best_match
    
    # Iterate through sample images
    for sample_type, sample_image in samples.items():
        similarity = image_similarity(image, sample_image)
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = sample_type
    
    return best_match


# Path to the folder containing images
image_folder = './each_eye/'

# Path to the folder containing sample images
sample_folder = os.path.join(image_folder, 'samples')

# Dictionary to hold sample images
samples = {}

# Load sample images
for filename in os.listdir(sample_folder):
    if filename.endswith('.png'):
        sample_type = filename.split('_')[0]
        sample_image = cv2.imread(os.path.join(sample_folder, filename))
        samples[sample_type] = sample_image

# Custom sorting function for numerical sorting
def numerical_sort(filename):
    if not filename.startswith('line'):
        return (float('inf'), float('inf'))  # Return a large tuple for filenames that don't start with 'line'
    parts = filename.split('_')
    line_number = int(parts[1])
    symbol_number = int(parts[3].split('.')[0])  # Remove file extension and extract symbol number
    return line_number, symbol_number


cipher_as_text = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
# Iterate through images and find the best matching sample
for filename in sorted(os.listdir(image_folder), key=numerical_sort):
    image_path = os.path.join(image_folder, filename)
    image = cv2.imread(image_path)
    match = find_best_match(image, samples)

    pattern = r'\d+'
    # Extracting the first number from the file name
    extract = re.search(pattern, filename)
    if extract:
        cipher_as_text[(int(extract.group())-1)/7].append("{0} ".format(match))
    print(f'{filename} matched with sample type: {match}')


for i in range(1,13):
    if i % 2 == 0:
        line = ' '
    else:
        line = ''

    for symbol in cipher_as_text[i]:
        line = line + "{0}".format(symbol)
    
    print(line)

print(cipher_as_text)