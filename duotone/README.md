# Convert image to duotone
Converts images to the duotone filter as specified in the Ersilia Brand Guidelines. Colors in the filter are:
- dark: #50285a (plum)
- light: #bee64b (green, default)
- 
## Requirements
```
opencv-python
PIL
```

## Installation
Create a conda environment, install the necessary packages and clone this repository
```
conda create -n visuals
conda activate visuals
pip install opencv-python
pip install pillow
git clone https://github.com/ersilia-os/ersilia-figures.git
```

## Usage
The following command will convert the image to the default duotone (plum:green). Choose a different filter color from the list `["green", "yellow", "blue", "pink", "red", "purple", "gray"]` to create a different plum:color combination. If filter = None, all possible duotones will be generated.
```python
from convert_image import Converter
c  = Converter("filepath/filename.jpg")
c.main(filter="green")
```


