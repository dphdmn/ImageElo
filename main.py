import random
import json
import os
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QWidget, \
    QHBoxLayout
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt


def handle_wheel_event(view, event):
    # Get the current zoom factor
    zoom_factor = view.transform().m11()

    # Calculate the new zoom factor based on the scroll direction
    zoom_delta = 0.2
    if event.angleDelta().y() > 0:
        zoom_factor += zoom_delta
    else:
        zoom_factor -= zoom_delta

    # Limit the zoom factor within certain bounds to avoid excessive scaling
    zoom_factor = max(0.5, min(4.0, zoom_factor))

    # Set the new zoom factor
    view.setTransform(QTransform().scale(zoom_factor, zoom_factor))


class ImageViewer(QMainWindow):
    def __init__(self, folder, file1, file2):
        super().__init__()

        self.folder = folder
        self.file1 = file1
        self.file2 = file2
        self.chosen_file = None

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)

        # Create graphics view for image1
        self.view1 = QGraphicsView(self)
        layout.addWidget(self.view1)

        # Create graphics view for image2
        self.view2 = QGraphicsView(self)
        layout.addWidget(self.view2)

        # Load images
        image1 = QPixmap(os.path.join(self.folder, self.file1))
        image2 = QPixmap(os.path.join(self.folder, self.file2))

        # Create graphics scenes for images
        self.scene1 = QGraphicsScene(self)
        self.scene2 = QGraphicsScene(self)

        # Add images to graphics scenes
        self.pixmap_item1 = QGraphicsPixmapItem(image1)
        self.pixmap_item2 = QGraphicsPixmapItem(image2)
        self.scene1.addItem(self.pixmap_item1)
        self.scene2.addItem(self.pixmap_item2)

        # Set scenes for graphics views
        self.view1.setScene(self.scene1)
        self.view2.setScene(self.scene2)

        # Set up zooming
        self.view1.setDragMode(QGraphicsView.ScrollHandDrag)

        self.view2.setDragMode(QGraphicsView.ScrollHandDrag)

        self.view1.keyPressEvent = self.keyPressEvent
        self.view2.keyPressEvent = self.keyPressEvent

        self.showFullScreen()
        # Enable zooming using the mouse wheel for view1 and view2
        self.view1.setInteractive(True)
        self.view2.setInteractive(True)
        self.view1.wheelEvent = lambda event: handle_wheel_event(self.view1, event)
        self.view2.wheelEvent = lambda event: handle_wheel_event(self.view2, event)

        # Calculate the initial zoom factor to fit the whole image in the view
        self.view1.fitInView(self.pixmap_item1, Qt.KeepAspectRatio)
        self.view2.fitInView(self.pixmap_item2, Qt.KeepAspectRatio)

        # Enable zooming using the mouse wheel for view1 and view2
        self.view1.setInteractive(True)
        self.view2.setInteractive(True)
        self.view1.wheelEvent = lambda event: handle_wheel_event(self.view1, event)
        self.view2.wheelEvent = lambda event: handle_wheel_event(self.view2, event)

        # Calculate the size for each QGraphicsView
        screen_resolution = QApplication.desktop().screenGeometry()
        view_width = screen_resolution.width() // 2
        view_height = screen_resolution.height()

        # Set the size for view1 and view2
        self.view1.setFixedSize(view_width, view_height)
        self.view2.setFixedSize(view_width, view_height)

        # Calculate the initial zoom factor to fit the whole image in the view
        self.view1.fitInView(self.pixmap_item1, Qt.KeepAspectRatio)
        self.view2.fitInView(self.pixmap_item2, Qt.KeepAspectRatio)

        # Enable zooming using the mouse wheel for view1 and view2
        self.view1.setInteractive(True)
        self.view2.setInteractive(True)
        self.view1.wheelEvent = lambda event: handle_wheel_event(self.view1, event)
        self.view2.wheelEvent = lambda event: handle_wheel_event(self.view2, event)

        self.showFullScreen()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.chosen_file = self.file1
            self.close()
        elif event.key() == Qt.Key_Right:
            self.chosen_file = self.file2
            self.close()
        elif event.key() == Qt.Key_Escape:
            self.close()


def display_and_choose_files(folder, file1, file2):
    app = QApplication(sys.argv)
    viewer = ImageViewer(folder, file1, file2)
    app.exec_()
    return viewer.chosen_file


def save_dict_to_file(dictionary, filename):
    with open(filename, 'w') as file:
        json.dump(dictionary, file)


def load_dict_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def simulate_battle(elo_dict, folder):
    """
    Simulates a battle between two random filenames with close Elo values and updates their Elo ratings.

    Parameters:
        elo_dict (dict): A dictionary containing filenames as keys and their corresponding Elo ratings as values.

    Returns:
        dict: The updated dictionary with Elo ratings after the simulated battle.
    """
    # Sort the filenames based on their Elo values
    sorted_filenames = sorted(elo_dict.keys(), key=lambda x: elo_dict[x])

    # Find two filenames with close Elo values
    index = random.randint(0, len(sorted_filenames) - 2)
    filename1, filename2 = sorted_filenames[index], sorted_filenames[index + 1]

    winner = display_and_choose_files(folder, filename1, filename2)
    if winner == filename1:
        loser = filename2
    elif winner == filename2:
        loser = filename1
    else:
        return False, elo_dict  # no winner

    # Update Elo ratings based on the result
    k = 32  # Elo update constant (you can adjust this as per your preference)
    elo1, elo2 = elo_dict[filename1], elo_dict[filename2]
    expected_win_prob_winner = 1 / (1 + 10 ** ((elo2 - elo1) / 400))
    expected_win_prob_loser = 1 / (1 + 10 ** ((elo1 - elo2) / 400))

    updated_elo_winner = elo1 + k * (1 - expected_win_prob_winner)
    updated_elo_loser = elo2 + k * (0 - expected_win_prob_loser)

    # Update the Elo ratings in the dictionary
    elo_dict[winner] = updated_elo_winner
    elo_dict[loser] = updated_elo_loser

    return True, elo_dict


def initialize_elo_system(filenames, initial_elo=1000):
    """
    Initializes the Elo system for a list of filenames.

    Parameters:
        filenames (list): A list of filenames to be ranked.
        initial_elo (int, optional): The initial Elo rating for all filenames. Default is 1000.

    Returns:
        dict: A dictionary containing filenames as keys and their corresponding Elo ratings as values.
    """
    elo_dict = {filename: initial_elo for filename in filenames}
    return elo_dict


def generate_unique_id(folderPath, value, extension, latestId):
    value_str = str(int(value))
    id_counter = latestId+1
    while True:
        new_filename = f"{value_str}_ID{id_counter}.{extension}"
        new_filepath = os.path.join(folderPath, new_filename)
        if not os.path.exists(new_filepath):
            return id_counter, new_filename
        id_counter += 1


def rename_files_and_update_dict(folderPath, file_dict):
    updated_dict = {}
    latestid = 0
    for filename, value in file_dict.items():
        _, extension = os.path.splitext(filename)
        latestid, new_filename = generate_unique_id(folderPath, value, extension[1:], latestid)
        old_filepath = os.path.join(folderPath, filename)
        new_filepath = os.path.join(folderPath, new_filename)

        os.rename(old_filepath, new_filepath)
        updated_dict[new_filename] = value

    return updated_dict


def doGame(folder, elo_dict, eloFile):
    winner = True
    while (winner):
        winner, elo_dict = simulate_battle(elo_dict, folder)
    elo_dict = rename_files_and_update_dict(folder, elo_dict)
    save_dict_to_file(elo_dict, eloFile)


def loadGame(folder):
    eloFile = os.path.join(folder, "gameElo.txt")
    elo_dict = load_dict_from_file(eloFile)
    doGame(folder, elo_dict, eloFile)


def startGame(folder, gamefile):
    filenames = []
    eloFile = os.path.join(folder, "gameElo.txt")
    with open(gamefile, 'r') as file:
        for line in file:
            filenames.append(line.strip())
    elo_dict = initialize_elo_system(filenames)
    doGame(folder, elo_dict, eloFile)


def writeInFile(filepath, folder_name):
    image_files = find_image_files(folder_name)

    if image_files:
        with open(filepath, 'w', encoding='utf-8') as file:
            for image_path in image_files:
                file.write(f"{os.path.basename(image_path)}\n")
        print(f"Image paths written to '{filepath}' successfully.")
    else:
        print("No image files found in the specified folder.")


def initNewGame(folder_path, gamefile_path):
    writeInFile(gamefile_path, folder_path)


def create_file_if_not_exists(folder_path):
    file_path = os.path.join(folder_path, "game.txt")
    if not os.path.exists(file_path):
        print(f"File '{file_path}' created successfully.")
        initNewGame(folder_path, file_path)
        startGame(folder_path, file_path)
    else:
        loadGame(folder_path)
        print(f"File '{file_path}' already exists.")
        # TODO - analyze game file and add new images

def is_image_file(filename):
    # Check if the file has an image extension (you can add more extensions if needed)
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp']
    return any(filename.lower().endswith(ext) for ext in image_extensions)


def find_image_files(folder_path):
    image_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if is_image_file(file):
                file_path = os.path.join(root, file)
                image_files.append(file_path)
    return image_files


def main():
    import sys
    if len(sys.argv) != 2:
        folder_name = os.getcwd()
    else:
        folder_name = sys.argv[1]
    if not os.path.exists(folder_name):
        print(f"Error: Folder '{folder_name}' does not exist.")
        return

    create_file_if_not_exists(folder_name)

if __name__ == "__main__":
    main()
