import numpy as np

roof1 = np.array([8, 8, 1])   # shingles + siding damage
roof2 = np.array([1, 1, 0])   # shingles + gutter damage
similarity = np.dot(roof1, roof2)
print("Similarity score:", similarity)