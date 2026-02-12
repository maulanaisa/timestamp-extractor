# Getting started

This module is used to extract coordinates within timestamped images using openai API.

## Requirements

Install Python 3.14 or newer in your system.

## Dependencies

Clone this repository
```bash
git clone https://github.com/maulanaisa/timestamp-extractor.git
```

Open repository folder in your terminal, create virtual environment and activate it.
```bash
python -m venv myenv
myenv\Scripts\activate
```

Install requirements.txt using pip.
```bash
pip install -r requirements.txt
```

## Usage

Open settings.py file to configure parameters.

### OpenAI API Module
Use openai_api.py to extract coordinates from images. Use IMAGES_PATH to configure where the image folder is.

```bash
python openai_api.py
```
this will export output_open_ai.csv containing filename, latitude, longitude.

### Main Module
Use main.py to export workbook file (.xlsx) containing images from IMAGES_PATH which also listed in output_openai_api.csv. The workbook will be saved to EXPORT_PATH. This module also does location detection based on csv file located in LOCATION_COORDINATES.
```bash
python main.py
```