# ImageElo: Interactive Image Sorting with Elo Rating

ImageElo is a powerful Python script designed to assist you in organizing your image folder interactively through the Elo rating system. With ImageElo, you can easily compare and sort your images by comparing them in pairs.

## ⚠️ Caution: Backup Your Files Before Running ⚠️

**Important:** Prior to executing this script on your actual image files, it is crucial to create a backup of your entire image folder. The script has the capability to rename files, which could potentially lead to data loss or other unintended issues.

## How to Use

Using ImageElo is straightforward. Follow these steps:

1. **Setup**:
   - Place the Python script (or exe file) in the same folder as your image collection.

2. **Navigation**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script and images are located.

3. **Running the Script**:
   - Execute the script by either:
     - Running it without any arguments (if the script is in the same folder as the images).
     - Specifying the image folder as an attribute (if the script is located elsewhere).

4. **Managing Image Files**:
   - You have the flexibility to add or delete image files between different sessions.
   - New images get default 1000 elo values regardless of their name (elo is not parsed from the image file)

5. **Important Note**:
   - Avoid deleting the "gameElo.txt" file, as doing so will reset your progress.
   - When the script is run again without "gameElo.txt," all files will be renamed and get default 1000 elo value.

6. **Understanding Game Progress**:
   - The game's progress is determined by Elo values assigned to each image, stored in the "gameElo.txt" dictionary.
   - The file names of the images are purely for visual sorting purposes and have no impact on Elo values.
   - Renaming a file will not affect its Elo value; instead, it will be treated as an unknown image with an initial Elo of 1000 on the next run.

7. **Merging different elo folders**:
   - Merging is not natively supported for now, so it's best to locate all images in one folder before using the script.
   - If you wish to include additional images from another session or a different folder, and keep their elo values, manually modify the values in "gameElo.txt" to merge them.
   - Otherwise, new files will be considered fresh with an initial Elo of 1000. 

Before applying ImageElo to your actual image collection, we strongly advise testing it on a small set of dummy files to ensure everything works as expected.

Remember that we welcome contributions and issue reports to enhance the functionality and stability of ImageElo. Whether you encounter problems or have suggestions for improvements, feel free to create a pull request or open an issue. Happy image organizing! 📸
