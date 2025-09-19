### **mod\_switcher.py**

import os
import shutil
import sys
import configparser
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, 
                             QListWidget, QLabel, QMessageBox, QLineEdit, QHBoxLayout, QFileDialog, QFrame)
from PyQt6.QtCore import Qt

class ModSwitcherApp(QWidget):
    """
    A PyQt6-based GUI application for managing and switching game mods.

    This tool auto-detects or allows the user to manually select a game directory,
    lists available mod folders, and provides a one-click solution to switch mods
    by copying files to the game's root. It also remembers the last used path.
    """
    def __init__(self):
        """
        Initializes the application window and sets up key properties.
        """
        super().__init__()
        # Root directory of the game, dynamically set by user selection or auto-detection.
        self.root_dir = ""
        # Path to the file that tracks the currently active mod.
        self.active_mod_file = ""
        # List of folders to ignore when scanning for mods (e.g., raw game files).
        self.ignore_folders = ["raw"]
        # Name of the configuration file to save/load the game path.
        self.config_file = "config.ini"
        
        self.init_ui()
        # Attempt to load a previously saved path or auto-detect on startup.
        self.load_saved_path()

    def init_ui(self):
        """
        Sets up the graphical user interface elements and their layout.
        """
        self.setWindowTitle("Game Mod Switcher")
        self.setFixedSize(500, 450)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Path selection section, using a horizontal layout for UI consistency.
        path_layout = QHBoxLayout()
        self.path_input = QLineEdit()
        self.path_input.setPlaceholderText("Select your game directory...")
        self.path_input.setReadOnly(True)
        path_layout.addWidget(self.path_input)

        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.select_directory)
        path_layout.addWidget(browse_button)

        self.auto_detect_button = QPushButton("Auto-Detect")
        self.auto_detect_button.clicked.connect(self.auto_detect_path)
        path_layout.addWidget(self.auto_detect_button)

        main_layout.addLayout(path_layout)
        
        # A horizontal line to visually separate the path section.
        separator1 = QFrame()
        separator1.setFrameShape(QFrame.Shape.HLine)
        separator1.setFrameShadow(QFrame.Shadow.Sunken)
        main_layout.addWidget(separator1)

        # Labels to provide feedback to the user.
        self.current_mod_label = QLabel("Please select a valid game directory.")
        self.current_mod_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #cc5500;")
        main_layout.addWidget(self.current_mod_label, alignment=Qt.AlignmentFlag.AlignCenter)

        mod_list_label = QLabel("Select a mod to switch to:")
        main_layout.addWidget(mod_list_label)

        # List widget to display detected mod folders.
        self.mod_list_widget = QListWidget()
        self.mod_list_widget.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        main_layout.addWidget(self.mod_list_widget)

        # The main action button for switching mods.
        self.switch_button = QPushButton("Switch Mod")
        self.switch_button.setStyleSheet("background-color: #2e8b57; color: white; font-weight: bold;")
        self.switch_button.clicked.connect(self.switch_mod)
        self.switch_button.setEnabled(False) # Disabled by default until a valid path is set.
        main_layout.addWidget(self.switch_button)

    def load_saved_path(self):
        """
        Loads a saved path from the config file on application startup.
        If no saved path is found or the path is invalid, it attempts to auto-detect.
        """
        config = configparser.ConfigParser()
        config.read(self.config_file)
        if 'Paths' in config and 'game_dir' in config['Paths']:
            saved_path = config['Paths']['game_dir']
            if os.path.exists(saved_path):
                self.set_game_directory(saved_path)
                # Disable the auto-detect button as a valid path has been found.
                self.auto_detect_button.setEnabled(False) 
                return

        # If no saved path, try to auto-detect the game directory.
        self.auto_detect_path()

    def save_path(self, path):
        """
        Saves the successfully validated game path to a configuration file.

        :param path: The absolute path of the game directory.
        """
        config = configparser.ConfigParser()
        config['Paths'] = {'game_dir': path}
        with open(self.config_file, 'w') as configfile:
            config.write(configfile)

    def select_directory(self):
        """
        Opens a file dialog for the user to manually select the game directory.
        Saves the path if a valid directory is chosen.
        """
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setOption(QFileDialog.Option.ShowDirsOnly, True)
        
        if dialog.exec():
            selected_dir = dialog.selectedFiles()[0]
            if self.set_game_directory(selected_dir):
                self.save_path(selected_dir)
                # Disable auto-detect as the user has manually set the path.
                self.auto_detect_button.setEnabled(False)

    def auto_detect_path(self):
        """
        Searches for the 't6' folder in common user profile paths.
        This handles cases where the username is different from the original installation.
        """
        user_profiles_path = "C:/Users/"
        found_path = None

        if os.path.exists(user_profiles_path):
            # Iterate through each user's profile directory.
            for username_dir in os.listdir(user_profiles_path):
                potential_path = os.path.join(user_profiles_path, username_dir, 'AppData', 'Local', 'Plutonium', 'storage', 't6')
                if os.path.exists(potential_path):
                    found_path = potential_path
                    break
        
        if found_path and self.set_game_directory(found_path):
            self.save_path(found_path)
            QMessageBox.information(self, "Auto-Detect Success", f"Found game directory at: \n{found_path}")
            self.auto_detect_button.setEnabled(False)
        else:
            # Handle failure case for auto-detection.
            self.root_dir = ""
            self.path_input.setText("Path not found...")
            self.current_mod_label.setText("Please select a valid game directory.")
            self.current_mod_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #cc5500;")
            self.mod_list_widget.clear()
            self.switch_button.setEnabled(False)
            QMessageBox.warning(self, "Auto-Detect Failed", f"Could not find the 't6' folder.")

    def set_game_directory(self, path):
        """
        Validates the selected path and updates the UI accordingly.

        :param path: The path to be set as the game directory.
        :return: True if the path is valid and set, False otherwise.
        """
        if not os.path.isdir(path):
            # Reset UI if the path is not a valid directory.
            self.root_dir = ""
            self.path_input.setText("Invalid path selected.")
            self.current_mod_label.setText("Invalid directory. Please try again.")
            self.current_mod_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #cc5500;")
            self.mod_list_widget.clear()
            self.switch_button.setEnabled(False)
            return False

        self.root_dir = path
        self.path_input.setText(self.root_dir)
        # Define the path for the active mod tracking file.
        self.active_mod_file = os.path.join(self.root_dir, ".active_mod")
        self.refresh_mod_list()
        return True

    def get_current_active_mod(self):
        """
        Reads the name of the currently active mod from the `.active_mod` file.

        :return: The name of the active mod, or None if the file doesn't exist.
        """
        if os.path.exists(self.active_mod_file):
            with open(self.active_mod_file, "r") as f:
                return f.read().strip()
        return None

    def get_mod_folders(self):
        """
        Scans the game directory for valid mod folders.
        A folder is considered a mod if it contains a 'scripts' or 'images' subdirectory.

        :return: A list of folder names that are detected as mods.
        """
        mod_folders = []
        if not os.path.isdir(self.root_dir):
            return []
            
        for item in os.listdir(self.root_dir):
            # Skip ignored folders and non-directories.
            if item.lower() in self.ignore_folders:
                continue
            if os.path.isdir(os.path.join(self.root_dir, item)):
                # Check for the presence of key mod files.
                if os.path.exists(os.path.join(self.root_dir, item, 'scripts')) or \
                   os.path.exists(os.path.join(self.root_dir, item, 'images')):
                    mod_folders.append(item)
        return mod_folders

    def refresh_mod_list(self):
        """
        Updates the mod list widget with the detected mods and refreshes the UI state.
        """
        self.mod_list_widget.clear()
        mod_folders = self.get_mod_folders()
        if mod_folders:
            for mod in mod_folders:
                self.mod_list_widget.addItem(mod)
            # Enable UI elements if mods are found.
            self.current_mod_label.setStyleSheet("font-size: 14px; font-weight: bold;")
            self.switch_button.setEnabled(True)
        else:
            # Display a warning if no mods are found.
            self.current_mod_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #cc5500;")
            self.switch_button.setEnabled(False)

        current_mod_name = self.get_current_active_mod() or "None"
        self.current_mod_label.setText(f"Current Active Mod: {current_mod_name}")

    def switch_mod(self):
        """
        Switches the currently active mod by copying the selected mod's files
        to the game's root directory. Handles file replacement and error cases.
        """
        selected_items = self.mod_list_widget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "Please select a mod first.")
            return

        selected_mod = selected_items[0].text()
        mod_path = os.path.join(self.root_dir, selected_mod)

        target_scripts_path = os.path.join(self.root_dir, 'scripts')
        target_images_path = os.path.join(self.root_dir, 'images')

        try:
            # Remove any existing scripts or images from a previous mod.
            if os.path.exists(target_scripts_path):
                shutil.rmtree(target_scripts_path)
            if os.path.exists(target_images_path):
                shutil.rmtree(target_images_path)

            src_scripts_path = os.path.join(mod_path, 'scripts')
            src_images_path = os.path.join(mod_path, 'images')

            # Copy the new mod files into the game's root directory.
            if os.path.exists(src_scripts_path):
                shutil.copytree(src_scripts_path, target_scripts_path)
            if os.path.exists(src_images_path):
                shutil.copytree(src_images_path, target_images_path)

            # Update the `.active_mod` file to reflect the new state.
            with open(self.active_mod_file, "w") as f:
                f.write(selected_mod)

            self.refresh_mod_list()
            QMessageBox.information(self, "Success", f"Successfully switched to {selected_mod} mod!")

        except Exception as e:
            # Provide a detailed error message in case of failure.
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

if __name__ == "__main__":
    # Standard entry point for a PyQt application.
    app = QApplication(sys.argv)
    ex = ModSwitcherApp()
    ex.show()
    sys.exit(app.exec())

