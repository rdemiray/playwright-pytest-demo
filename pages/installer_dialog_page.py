import subprocess
import zipfile
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
        time.sleep(10)  # give the app couple of seconds to launch

    def click_continue_button(self, process_name="CarboniteInstall"):
        script = f'''
        tell application "System Events"
            tell process "{process_name}"
                set frontmost to true
                delay 1
                click button "Continue" of window 1
            end tell
        end tell
        '''
        subprocess.run(["osascript", "-e", script], check=True)
    
    def is_installation_dialog_open(self, process_name="CarboniteInstall") -> bool:
        script = f'''
        tell application "System Events"
            set dialog_open to false
            if exists process "{process_name}" then
                if (count of windows of process "{process_name}") > 0 then
                    set dialog_open to true
                end if
            end if
        end tell
        return dialog_open
        '''
        result = subprocess.run(
            ["osascript", "-e", script],
            capture_output=True,
            text=True
        )
        return result.stdout.strip().lower() == "true"
    

    # def wait_for_error_dialog(self, process_name="CarboniteInstall", timeout=45):
    #     script = f'''
    #     tell application "System Events"
    #         if exists (button "Abort" of window 1 of process "{process_name}") then
    #             return true
    #         else
    #             return false
    #         end if
    #     end tell
    #     '''
    #     start_time = time.time()
    #     while time.time() - start_time < timeout:
    #         result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    #         if result.stdout.strip().lower() == "true":
    #             print("Error dialog appeared.")
    #             return True
    #         time.sleep(1)
    #     print("Timeout: Error dialog did not appear.")
    #     return False

    # def wait_for_error_dialog(self, process_name="CarboniteInstall", timeout=30):
    #     print(f"Waiting up to {timeout}s for error dialog in process '{process_name}'...")
    #     check_script = f'''
    #     tell application "System Events"
    #         if exists process "{process_name}" then
    #             tell process "{process_name}"
    #                 repeat with w in windows
    #                     if exists (button "Abort" of w) then
    #                         return true
    #                     end if
    #                 end repeat
    #             end tell
    #         end if
    #         return false
    #     end tell
    #     '''

    #     start_time = time.time()
    #     while time.time() - start_time < timeout:
    #         result = subprocess.run(
    #             ["osascript", "-e", check_script],
    #             capture_output=True,
    #             text=True
    #         )
    #         is_found = result.stdout.strip().lower() == "true"
    #         if is_found:
    #             print("Found error dialog with 'Abort' button.")
    #             return True
    #         time.sleep(1)

    #     raise AssertionError("Error dialog did not appear as expected.")

    # def wait_for_error_dialog(self, process_name="CarboniteInstall", timeout=30):
    #     print(f"Waiting up to {timeout}s for error dialog with 'Abort' button in '{process_name}'...")

    #     check_script = f'''
    #     tell application "System Events"
    #         if exists process "{process_name}" then
    #             tell process "{process_name}"
    #                 -- Check all windows
    #                 repeat with w in windows
    #                     if exists (button "Abort" of w) then
    #                         return true
    #                     end if
    #                 end repeat

    #                 -- Check sheets attached to windows
    #                 repeat with w in windows
    #                     repeat with s in sheets of w
    #                         if exists (button "Abort" of s) then
    #                             return true
    #                         end if
    #                     end repeat
    #                 end repeat

    #                 -- Check dialogs (may be treated as windows)
    #                 if exists (button "Abort") then
    #                     return true
    #                 end if
    #             end tell
    #         end if
    #         return false
    #     end tell
    #     '''

    #     start_time = time.time()
    #     while time.time() - start_time < timeout:
    #         result = subprocess.run(
    #             ["osascript", "-e", check_script],
    #             capture_output=True,
    #             text=True
    #         )
    #         if result.stdout.strip().lower() == "true":
    #             print("Found 'Abort' button in error dialog.")
    #             return True
    #         time.sleep(1)

    #     raise AssertionError("Error dialog with 'Abort' button did not appear within timeout.")
    
    # def click_abort_button(self, process_name="CarboniteInstall"):
    #     script = f'''
    #     tell application "System Events"
    #         tell process "{process_name}"
    #             click button "Abort" of window 1
    #         end tell
    #     end tell
    #     '''
    #     subprocess.run(["osascript", "-e", script], check=True)

    # def wait_for_error_dialog(self, process_name="CarboniteInstall", timeout=30):
    #     print(f"Waiting up to {timeout}s for error dialog with 'Abort' button in '{process_name}'...")

    #     check_script = f'''
    #     tell application "System Events"
    #         if exists process "{process_name}" then
    #             tell process "{process_name}"
    #                 repeat with w in windows
    #                     if exists (button "Abort" of w) then
    #                         return true
    #                     end if
    #                     -- Check sheets if present
    #                     if (count of sheets of w) > 0 then
    #                         repeat with s in sheets of w
    #                             if exists (button "Abort" of s) then
    #                                 return true
    #                             end if
    #                         end repeat
    #                     end if
    #                 end repeat
    #             end tell
    #         end if
    #         return false
    #     end tell
    #     '''

    #     start_time = time.time()
    #     while time.time() - start_time < timeout:
    #         result = subprocess.run(
    #             ["osascript", "-e", check_script],
    #             capture_output=True,
    #             text=True
    #         )
    #         if result.stdout.strip().lower() == "true":
    #             print("Found error dialog with 'Abort' button.")
    #             return True
    #         time.sleep(1)

    #     raise AssertionError("Error dialog with 'Abort' button did not appear within timeout.")

    # def click_abort_button(self, process_name="CarboniteInstall"):
    #     print("Attempting to click 'Abort' button...")

    #     click_script = f'''
    #     tell application "System Events"
    #         tell process "{process_name}"
    #             repeat with w in windows
    #                 if exists (button "Abort" of w) then
    #                     click button "Abort" of w
    #                     return
    #                 end if
    #                 -- Try sheets attached to the window
    #                 repeat with s in sheets of w
    #                     if exists (button "Abort" of s) then
    #                         click button "Abort" of s
    #                         return
    #                     end if
    #                 end repeat
    #             end repeat
    #         end tell
    #     end tell
    #     '''
    #     subprocess.run(["osascript", "-e", click_script], check=True)

    def wait_for_error_dialog(self, process_name="CarboniteInstall", timeout=30):
        script = f'''
        tell application "System Events"
            tell process "{process_name}"
                if exists (button 2 of group 1 of window 1) then
                    return true
                else
                    return false
                end if
            end tell
        end tell
        '''
        start_time = time.time()
        while time.time() - start_time < timeout:
            result = subprocess.run(
                ["osascript", "-e", script],
                capture_output=True,
                text=True
            )
            if result.stdout.strip().lower() == "true":
                return True
            time.sleep(1)
        return False

    def click_abort_button(self, process_name="CarboniteInstall"):
        script = f'''
        tell application "System Events"
            tell process "{process_name}"
                click button 2 of group 1 of window 1
            end tell
        end tell
        '''
        subprocess.run(["osascript", "-e", script], check=True)

    def is_process_running(self, process_name="CarboniteInstall") -> bool:
        result = subprocess.run(["pgrep", "-x", process_name], capture_output=True)
        return result.returncode == 0