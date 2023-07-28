# ImageElo: Interactive Image Sorting with Elo Rating

ImageElo is a Python script that allows you to create an interactive game of Elo for organizing your image folder by comparing two images at a time.

## ⚠️ Caution: Backup Your Files Before Running ⚠️

**Important:** Before running this script on real image files, it is strongly recommended to create a backup of your image folder. The script has the potential to rename files and could inadvertently cause data loss or other issues.

## Known Issues

- Some image files may not work correctly with the script, including simple png files. As a temporary workaround, the script currently converts these problematic images to jpg format, which can significantly slow down the sorting process.
- The issues appear to be related to the PIL (Python Imaging Library) and/or QGraphicsView used by the script. Errors may occur when attempting to open certain images, even after conversion.

## How to Use

To use ImageElo, follow these steps:

1. Place the Python script in the same folder as your images.
2. Open a terminal or command prompt and navigate to the folder containing the script and images.
3. Run the script, either without any arguments (in the same folder as images) or by specifying the image folder as an attribute.

Please exercise caution when using this script, and it's always best to test it on a small set of dummy files before applying it to your actual image collection.

We welcome contributions and issue reports to improve the functionality and stability of ImageElo. Feel free to create a pull request or open an issue if you encounter any problems or have suggestions for enhancements. Happy image organizing! 📸
