# ImageElo: Interactive Image Sorting with Elo Rating

ImageElo is a powerful Python script designed to assist you in organizing your image folder interactively through the Elo rating system. With ImageElo, you can easily compare and sort your images by comparing them in pairs.

## ⚠️ Caution: Backup Your Files Before Running ⚠️

**Important:** Prior to executing this script on your actual image files, it is crucial to create a backup of your entire image folder. The script has the capability to rename files, which could potentially lead to data loss or other unintended issues.

## How to Use

Using ImageElo is straightforward. Follow these steps:

1. Place the Python script (or exe file) in the same folder as your image collection.
2. Open a terminal or command prompt and navigate to the directory where the script and images are located.
3. Run the script by either executing it without any arguments (in the same folder as the images) or by specifying the image folder as an attribute.

Feel free to manage your image files between sessions, but make sure not to delete the "gameElo.txt" file. Doing so will reset your progress, and all files will be renamed once the script is run again without that file.

The game's progress, represented by Elo values for each image, is stored in the "gameElo.txt" dictionary. The actual file names of the images are used solely for visual sorting purposes. If you decide to rename a file, it will not affect its Elo value. Instead, the image will be treated as unknown with an Elo of 1000 on the next run. If you want to add more images from another session or a different folder, you'll need to manually modify the values in "gameElo.txt" to merge them. Otherwise, new files will be considered fresh with an initial Elo of 1000.

Before applying ImageElo to your actual image collection, we strongly advise testing it on a small set of dummy files to ensure everything works as expected.

We warmly welcome contributions and issue reports to enhance the functionality and stability of ImageElo. Whether you have encountered problems or have suggestions for improvements, don't hesitate to create a pull request or open an issue. Happy image organizing! 📸
