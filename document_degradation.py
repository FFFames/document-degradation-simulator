import cv2
import numpy as np
import random

def add_gaussian_noise(image, mean=0, sigma=10):
    """Adds Gaussian noise to an image."""
    row, col, ch = image.shape
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    noisy = np.clip(image + gauss, 0, 255).astype(np.uint8)
    return noisy

def add_salt_and_pepper(image, prob=0.01):
    """Adds salt and pepper noise."""
    output = np.copy(image)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = [0, 0, 0]
            elif rdn > thres:
                output[i][j] = [255, 255, 255]
    return output

def apply_blur(image, kernel_size=3):
    """Applies Gaussian blur."""
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def simulate_scan(image_path, output_path):
    # Load image
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not read image.")
        return

    # 1. Subtle Blur
    img = apply_blur(img, kernel_size=3)

    # 2. Add Noise
    img = add_gaussian_noise(img, sigma=15)
    img = add_salt_and_pepper(img, prob=0.005)

    # 3. Random Rotation (Slight)
    angle = random.uniform(-0.5, 0.5)
    h, w = img.shape[:2]
    M = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)
    img = cv2.warpAffine(img, M, (w, h), borderMode=cv2.BORDER_CONSTANT, borderValue=(255,255,255))

    # 4. Adjust Contrast (Simulate fading)
    alpha = 0.9 # Contrast control
    beta = 10   # Brightness control
    img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    # Save output
    cv2.imwrite(output_path, img)
    print(f"Degraded document saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    # simulate_scan("input.png", "degraded_output.png")
    pass
