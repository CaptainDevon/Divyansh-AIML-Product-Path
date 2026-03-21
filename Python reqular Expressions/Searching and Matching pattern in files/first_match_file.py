import os
import re

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "Assets", "sample1.txt")

with open(file_path, "r") as f:
    for line in f:
        match = re.search("sample", line)

        if match:
            print("match found in line:", line)
            break