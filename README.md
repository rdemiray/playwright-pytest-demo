# playwright-pytest-demo
Playwright - Pytest - Python Automation Framework


## Introduction
This framework demonstrates two key automation capabilities:

- **Web Automation with Playwright:** Automate browser interactions for web applications using Playwright, enabling robust end-to-end testing with Python and pytest.
- **Native Mac Installer Automation:** Automate native macOS installer workflows using AppleScript and `osascript`, allowing for seamless testing and scripting of application installations on Mac.

## Folder Structure

The framework is organized into the following main directories:

- **`data/`**: Contains test data files (e.g., JSON, CSV) used for parameterizing and driving tests.
- **`pages/`**: Implements the Page Object Model; each file represents a page or component with its locators and actions.
- **`tests/`**: Includes all test scripts, organized by feature or functionality.
- **`utils/`**: Utility modules and helper functions shared across tests (e.g., custom assertions, configuration, logging).
This project is a Python-based automation framework utilizing Playwright and pytest. It follows the Page Object Model (POM) design pattern, promoting maintainability and scalability. The framework is structured in multiple layers, separating test logic, page interactions, and test data. Test data abstraction allows for easy management and reusability across different test scenarios.

## Setup and Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/playwright-pytest-demo.git
    cd playwright-pytest-demo
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**


    ```bash
    pip install -r requirements.txt
    playwright install
    ```
    (Python packages and Playwright browsers will be installed as specified in `requirements.txt`. The `playwright install` command downloads the necessary browser binaries.)


## Running Tests and Generating Reports

- **Run all tests:**
  ```bash
  pytest --html=report.html
  ```

- **Run a specific test file or test case:**
  ```bash
  pytest tests/test_example.py
  pytest tests/test_example.py::test_case_name
  ```

- **Run tests individually using VS Code:**
  The included `launch.json` configuration allows you to run and debug individual tests directly from the editor. All you need to do is to hit F5 key on your keyboard when a test file is selected.

- **View the HTML report:**
  After running tests with the `--html=report.html` option, open `report.html` in your browser to view detailed results.
  If you ran tests using F5 key (launch.json configuration), the report will be generated in the `reports` directory. The most recent report will overwrite the previous one, so you can always check the latest results.