from PIL import Image
import random
import numpy as np

def extract_patches_one_image(image, patch_size, gap):
    """
    image: (H, W, C)

    Returns:
        patch_a: (P, P, C)
        patch_b: (P, P, C)
        label: integer in [0, 7]
    """
    H, W, C = image.shape
    S = patch_size + gap

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    # Choose one of the 8 relative positions
    label = random.randrange(8)
    dy, dx = directions[label]

    # Choose a valid reference patch location
    valid_y = list(range(
        max(0, -dy * S),
        min(H - patch_size, H - patch_size - dy * S) + 1
    ))
    valid_x = list(range(
        max(0, -dx * S),
        min(W - patch_size, W - patch_size - dx * S) + 1
    ))

    y = random.choice(valid_y)
    x = random.choice(valid_x)

    # Extract the two patches
    patch_a = image[y:y+patch_size, x:x+patch_size, :]

    y_b = y + dy * S
    x_b = x + dx * S

    patch_b = image[y_b:y_b+patch_size, x_b:x_b+patch_size, :]

    return patch_a, patch_b, label



if __name__ == "__main__":
    img_name = "img.png"
    img = Image.open(img_name)
    img = np.array(img)

    patch_a, patch_b, label = extract_patches_one_image(img, 100, 20)
    print(img.shape)
    print(patch_a.shape, patch_b.shape, label)

    patch_a_img = Image.fromarray(patch_a)
    patch_a_img.show("patch A")

    patch_b_img = Image.fromarray(patch_b)
    patch_b_img.show("patch B")