import numpy as np

v = np.array([3, 4])  # like a roof with 3 broken shingles, 4 cracked tiles

# Length (magnitude)
length = np.linalg.norm(v)

# Normalize (scale to length 1)
normalized = v / length

print("Original vector:", v)
print("Length:", length)
print("Normalized:", normalized)
print("Length after normalization:", np.linalg.norm(normalized))
