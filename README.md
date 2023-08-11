# ImageElo: Organize Your Images with Elo Rating

ImageElo is an interactive Python script that helps you sort and organize your image collection using the Elo rating system. Easily compare images in pairs and let ImageElo do the rest!

## ⚠️ Caution: Backup Your Files Before Running ⚠️

**Before you begin:** Create a backup of your entire image folder. ImageElo can rename files, so it's better to be safe and avoid any data loss or issues.

## How to Use

1. **Setup**:
   - Place the Python script (or exe file) in the same folder as your image collection.

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the folder where the script and images are located.

3. **Execute the Script**:
   - Run the script without any arguments if it's in the same folder as your images.
   - Alternatively, specify the image folder as an attribute if the script is located elsewhere.
   - Easy way I personally like to run the script - having ImageElo.exe in one of my PATH folders, and then simply typing "ImageElo" into address bar of the image folder.

4. **Sorting Fun**:
   - ImageElo presents image pairs for comparison. Choose which one you prefer or find more appealing.
   - Use the Left Arrow key to choose the image on the left.
   - Use the Right Arrow key to select the image on the right.
   - Pan/zoom images using the scroll wheel and left mouse button.
   - Press the Esc key to exit.

5. **Flexible Management**:
   - Add or delete image files between sessions to keep your collection up to date.
   - New images receive a default Elo value of 1000, no matter their names.

6. **Important Progress Note**:
   - Do not delete "gameElo.txt" to preserve your progress.
   - When you run the script again, it picks up from where you left off, considering new and deleted files.

7. **Understanding Elo Rating**:
   - Elo values are stored in "gameElo.txt" for each image.
   - Image filenames are for visual sorting only and don't affect Elo ratings.
   - Renaming an image won't change its Elo value, it will be treated as new on the next run.

8. **Merging Elo Folders**:
   - To merge images from different folders while retaining their Elo values:
     - Manually modify "gameElo.txt" with the new image data.
     - All other files, not specified in "gameElo.txt", will start with a default Elo of 1000.

Before running ImageElo on your precious image collection, test it on a small set of dummy files to familiarize yourself with the process.

We welcome contributions and issue reports to enhance ImageElo's functionality and stability. If you encounter any problems or have exciting ideas for improvements, feel free to create a pull request or open an issue. Happy image organizing! 📸
