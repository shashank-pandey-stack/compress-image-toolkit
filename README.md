# Image Compressor

Compress images with adjustable quality and size options.

## Installation

```bash
pip install Pillow
```

## Usage

```bash
# Basic compression (85% quality, auto-named output)
python compress_image.py photo.jpg

# Set quality (1-100, lower = smaller file)
python compress_image.py photo.jpg -q 70

# Resize while compressing
python compress_image.py photo.jpg -w 1920 -h 1080

# Custom output filename
python compress_image.py photo.jpg -o compressed.jpg

# Combine all options
python compress_image.py photo.jpg -o small.jpg -q 60 -w 800 -h 600
```

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `-o, --output` | Output file path | `{input}_compressed.jpg` |
| `-q, --quality` | JPEG quality (1-100) | 85 |
| `-w, --width` | Maximum width (pixels) | Original |
| `-h, --height` | Maximum height (pixels) | Original |

## Features

- Compresses to optimized JPEG format
- Preserves aspect ratio when resizing
- Shows original/compressed sizes and reduction %
- Handles PNG, JPEG, WebP, and other formats

## Output

```
✓ Original: 4032x3024 (3847.2 KB)
✓ Compressed: 1920x1440 (421.8 KB)
✓ Reduced by: 89.0%
✓ Saved to: photo_compressed.jpg
```

## Requirements

- Python 3.6+
- Pillow library