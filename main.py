from PySide6.QtWidgets import QApplication

app = QApplication([])

# Load the UI file and create the dialog
dialog = QWidgets()
ui = Ui_Dialog()
ui.setupUi(dialog)

# Assume you have read the WorkDirPath value from the configuration file
work_dir_path = "/path/to/your/directory"

# Set the WorkDirPath value to the WorkDirFolder QLineEdit
ui.WorkDirFolder.setText(work_dir_path)

# Show the dialog
dialog.show()

# Run the application loop
app.exec()