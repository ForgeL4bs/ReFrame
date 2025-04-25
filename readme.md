# ReFrame (**Video Frame Extractor**)

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?logo=python&logoColor=yellow)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green.svg?logo=opencv&logoColor=white)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python-based command-line tool to extract frames from video files (MP4, MKV, etc.) and save them as PNG or JPG images.  Handles videos of any length.

## Table of Contents

* [Features](#features)
* [Requirements](#requirements)
* [Installation](#installation)
* [Arguments](#arguments)
* [Usage](#usage)
* [Examples](#examples)

## Features

* **Frame Extraction:** Extracts frames from video files.
* **Format Support:** Supports outputting frames in both PNG and JPG formats.
* **FPS Control:** Allows you to specify the frames per second (FPS) for extraction.  If not specified, extracts all frames.
* **Command-Line Interface:** Easy-to-use command-line interface with clear arguments.
* **Efficiency:** Processes videos efficiently using OpenCV.
* **Cross-Platform:** Works on Linux, macOS, and Windows.

## Requirements

* **Python:** 3.7 or higher.
* **OpenCV:** 4.0 or higher (install with `pip install opencv-python`).

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/ForgeL4bs/ReFrame
    cd ReFrame
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Linux/macOS
    .venv\Scripts\activate  # On Windows
    ```

3.  **Install the requirements:**

    ```bash
    pip install opencv-python
    ```

## Arguments
* `video_path` (**Required**): The path to the video file you want to extract frames from.
* `output_dir` (**Required**): The directory where you want to save the extracted frames.  This directory will be created if it doesn't exist. 
* `-f, --format` (Optional): The format of the output frames. Can be either png or jpg. Default is png. 
* `-fps, --fps` (Optional): The number of frames per second to extract. If not specified, all frames will be extracted. (**Note: this is calculated based on the FPS of your input video so use it if you really want, for more clarity check out the code in extract_frames.py.**)

## Usage

```bash
python extract_frames.py <video_path> <output_dir> [-f <format>] [-fps <frames_per_second>]
```

## Examples
* Extract all frames from `test.mp4` to the `output_frames` directory as PNGs:
```bash
python extract_frames.py test.mp4 output_frames
```
* Extract frames from `video.mkv` to the `frames` directory as JPGs at 10 frames per second:
```bash
python extract_frames.py video.mkv frames -f jpg -fps 10
```
* Extract frames from `movie.mp4` to the `images` directory as PNGs at 1 frame per second:
```bash
python extract_frames.py movie.mp4 images -fps 1
```