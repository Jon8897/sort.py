# Sorting App

*Version 1.0.0.2*

This project is a Python-based tool designed for efficient web scraping, specifically tailored for finding SKU numbers and extracting SEO-related metadata from specified URLs.

## Tools Needed

Before running the program, ensure you have the following:

1. **BeautifulSoup (bs4)**: A Python library for pulling data from HTML and XML files.
    ```
    pip install beautifulsoup4
    ```
2. **Python**: The program requires Python's latest version. Visit [python.org](https://www.python.org/downloads/) to download and install it.

## User Guide

### Downloading and Setting Up

1. **Download**:
    - Go to the 'Code' section of the GitHub repository.
    - Click on 'Download ZIP', then extract the ZIP file to your preferred location.

2. **File Preparation**:
    - Place your input CSV file in the same directory as the program.
    - The CSV file should be named according to the reference in the script (default is `pyhtontestdata.csv`). You can change it to match your file's name (e.g., `data.csv`).

### Running the Program

1. Open the terminal (Command Prompt, PowerShell, or Terminal).
2. Navigate to the directory where the program is located.
3. Execute the program:
    ```
    python sort.py
    ```
    - The script's execution time will depend on the size of the CSV file.
    - Monitor the progress directly in the terminal.

### Retrieving Output

- After completion, an `output.csv` file will be generated in the same directory.
- Rename and utilize this file as needed for your requirements.

## Future Upgrades

1. **GUI Integration**: Future iterations will include a user-friendly graphical interface to simplify interactions and improve accessibility.

2. **Performance Enhancements**: Efforts are underway to optimize the script for faster processing, especially for larger data sets.

## Troubleshooting

If you encounter issues, check the following:

- Ensure Python is correctly installed and added to your system's PATH.
- Verify that the CSV file is correctly named and placed in the same directory as the program.
- Check for error messages in the terminal and ensure all required libraries are installed.
