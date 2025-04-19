# Repeating Pattern Extractor

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.9.0-green.svg)](https://opencv.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red.svg)](https://streamlit.io/)

A computer vision application that automatically extracts the smallest repeating unit from pattern images such as textiles, wallpapers, and decorative designs.

## 📖 About

The Repeating Pattern Extractor is an advanced computer vision tool designed to identify and extract the fundamental repeating units from patterned images. Built with OpenCV and Python, this project implements a novel algorithm using sliding window techniques to detect pattern repetition boundaries with remarkable accuracy.

**Key Insights:**

- Uses L2 loss (mean squared error) calculations to detect pattern boundaries
- Works efficiently on both simple and complex repeating patterns
- Supports color (RGB) and grayscale images with specialized processing pipelines
- Features a user-friendly web interface built with Streamlit for accessibility

This tool is particularly valuable for:

- **Textile Designers**: Analyzing and decomposing existing fabric patterns
- **Digital Artists**: Extracting core design elements from repeating works
- **Computer Vision Researchers**: Studying pattern recognition techniques
- **Design Students**: Learning about pattern composition and structure

The project originated from research into pattern analysis algorithms and has been optimized for performance across various pattern types, from simple geometric designs to complex natural patterns.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Algorithm](#algorithm)
- [Installation](#installation)
- [Usage](#usage)
  - [Web Application](#web-application)
  - [Command Line](#command-line)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Contributing](#contributing)

## 🔍 Overview

The Repeating Pattern Extractor is a tool that analyzes images with repeating patterns and identifies the foundational unit that creates the overall pattern. This is particularly useful for textile analysis, design extraction, and pattern recognition tasks.

## ✨ Features

- **Pattern Unit Extraction**: Identifies and extracts the smallest repeating unit in a pattern
- **Support for Both Color and Grayscale Images**: Works with different image types
- **User-friendly Web Interface**: Easy-to-use Streamlit application for uploading and processing images
- **Real-time Processing**: Provides immediate visual feedback
- **Flexible Input Handling**: Accepts various image formats (JPG, PNG, JPEG)

## 🎬 Demo

The tool provides a web interface where you can:

1. Upload your own pattern image
2. Try the included sample image
3. View the extracted pattern unit

## 🧠 Algorithm

The pattern extraction uses a sliding window approach with these key steps:

1. **Horizontal Sliding Analysis**:

   - The algorithm slides portions of the image from left to right
   - Calculates L2 loss (mean squared error) between overlapping regions
   - Identifies pattern boundaries where loss values cross a threshold

2. **Vertical Sliding Analysis**:

   - Similarly slides portions from top to bottom
   - Identifies vertical boundaries of the pattern unit

3. **Pattern Extraction**:
   - Combines horizontal and vertical analyses to determine the smallest repeating rectangle
   - Extracts this region as the pattern unit

The implementation includes specialized versions for both grayscale and color images.

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/LalitAI17/repeating-pattern-extractor.git
   cd repeating-pattern-extractor
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Web Application

1. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL displayed in the terminal (typically http://localhost:8501)

3. Upload an image or use the sample image, then click "Submit" to extract the pattern

### Command Line

For direct pattern extraction from Python scripts:

```python
from repeating_pattern_extractor_single_scale_image import find_repeating_pattern_unit

# For grayscale or auto-conversion to grayscale
find_repeating_pattern_unit("path/to/your/image.jpg")

# For color images
from repeating_pattern_extractor_three_scale_image import find_repeating_pattern_unit as find_color_pattern
find_color_pattern("path/to/your/image.jpg")
```

## 📁 Project Structure

```
repeating-pattern-extractor/
├── app.py                                      # Streamlit web application
├── repeating_pattern_extractor_single_scale_image.py  # Grayscale image processor
├── repeating_pattern_extractor_three_scale_image.py   # Color image processor
├── requirements.txt                            # Python dependencies
├── packages.txt                                # System dependencies
├── images/                                     # Sample images
│   └── sample_image.jpg                        # Example pattern image
└── README.md                                   # Project documentation
```

## 📋 Requirements

The key dependencies for this project are:

- OpenCV (4.9.0): Computer vision operations
- NumPy: Numerical computations
- Streamlit: Web interface
- Python 3.8+: Programming language

See `requirements.txt` for a complete list of dependencies.

## 🤝 Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

Please ensure your code follows the project's coding style and includes appropriate tests.

## 📝 Citations

If you use this software in your research, please cite:

```
@software{repeating_pattern_extractor,
  author = {Lalit Kumar},
  title = {Repeating Pattern Extractor},
  year = {2023},
  url = {https://github.com/LalitAI17/repeating-pattern-extractor}
}
```
