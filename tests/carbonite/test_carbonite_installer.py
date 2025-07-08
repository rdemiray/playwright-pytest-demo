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


    assert True