import os
import shutil
from datetime import datetime, timedelta

class FileTransfer:
    def __init__(self, source_folder, destination_folder):
        self.source_folder = source_folder
        self.destination_folder = destination_folder

    def transferFiles(self):
        # Get the current time
        current_time = datetime.now()

        # Calculate the time threshold for files to be considered new/edited (24 hours ago)
        threshold_time = current_time - timedelta(hours=24)

        # Iterate over the files in the source folder
        for filename in os.listdir(self.source_folder):
            file_path = os.path.join(self.source_folder, filename)

            # Get the last modified time of the file
            file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))

            # Check if the file was modified within the last 24 hours
            if file_modified_time > threshold_time:
                # Transfer the file to the destination folder
                shutil.copy(file_path, self.destination_folder)
                print(f"Transferred {filename} to {self.destination_folder}")

# Usage example
source_folder = '/path/to/source_folder'
destination_folder = '/path/to/destination_folder'

file_transfer = FileTransfer(source_folder, destination_folder)
file_transfer.transferFiles()