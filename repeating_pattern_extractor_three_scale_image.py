import numpy as np
import cv2
import time


def calculate_l2_loss(image1, image2):
    """Calculate the L2 loss between two images."""
    diff = image1.astype(float) - image2.astype(float)
    l2_loss = np.sqrt(np.sum(diff ** 2, axis=-1))  # Per-pixel L2 loss
    return np.mean(l2_loss)

def find_repeating_pattern_with_left_to_right_sliding(image):
    """Detect repeating pattern from left to right."""
    h, w, c = image.shape
    losses = []
    
    # Sliding process: Move right portion of the image leftward
    for shift in range(w):
        # Define overlapping region
        reference = image[:, shift:, :]  # Fixed left region
        sliding = image[:, :w - shift, :]  # Sliding right region
        
        # Compute L2 loss for the overlapping region
        loss = calculate_l2_loss(reference, sliding)
        losses.append(loss)
    
    
    midline = (max(losses) + min(losses)) / 2
    ascending_crosses = np.where((np.array(losses[:-1]) < midline) & (np.array(losses[1:]) > midline))[0]

    if len(ascending_crosses) >= 2:
        x_min = ascending_crosses[0]  # Ascending region of the first curve
        x_max = ascending_crosses[1]    # Ascending region of the second curve
        return x_min, x_max
    else:
        print("Not enough ascending regions crossing the midline to draw the segment.")
        print(f"Left to Right Sliding Coordinates : {ascending_crosses}")
        return None, None


def find_repeating_pattern_with_top_to_bottom_sliding(image):
    """Detect repeating pattern and dynamically visualize sliding from top to bottom."""
    h, w, c = image.shape
    losses = []

    # Sliding process: Move top portion of the image downward
    for shift in range(h):
        # Define overlapping region
        reference = image[shift:, :, :]  # Fixed top region
        sliding = image[:h - shift, :, :]  # Sliding downward region
        
        # Compute L2 loss for the overlapping region
        loss = calculate_l2_loss(reference, sliding)
        losses.append(loss)
        
    
    midline = (max(losses) + min(losses)) / 2
    ascending_crosses = np.where((np.array(losses[:-1]) < midline) & (np.array(losses[1:]) > midline))[0]

    if len(ascending_crosses) >= 2:
        y_min = ascending_crosses[0]  # Ascending region of the first curve
        y_max = ascending_crosses[1]    # Ascending region of the second curve
        return y_min, y_max
    else:
        print("Not enough ascending regions crossing the midline to draw the segment.")
        print(f"Top to Bottom Sliding Coordinates : {ascending_crosses}")
        return None, None


def find_repeating_pattern_unit(image_path):
    start_time = time.time()
    image = cv2.imread(image_path) 
    y_min, y_max = find_repeating_pattern_with_top_to_bottom_sliding(image)
    x_min, x_max = find_repeating_pattern_with_left_to_right_sliding(image)
    if all([x_min, x_max, y_min, y_max]):
        pattern = image[y_min:y_max, x_min:x_max, :]
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("The time of execution of above program is :",
        elapsed_time, "seconds")
        cv2.imshow("Repeating Pattern Unit", pattern)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("There is no Repeating Pattern in image")

if __name__ == "__main__":
    img_path = "images_pattern\\rp13.jpg"
    find_repeating_pattern_unit(img_path)




