import subprocess
import zipfile
import os
import time
from pathlib import Path


class MacInstallerDialogPage:
    def __init__(self, temp_dir="/Users/remidemiray/Downloads/carbonite_temp"):
        self.temp_dir = Path(temp_dir)
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        # /Users/remidemiray/Downloads/Carbonite-mac-personal-client.app.zip
    
    def unzip_installer(self, zip_path: str) -> str:
        """Unzips .zip file and returns path to the .app"""
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(self.temp_dir)

        for item in self.temp_dir.iterdir():
            if item.suffix == ".app":
                return str(item)

        raise FileNotFoundError("No .app file found in zip.")
    
    def unzip_with_permissions(self, zip_path, dest_path):
        """Unzips .zip file to the destination path with permissions preserved so that the files under Contents/MacOS are Unix exceutables, not just documents"""
        
        # -o for overwrite existing files
        # -q for quiet mode, suppressing output
        # -d for destination directory
        subprocess.run(["unzip", "-q", "-o", zip_path, "-d", dest_path], check=True)

    def get_app_name_in_folder(self, folder: Path) -> Path:
        for item in folder.rglob("*.app"):
            return item
        raise FileNotFoundError("No .app found after unzipping.")
    
    def launch_app(self, app_path: str):
        subprocess.run(["open", app_path], check=True)
        time.sleep(3)  # give the app a few seconds to launch