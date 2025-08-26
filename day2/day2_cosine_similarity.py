import numpy as np
from numpy.linalg import norm

# Roof 1: mostly shingle damage
roof1 = np.array([10, 2])  # [shingle, tile]
# Roof 2: mostly tile damage
roof2 = np.array([2, 10])

cosine_sim = np.dot(roof1, roof2) / (norm(roof1) * norm(roof2))

print("Cosine similarity:", cosine_sim)
