import numpy as np

# Step 0: Create fake image
img = np.random.randint(0, 255, (28, 28))

# Step 1: Normalize
img_norm = img / 255.0

# Step 2: Flip horizontally
img_flip = img[:, ::-1]

# Step 3: Blur using 3x3 average kernel
kernel = np.ones((3,3)) / 9
blurred = np.zeros_like(img, dtype=float)

for i in range(1,27):
    for j in range(1,27):
        region = img[i-1:i+2, j-1:j+2]
        blurred[i,j] = np.sum(region * kernel)

# Step 4: Binary threshold
binary = (img_norm > 0.5).astype(int)

print("Normalized:\n", img_norm)
print("Flipped:\n", img_flip)
print("Blurred:\n", blurred)
print("Binary:\n", binary)
