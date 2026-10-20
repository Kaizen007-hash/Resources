"""Print HSV medians and classifications to help debug mat color thresholds."""

from pathlib import Path

import cv2
import numpy as np

from mat_reader import PATCH_RADIUS, POSITIONS, classify_hsv


def main() -> None:
    image_path = Path(__file__).resolve().parents[1] / "assets" / "IMG_0794.jpg"
    image = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(f"Cannot read mat photograph: {image_path}")
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    for position, (x, y) in POSITIONS.items():
        patch = hsv[
            max(0, y - PATCH_RADIUS): y + PATCH_RADIUS,
            max(0, x - PATCH_RADIUS): x + PATCH_RADIUS,
        ]
        if patch.size == 0:
            raise ValueError(f"Sample point {position} ({x}, {y}) is outside the image")
        h, s, v = np.median(patch, axis=(0, 1))
        color = classify_hsv(float(h), float(s), float(v))
        print(f"{position}: HSV=({h:.1f}, {s:.1f}, {v:.1f}) -> {color}")


if __name__ == "__main__":
    main()
