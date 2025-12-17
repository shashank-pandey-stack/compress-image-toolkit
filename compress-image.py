#!/usr/bin/env python3
"""
Image compression script with quality and size control.
"""

import sys
from PIL import Image
import os

def compress_image(input_path, output_path=None, quality=85, max_width=None, max_height=None):
    """
    Compress an image with quality and size options.
    
    Args:
        input_path: Path to input image
        output_path: Path to save compressed image (optional)
        quality: JPEG quality 1-100 (default: 85)
        max_width: Maximum width in pixels (optional)
        max_height: Maximum height in pixels (optional)
    """
    try:
        with Image.open(input_path) as img:
            # Get original size
            original_size = os.path.getsize(input_path)
            original_width, original_height = img.size
            
            # Resize if max dimensions specified
            if max_width or max_height:
                img.thumbnail((max_width or original_width, max_height or original_height), Image.Resampling.LANCZOS)
            
            # Convert RGBA to RGB for JPEG
            if img.mode in ('RGBA', 'LA'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[-1] if 'A' in img.mode else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Generate output path if not provided
            if not output_path:
                base, ext = os.path.splitext(input_path)
                output_path = f"{base}_compressed.jpg"
            
            # Save with compression
            img.save(output_path, 'JPEG', quality=quality, optimize=True)
            
            # Show results
            compressed_size = os.path.getsize(output_path)
            reduction = ((original_size - compressed_size) / original_size) * 100
            
            print(f"✓ Original: {original_width}x{original_height} ({original_size/1024:.1f} KB)")
            print(f"✓ Compressed: {img.size[0]}x{img.size[1]} ({compressed_size/1024:.1f} KB)")
            print(f"✓ Reduced by: {reduction:.1f}%")
            print(f"✓ Saved to: {output_path}")
            
            return True
            
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python compress_image.py <input> [options]")
        print("\nOptions:")
        print("  -o, --output <path>     Output file path")
        print("  -q, --quality <1-100>   JPEG quality (default: 85)")
        print("  -w, --width <pixels>    Maximum width")
        print("  -h, --height <pixels>   Maximum height")
        print("\nExamples:")
        print("  python compress_image.py photo.jpg")
        print("  python compress_image.py photo.jpg -q 70")
        print("  python compress_image.py photo.jpg -w 1920 -h 1080")
        print("  python compress_image.py photo.jpg -o small.jpg -q 60 -w 800")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = None
    quality = 85
    max_width = None
    max_height = None
    
    # Parse arguments
    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg in ('-o', '--output') and i + 1 < len(sys.argv):
            output_path = sys.argv[i + 1]
            i += 2
        elif arg in ('-q', '--quality') and i + 1 < len(sys.argv):
            quality = int(sys.argv[i + 1])
            i += 2
        elif arg in ('-w', '--width') and i + 1 < len(sys.argv):
            max_width = int(sys.argv[i + 1])
            i += 2
        elif arg in ('-h', '--height') and i + 1 < len(sys.argv):
            max_height = int(sys.argv[i + 1])
            i += 2
        else:
            i += 1
    
    compress_image(input_path, output_path, quality, max_width, max_height)

if __name__ == "__main__":
    main()