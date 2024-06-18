
import cv2
import numpy as np

def analyze_colors(image_path):

    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Failed to load image")
        return {}   

    # Convert to RGB (OpenCV uses BGR by default)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Assuming the strip has 10 different pads
    colors = []
    height, width, _ = image.shape
    pad_height = height // 10  # Divide the image height by the number of pads

    # Labels based on typical urine strip tests
    test_labels = ['URO', 'BIL', 'KET', 'SG', 'BLOOD', 'pH', 'PRO', 'NIT', 'LEU', 'GLU']
    test_results = {}

    for i, label in enumerate(test_labels):
        # Extract the color of each strip section
        section = image[i * pad_height:(i + 1) * pad_height, :]
        avg_color = np.mean(section, axis=(0, 1))  # Average color in the section
        test_results[label] = avg_color.astype(int).tolist()

    return test_results
