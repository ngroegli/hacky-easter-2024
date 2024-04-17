from PIL import Image

# Function to get neighbors of a pixel
def get_neighbors(image, x, y):
    neighbors = []
    width, height = image.size
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx < width and ny >= 0 and ny < height and (dx != 0 or dy != 0):
                neighbors.append((nx, ny))
    return neighbors

# Connected component labeling function
def label_components(image):
    pixels = image.load()
    width, height = image.size
    labels = [[0 for _ in range(width)] for _ in range(height)]
    current_label = 0

    for y in range(height):
        for x in range(width):
            if pixels[x, y] == 0 and labels[y][x] == 0:
                current_label += 1
                stack = [(x, y)]
                while stack:
                    cx, cy = stack.pop()
                    labels[cy][cx] = current_label
                    for nx, ny in get_neighbors(image, cx, cy):
                        if pixels[nx, ny] == 0 and labels[ny][nx] == 0:
                            stack.append((nx, ny))
    return labels, current_label

# Function to extract symbols and save them
def extract_and_save_symbols(image_path):
    img = Image.open(image_path)
    img_gray = img.convert('L')
    threshold = 100  # adjust threshold as needed
    img_binary = img_gray.point(lambda p: p > threshold and 255)

    labels, num_labels = label_components(img_binary)

    for label_id in range(1, num_labels + 1):
        min_x, min_y, max_x, max_y = img.size[0], img.size[1], 0, 0
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if labels[y][x] == label_id:
                    min_x = min(min_x, x)
                    min_y = min(min_y, y)
                    max_x = max(max_x, x)
                    max_y = max(max_y, y)
        if max_x - min_x > 5 and max_y - min_y > 5:  # Skip small regions (noise)
            symbol = img.crop((min_x, min_y, max_x + 1, max_y + 1))
            symbol.save(f'line_{min_y}_symbol_{min_x}.png')

if __name__ == "__main__":
    # Replace 'input_image.png' with the path to your input image
    extract_and_save_symbols('west-5-only.png')
