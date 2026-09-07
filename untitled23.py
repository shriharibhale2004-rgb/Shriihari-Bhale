# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:16:41 2026

@author: shrih
"""


# Faceplate transactions
transactions = [
    ['Red', 'White', 'Green'],          # T1
    ['White', 'Orange'],                # T2
    ['White', 'Blue'],                  # T3
    ['Red', 'White', 'Orange'],         # T4
    ['Red', 'Blue'],                    # T5
    ['White', 'Blue'],                  # T6
    ['White', 'Orange'],                # T7
    ['Red', 'White', 'Blue', 'Green'],  # T8
    ['Red', 'White', 'Blue'],           # T9
    ['Yellow']                          # T10
]

# -----------------------------------
# Step 1: Identify Transactions
# -----------------------------------

red_transactions = []
white_transactions = []
red_white_transactions = []

for i, t in enumerate(transactions, start=1):
    if 'Red' in t:
        red_transactions.append(f"T{i}")
    if 'White' in t:
        white_transactions.append(f"T{i}")
    if 'Red' in t and 'White' in t:
        red_white_transactions.append(f"T{i}")

# -----------------------------------
# Step 2: SUPPORT
# -----------------------------------
print("Step 1 — Support")

print("Transactions containing Red & White:", red_white_transactions,
      "→", len(red_white_transactions), "transactions")

print("Total transactions:", len(transactions))

support = len(red_white_transactions) / len(transactions)

print("Support =", len(red_white_transactions), "/", len(transactions),
      "=", round(support, 2))

# -----------------------------------
# Step 3: CONFIDENCE
# -----------------------------------
print("\nStep 2 — Confidence")

print("Transactions with Red:", red_transactions,
      "→", len(red_transactions), "transactions")

print("Transactions with Red & White:", red_white_transactions,
      "→", len(red_white_transactions), "transactions")

confidence = len(red_white_transactions) / len(red_transactions)

print("Confidence =", len(red_white_transactions), "/", len(red_transactions),
      "=", round(confidence, 2))

# -----------------------------------
# Step 4: LIFT
# -----------------------------------
print("\nStep 3 — Lift")

print("Support(White) =", len(white_transactions), "/", len(transactions))

support_white = len(white_transactions) / len(transactions)

print("Confidence (Red → White) =", round(confidence, 2))

lift = confidence / support_white

print("Lift =", round(confidence, 2), "/", round(support_white, 2),
      "=", round(lift, 2))
######################## Need for apriori ##########################
'''
If you have n items, possible rules are:

Rules of type: A → B

Total possible rules grow very fast (exponential)

'''
from itertools import combinations

# All unique items from your dataset
transactions = [
    ['Red', 'White', 'Green'],
    ['White', 'Orange'],
    ['White', 'Blue'],
    ['Red', 'White', 'Orange'],
    ['Red', 'Blue'],
    ['White', 'Blue'],
    ['White', 'Orange'],
    ['Red', 'White', 'Blue', 'Green'],
    ['Red', 'White', 'Blue'],
    ['Yellow']
]

# Get unique items
items = sorted(set(item for t in transactions for item in t))

print("Unique items:", items)

# -----------------------------------
# Generate ALL possible rules
# -----------------------------------
rules = []

for i in range(1, len(items)):
    for A in combinations(items, i):
        remaining = set(items) - set(A)
        
        for j in range(1, len(remaining) + 1):
            for B in combinations(remaining, j):
                rules.append((A, B))

# -----------------------------------
# Results
# -----------------------------------
print("\nTotal number of possible rules =", len(rules))

# Show first 10 rules
print("\nSample rules:")
for r in rules[:10]:
    print(f"{r[0]} → {r[1]}")
    
'''
| Items | Possible Rules |
| ----- | -------------- |
| 3     | 12             |
| 4     | 50             |
| 5     | 180            |
| 6     | 602            |
| 10    | 57,000+        |


“What if Amazon has 1000 products?”

Then say:

 “Rules ≈ billions → impossible without Apriori”
With Apriori:

✅ Prunes unnecessary combinations
✅ Uses “if subset not frequent → ignore supersets”
✅ Huge performance improvement

Why Apriori is Needed

Without Apriori:

❌ Check all 602 rules
❌ Compute support/confidence for each
❌ Very slow for large datasets
'''
###############After apriori algorithm#######################


from itertools import combinations

# -----------------------------------
# Step 0: Dataset
# -----------------------------------
transactions = [
    ['Red', 'White', 'Green'],
    ['White', 'Orange'],
    ['White', 'Blue'],
    ['Red', 'White', 'Orange'],
    ['Red', 'Blue'],
    ['White', 'Blue'],
    ['White', 'Orange'],
    ['Red', 'White', 'Blue', 'Green'],
    ['Red', 'White', 'Blue'],
    ['Yellow']
]

total = len(transactions)

# -----------------------------------
# Step 1: Unique Items
# -----------------------------------
items = sorted(set(item for t in transactions for item in t))

# -----------------------------------
# Step 2: Generate ALL possible rules
# -----------------------------------
all_rules = []

for i in range(1, len(items)):
    for A in combinations(items, i):
        remaining = set(items) - set(A)
        for j in range(1, len(remaining) + 1):
            for B in combinations(remaining, j):
                all_rules.append((A, B))

print("Total possible rules (Brute Force) =", len(all_rules))


# -----------------------------------
# Step 3: Function to calculate support
# -----------------------------------
def get_support(itemset):
    count = 0
    for t in transactions:
        if set(itemset).issubset(t):
            count += 1
    return count / total


# -----------------------------------
# Step 4: APRIORI (Filter by Support)
# -----------------------------------
min_support = 0.3   # you can change this

frequent_rules = []

for A, B in all_rules:
    support = get_support(list(A) + list(B))
    
    if support >= min_support:
        frequent_rules.append((A, B, support))

print("Rules after Support Pruning =", len(frequent_rules))


# -----------------------------------
# Step 5: Further Filter by Confidence
# -----------------------------------
def get_confidence(A, B):
    support_A = get_support(A)
    support_AB = get_support(list(A) + list(B))
    return support_AB / support_A if support_A != 0 else 0


min_confidence = 0.6

strong_rules = []

for A, B, support in frequent_rules:
    confidence = get_confidence(list(A), list(B))
    
    if confidence >= min_confidence:
        strong_rules.append((A, B, support, confidence))

print("Rules after Confidence Pruning =", len(strong_rules))






