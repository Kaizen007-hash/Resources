"""Classify the colors at five sample points in the supplied mat photograph."""

from pathlib import Path

import cv2
import numpy as np


POSITIONS = {
    "P1": (778, 350),
    "P2": (459, 492),
    "P3": (891, 481),
    "P4": (560, 651),
    "P5": (695, 529),
}
PATCH_RADIUS = 6


def classify_hsv(h: float, s: float, v: float) -> str:
    if s < 50 and v < 60:
        return "empty"
    if s < 60 or v < 60:
        return "unknown"
    if h <= 10 or h >= 170:
        return "red"
    if 20 <= h <= 34:
        return "yellow"
    if 35 <= h <= 85:
        return "green"
    if 90 <= h <= 130:
        return "blue"
    return "unknown"


def read_positions(image_path: Path) -> dict[str, str]:
    image = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(f"Cannot read mat photograph: {image_path}")

    height, width = image.shape[:2]
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    results: dict[str, str] = {}
    for position, (x, y) in POSITIONS.items():
        x0, x1 = max(0, x - PATCH_RADIUS), min(width, x + PATCH_RADIUS)
        y0, y1 = max(0, y - PATCH_RADIUS), min(height, y + PATCH_RADIUS)
        if x0 >= x1 or y0 >= y1 or not (0 <= x < width and 0 <= y < height):
            raise ValueError(
                f"Sample point {position} ({x}, {y}) is outside "
                f"the {width} x {height} image"
            )
        h, s, v = np.median(hsv[y0:y1, x0:x1], axis=(0, 1))
        results[position] = classify_hsv(float(h), float(s), float(v))
    return results


if __name__ == "__main__":
    image_path = Path(__file__).resolve().parents[1] / "assets" / "IMG_0794.jpg"
    for position, color in read_positions(image_path).items():
        print(f"{position}: {color}")
