# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]

# Convert the list shelf1_update of new items to a tuple called shelf1_update_tuple.
shelf1_update_tuple = tuple(shelf1_update)

# Concatenate shelf1_update_tuple with the existing tuple shelf1 to create a new tuple shelf1_concat.
shelf1_concat = shelf1 + shelf1_update_tuple

# Count how many times "celery" appears in shelf1_concat and store the result in celery_count.
celery_count = shelf1_concat.count("celery")

# Find the index of the first occurrence of "celery" in shelf1_concat and store it in celery_index.
celery_index = shelf1_concat.index("celery")

# Output Requirements

# Print the updated shelf contents: "Updated Shelf #1: <$shelf1_concat>".
print("Updated Shelf #1: ", shelf1_concat)

# Print the count of "celery": "Number of Celery: <$celery_count>".
print("Number of Celery: ", celery_count)

# Print the index of the first occurrence of "celery": "Celery Index: <$celery_index>".
print("Celery Index: ", celery_index)
