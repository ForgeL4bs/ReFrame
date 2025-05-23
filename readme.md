<p align=”center”>

<img src="https://raw.githubusercontent.com/ForgeL4bs/ReFrame/main/assets/Frame%202.png" alt="my banner">

</p>

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?logo=python&logoColor=yellow)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green.svg?logo=opencv&logoColor=white)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

ReFrame-CLI is a Python-based command-line `ImageToolKit` to streamline your image manipulation tasks. Ideal for preparing image datasets for training machine learning models, including generative AI and diffusion models. Can handle videos of any length.

Reframe is still in development and we know it needs a lot of improvements, So communities contributions are really appreciated🙇.

---

## Table of Contents

* [Features](#features)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Arguments](#arguments)
  - Frame Extraction
  - Image Conversion
  - Resize Image
  - Background Remover
  - GIF Creation
* [Examples](#examples)
* [Change History](#change-history)

---

## Features

* **Frame Extraction:** Extracts frames from video files.
* **Convert Images**: Convert images between multiple formats such as PNG, JPG/JPEG, WEBP, HEIF/HEIC.
* **Resize Images**: Resize images to desired size/ratio or use the multiplier to just upscale the size of the image.
* **Background Remover**: Remove background from an image and optionally replace it with a specified color.
* **Bulk Support**: Convert/Resize images in bulk by just passing the input_path/dir rather than passing them one by one.
* **GIF Creation**: An additional feature to create Animated GIFs just by stacking up multiple frames(images).
* **Cross-Platform:** Works on Linux, macOS, and Windows.

---

## Requirements

* **Python:** 3.7 or higher.
* **Dependencies**:
  - Check out requirements.txt

---

## Installation

### Install via pip(Recommended):
**By far the easiest way to install and use reframe-cli**
```bash
pip install reframe-cli
```

### Install from the source(github repo)

1.  **Clone the repository**
```bash
git clone https://github.com/ForgeL4bs/ReFrame
cd ReFrame
```

2.  **Create a virtual environment(recommended)**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Linux/macOS
.venv\Scripts\activate  # On Windows
```

3.  **Install the package in editable mode**
```bash
pip install -e .
```

---

## Arguments
**In General(Required for all the features)**

* `-input`: Input path to any directory or file from where you want to access the files
* `-output`: Output path to save the output

**Frame Extraction(Optionals)**

* `-f`: To specify the output format(Default = png)
* `-fps`: To specify the frames_per_second to extract, if not specified then all the frames will be extracted
* `-start`:The time (in seconds) from where you want to start the extraction
* `-end`: The time (in seconds) till where you want to extract

**Image Conversion(Required)**

* `-f`: sets the output format (e.g., 'png', 'jpg', 'jpeg', 'webp', 'heic')

**Resize Image(Required)**

* `-wh`: The width of the resized image
* `-ht`: The height of the resized image
* `-ratio`:The desired aspect ratio (e.g., 1:1, 3:4).
* Note: If you use `-wh` and `-ht` then you don't need to specify `-ratio` and vise versa, since both are for specifying dimension only(just use any one between) and yeah it goes same for `-multi` multiplier, cause it just multiplies your height width by the number you have specified, or you can say upscaled dimensions by `-multi`.

**Resize Image(Optionals)**

* `-f`: Is to specify format of the output image [choices are: png, jpg], if you need any other format, you can just convert it using the `convert` feature.
* `-fp`: The focal point for resizing ('left', 'right', 'top', 'bottom', 'center', 'auto'). Defaults to 'auto', which behaves like 'center'.
* `-multi`: The resizing multiplier (e.g., 2 for 2x). Overrides width, height, and ratio.

**Background Remover(Optionals)**

* `-color`: RGB color to replace the background. If None, the background will be transparent.

**GIF Creation(Optional)**

* `-d`: sets the duration of each frame in the GIF in milliseconds (default: 100ms)
* Note: In case of GIF `-output` you would need to specify the output path along with the `.gif` extension for the output file `for ex: home/gour4v/output/test.gif`

---

## Usage

**ReFrame-CLI provides three main functionalities: frame extraction, image conversion, and GIF creation. Use the reframe command to access these features.**

* ### Frame Extraction
**(Extract frames from a video file)**
```bash
reframe extractf -input <video_path> -output <output_dir> [-f <format>] [-fps <frames_per_second>] [-start <start_time>] [-end <end_time>]
```

* ### Convert image format
**(Convert images between multiple formats)**
```bash
reframe convert -input <input_path> -output <output_dir> -f <format>
```

* ### Resize Image
```bash
reframe resize -input <input_path> -output <output_dir> [-wh <width>] [-ht <height>] [-ratio <aspect_ratio>] [-multi <multiplier>] [-f <format>] [-fp <focal_point>]
```

* ### Background Remover
```bash
reframe bgremove -input <input_path> -output <output_dir> -color 255,255,255(for white)
```

* ### GIF Creation
**(Create animated gifs from images)**
```bash
reframe gifc -input <input_dir> -output <output_path> [-d <duration>]
```

---

## Examples
1. ### Frame Extraction
* Extract all frames from `test.mp4` to the `output_frames` directory as PNGs:
```bash
reframe extractf -input test.mp4 -output output_frames
```
* Extract frames from `video.mkv` to the `frames` directory as JPGs at 10 frames per second:
```bash
reframe extractf -input video.mkv -output frames -f jpg -fps 10
```
* Extract frames within a time range:
```bash
reframe extractf -input video.mp4 -output output_frames -start 10 -end 25
```

2. ### Image Conversion
* Convert all images in `input_images` to PNG format and save them in `converted_images`:
```bash
reframe convert -input input_images -output converted_images -f png
```
* Convert a single HEIC image to JPG:
```bash
reframe convert -input image.heic -output converted_images -f jpg
```

3. ### Resize Images

* Resize all images in the `input_images` directory to 800x600 and save them in the `resized_images` directory:
```bash
reframe resize -input input_images -output resized_images -wh 800 -ht 600
```
* Resize all images in the `input_images` directory to a `3:4` aspect ratio along with `focal_point` left and save them in the `resized_images` directory:
```bash
reframe resize -input input_images -output resized_images -ratio 3:4 -fp left
```

4. ### Background Remover

* Remove Background for a Directory
```bash
reframe bgremove -input ./images -output ./bg_removed
```

* Remove Background and Replace with a slight reddish color
```bash
reframe bgremove -input ./images -output ./bg_removed -color 199,74,74
```

5. ### GIF Creation
* Create a GIF from images in the `frames` directory:
```bash
reframe gifc -input frames -output animation.gif
```
* Create a GIF with a custom frame duration (200ms per frame):
```bash
reframe gifc -input frames -output animation.gif -d 200
```

---

## Change History

### April 30, 2025

* Release: v1.2.0
* Newly added feature: **Background Remover**
* Using `rembg` and `onnxruntime` to remove the background from an image.

### April 29, 2025

* Release: v1.1.1
* Added a better progress bar using tqdm
* Removed PIL from image_resizer.py

### April 29, 2025

* Latest release of ReFrame-CLI-1.1.0 on [pypi](https://pypi.org/project/reframe-cli/)
* Added a new feature ~ **Image Resizer**.
* Fixed some bugs inside Image converter.

### April 27, 2025

* Initial release of ReFrame-CLI.
* Added image conversion support for PNG, JPG, WEBP, HEIC, and HEIF formats.
* Added GIF creation functionality.
* Built and deployed to [pypi](https://pypi.org/project/reframe-cli/)

### April 26, 2025

* Added Support to specify a timeline from which you wanna extract frames. Works kind of like trimming the video(same same but different).