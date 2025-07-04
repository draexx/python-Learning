# Python Learning Repository

This repository is for Python programming and framework testing.

## Getting Started

This repository contains two main projects:

*   **PySample**: Contains Python code for various syntax and library tests.
*   **flaskProject**: A small project demonstrating the use of the Flask framework.

### Prerequisites

*   **PySample**: Requires pyTesseract and OpenCV for image reading.
    *   You can install these using pip:
        ```bash
        pip install pytesseract opencv-python
        ```
*   **flaskProject**: Dependencies are listed in `flaskProject/requeriments.txt`.

### Installing

**flaskProject**:

1.  Navigate to the `flaskProject` directory.
2.  Install the dependencies:
    ```bash
    pip install -r requeriments.txt
    ```

### Environment Variables

For the `flaskProject` to work, you need to set the following environment variables:

#### Linux/Mac

```bash
export FLASK_APP="entrypoint"
export FLASK_ENV="development"
export APP_SETTINGS_MODULE="config.local"
```

#### Windows

```powershell
set FLASK_APP="entrypoint"
set FLASK_ENV="development"
set APP_SETTINGS_MODULE="config.local"
```

> **Recommendation**: If you are using a virtual environment (e.g., `virtualenv`), it's good practice to add these environment variable settings to the `activate` (for Linux/Mac) or `activate.bat` (for Windows) script within your virtual environment's directory.

## Running the tests

Currently, this project does not have an automated test suite.

## Built With

*   [Flask](https://www.palletsprojects.com/p/flask/) - The web framework used in `flaskProject`.
*   [pyTesseract](https://pypi.org/project/pytesseract/) - OCR tool used in `PySample`.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/draexx/946513c6cb2ee2adffca97b2999dc4d2) for details on our code of conduct and the process for submitting pull requests.

## Authors

*   **Pedro Carranza** - *Initial work* - [Draexx](https://github.com/draexx)

See also the list of [contributors](https://github.com/draexx/python-Learning/contributors) who participated in this project.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

*   Hat tip to anyone whose code was used.
*   Inspiration.
