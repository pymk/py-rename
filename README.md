# pyrename

A simple CLI tool for renaming images to their SHA-1 checksum.

## Features

- Rename image files with extensions: `.jpeg`, `.jpg`, `.png`
- Outputs the original and new file names.

## Usage

```sh
poetry run python pyrename/main.py /path/to/your/image/directory
```

Running unit test:

```sh
cd tests
poetry run python -m unittest discover 
```

## Example

```
> poetry run python pyrename/main.py ~/Pictures/Wallpapers

test_1.jpg -> 4c2ad46d9b4f5d1d6ec0eb7fe3ccca4d32675194.jpg
test_2.png -> df7c46935c4a070dc349777b36fdadb3064c4f3c.png
```
