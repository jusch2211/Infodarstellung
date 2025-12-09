#!/usr/bin/env python3
import sys
from PIL import Image

def rgb_to_bits(value):
    """Convert an integer (0–255) to an 8-bit binary string."""
    return format(value, "08b")

def print_image_as_bitpatterns(image_path):
    # Bild laden
    img = Image.open(image_path).convert("RGB")
    width, height = img.size

    print(f"Bild: {image_path}")
    print(f"Auflösung: {width} × {height}\n")

    print("Limit: 50x50 Pixel für die Ausgabe\n")
    width,height = min(width,50), min(height,50)

    # Pixel für Pixel auslesen
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            r_bits = rgb_to_bits(r)
            g_bits = rgb_to_bits(g)
            b_bits = rgb_to_bits(b)

            print(f"({x},{y})  R:{r_bits}  G:{g_bits}  B:{b_bits}")
        print()  # Leerzeile zwischen Zeilen

def main():
    if len(sys.argv) != 2:
        print("Usage: python pixelbits.py <image.png>")
        sys.exit(1)

    image_path = sys.argv[1]
    print_image_as_bitpatterns(image_path)

if __name__ == "__main__":
    main()
