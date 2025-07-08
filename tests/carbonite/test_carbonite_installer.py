from pages.installer_dialog_page import MacInstallerDialogPage
import pytest
import os


@pytest.mark.tc4
def test_mac_installer_dialog():
    mac_installer_page = MacInstallerDialogPage()
    zip_path = "/Users/remidemiray/Downloads/Carbonite-mac-personal-client.app.zip"
    # app_path = mac_installer_page.unzip_installer(zip_path)
    # app_path = mac_installer_page.temp_dir / "Carbonite-mac-personal-client.app"
    mac_installer_page.unzip_with_permissions(zip_path, mac_installer_page.temp_dir)

    app_path = mac_installer_page.get_app_name_in_folder(mac_installer_page.temp_dir)

    # Check if the .app file exists
    assert os.path.exists(app_path), "The .app file does not exist after unzipping."

    # Launch the app
    mac_installer_page.launch_app(app_path)

    # Click the "Continue" button in the installer dialog
    mac_installer_page.click_continue_button()

    # Wait for the user to enter their Mac password and click "Add Helper"
    # macOS treats password prompts (like the “Add Helper” dialog) as secure input fields, and by design, prevents scripting tools like AppleScript from accessing them.

    # Alternative methods:
    # 1. If app supports slient installation, use command line tools and start with `sudo`.
    # 2. Use https://github.com/BlueM/cliclick to simulate mouse clicks and keyboard input.(might be very fragile and flakey)
    print("Please enter your Mac password and click 'Add Helper' in the dialog, then press Enter to continue...")

    assert mac_installer_page.is_installation_dialog_open(), "Installation dialog is no longer open."

    assert mac_installer_page.wait_for_error_dialog(), "Error dialog did not appear as expected."

    mac_installer_page.click_abort_button()

    # Confirm that the process is no longer running
    assert not mac_installer_page.is_process_running("CarboniteInstall"), "Process is still running after clicking Abort."


    assert True