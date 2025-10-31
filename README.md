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

```python
SETTINGS = {
    "IMAGE_DIMENSION" : {
        "height" : 150,
        "width" : 120,
    },
    "FOLDER_PATH" : r"C:\Users\myuser\Downloads\TO penebangan-20251028T071712Z-1-001\TO penebangan",
    "EXPORT_PATH" : r"C:\Users\myuser\Desktop\test.xlsx",
}
```

### OpenAI API Module
Use openai_api.py to extract coordinates from images in the FOLDER_PATH from settings.py.

```bash
python openai_api.py
```
this will export output.csv containing filename, coordinate1, coordinate2.

### Main Module
Use main.py to export workbook file (.xlsx) containing images from FOLDER_PATH and output.csv values. The workbook will be saved in EXPORT_PATH from settings.py.
```bash
python main.py
```

If you only need to export images to workbook, then add optional parameters.
```bash
python main.py --images_only
```
or
```bash
python main.py -i
```