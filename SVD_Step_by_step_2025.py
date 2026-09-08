# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 19:28:50 2025

@author: user
"""
#Step-1
import numpy as np

# Define a small 2x2 matrix
A = np.array([[4, 0],
              [3, -5]])
print("Original Matrix A:\n", A)
#Step 2: Apply SVD
U, S, VT = np.linalg.svd(A)
'''
This gives you:

U: Left singular vectors (2×2)

S: Singular values (only the diagonal, as a vector of length 2)
VT : Right singular vectors transposed (2×2)

'''
#step 3:Display the components
print("U (Left singular vectors):\n", U)
print("Singular values (Sigma):\n", S)
print("V^T (Right singular vectors):\n", VT)
# step 4:Convert S (1D array) into a diagonal matrix
Sigma = np.diag(S)
print("Sigma as a diagonal matrix:\n", Sigma)
#Step 5: Reconstruct A to check the decomposition
# Multiply U * Sigma * V^T to reconstruct A
A_reconstructed = U @ Sigma @ VT
print("Reconstructed A (U * Sigma * V^T):\n", A_reconstructed)
'''
Output (example values will look like):
    Original Matrix A:
[[ 4  0]
 [ 3 -5]]

U:
[[-0.447  -0.894]
 [-0.894   0.447]]

Sigma:
[[6.4, 0.0],
 [0.0, 3.2]]

V^T:
[[-0.625  0.781],
 [-0.781 -0.625]]

Reconstructed A:
[[ 4.  0.]
 [ 3. -5.]]

'''

import numpy as np

# Let's say we have 4 samples and 5 features
A = np.array([
    [2, 4, 1, 3, 5],
    [1, 3, 0, 4, 4],
    [2, 5, 1, 2, 6],
    [3, 6, 2, 3, 7]
])

print("Original Matrix A (4 samples x 5 features):\n", A)
#apply SVD
U, S, VT = np.linalg.svd(A, full_matrices=False)

print("\nSingular values:\n", S)
#Reduce dimensions (keep top 2)
# Keep top k = 2 singular values
k = 2

U_k = U[:, :k]              # shape (4, 2)
S_k = np.diag(S[:k])        # shape (2, 2)
VT_k = VT[:k, :]            # shape (2, 5)

#Step 4: Reconstruct matrix with reduced rank
A_approx = U_k @ S_k @ VT_k
print("\nReconstructed Matrix A (with k=2):\n", np.round(A_approx, 2))
#Compare sizes (optional)
original_size = A.size
original_size
reduced_size = U_k.size + S_k.size + VT_k.size
reduced_size

print(f"\nOriginal size: {original_size} values")
print(f"Reduced size (U_k + S_k + VT_k): {reduced_size} values")
'''
Original data: 4×5 = 20 values

SVD (rank-2): 

(4×2)+(2×2)+(2×5)=8+4+10=22 → slightly more 
due to decomposition overhead

But if data had 1000 rows and 5 features, 
and we only keep k=2, it would be a huge compression

'''




