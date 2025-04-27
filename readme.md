# ReFrame-CLI

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?logo=python&logoColor=yellow)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green.svg?logo=opencv&logoColor=white)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

ReFrame-CLI is a Python-based command-line tool to streamline your video and image manipulation tasks. Ideal for preparing image datasets for training machine learning models, including generative AI and diffusion models. Can handle videos of any length.

---

## Table of Contents

* [Features](#features)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
  - [Frame Extraction](#frame-extraction)
  - [Image Conversion](#image-conversion)
  - [GIF Creation](#gif-creation)
* [Examples](#examples)
* [Change History](#change-history)

---

## Features

* **Frame Extraction:** Extracts frames from video files.
* **Specify Timelines** Extracts frames withing a specified timeline.
* **FPS Control:** Allows you to specify the frames per second (FPS) for extraction.  If not specified, extracts all frames.
* **Convert Images**: Convert images between multiple formats such as PNG, JPG/JPEG, WEBP, HEIF/HEIC.
* **Bulk Support**: Convert images in bulk by just passing the input_path/dir rather than passing them one by one.
* **GIF Creation**: An additional feature to create Animated GIFs just by stacking up multiple frames(images).
* **Command-Line Interface:** Easy-to-use command-line interface with clear arguments.
* **Cross-Platform:** Works on Linux, macOS, and Windows.

---

## Requirements

* **Python:** 3.7 or higher.
* **Dependencies**:
  - OpenCV (`opencv-python`)
  - pillow
  - imageio
  - pillow-heif (for HEIC/HEIF support)

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

## Usage

**ReFrame-CLI provides three main functionalities: frame extraction, image conversion, and GIF creation. Use the reframe command to access these features.**

* ### Frame Extraction (Extract frames from a video file).
```bash
reframe extractf -input <video_path> -output <output_dir> [-f <format>] [-fps <frames_per_second>] [-start <start_time>] [-end <end_time>]
```

* ### Convert image format (Convert images between multiple formats)
```bash
reframe convert -input <input_path> -output <output_dir> -f <format>
```

* ### GIF Creation (Create animated gifs from images)
```bash
reframe gifc -input <input_dir> -output <output_path> [-d <duration>]
```

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

3. ### GIF Creation
* Create a GIF from images in the `frames` directory:
```bash
reframe gifc -input frames -output animation.gif
```
* Create a GIF with a custom frame duration (200ms per frame):
```bash
reframe gifc -input frames -output animation.gif -d 200
```

## Change History

### April 27, 2025

* Initial release of ReFrame-CLI.
* Added image conversion support for PNG, JPG, WEBP, HEIC, and HEIF formats.
* Added GIF creation functionality.
* Built and deployed to pypi

### April 26, 2025

* Added Support to specify a timeline from which you wanna extract frames. Works kind of like trimming the video(same same but different).