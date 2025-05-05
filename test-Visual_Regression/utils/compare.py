# utils/compare.py

import os
from PIL import Image, ImageChops
from config import DIFFS_DIR

def compare_images(baseline_path, current_path, diff_path):
    baseline = Image.open(baseline_path)
    current = Image.open(current_path)
    diff = ImageChops.difference(baseline, current)

    if diff.getbbox():
        os.makedirs(os.path.dirname(diff_path), exist_ok=True)
        diff.save(diff_path)
        return True  # Differences found
    return False  # No differences