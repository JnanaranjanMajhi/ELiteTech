# Task -1
# Email Slicer

## Description

The Email Slicer script is a Python program that processes multiple email addresses, validates them, and extracts relevant information such as the username, domain, and domain type. The user can input multiple email addresses, and the script will validate each one, providing the details in a user-friendly format. Additionally, the script offers an option to save the processed results into a text file.

## Features

- Accepts multiple email addresses separated by commas.
- Validates email addresses using a regular expression.
- Extracts and displays the following details for each valid email:
  - **Email**: The original email address.
  - **Username**: The part of the email before the "@" symbol.
  - **Domain**: The domain part of the email.
  - **Domain Type**: The first part of the domain name, capitalized.
- Invalid email addresses are flagged, and the user is notified.
- Provides an option to save the results to a text file.

## Requirements

- Python 3.x (No external libraries are required; only the standard Python library is used).

## Installation

To use the script:

1. Clone or download the repository to your local machine.
2. Ensure that Python 3.x is installed on your system.

   - You can download Python 3 from the official website: https://www.python.org/downloads/

3. Navigate to the folder where the script is located.

## How to Use

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is stored.
3. Run the script using the following command:

   ```bash
   python email_slicer.py
   ```
4. You will be prompted to enter multiple email addresses separated by commas (e.g., user1@example.com, user2@domain.org).
5. The script will validate the emails, and for each valid one, it will display the following:
   - Email
   - Username
   - Domain
   - Domain Type
6. After processing, you will be asked if you want to save the results to a file. Type yes to save the output to a file named email_slicer_output.txt, or no to discard it.


# Task - 2
# Acronym Creator

The Acronym Creator is a simple Python program that generates acronyms from phrases. The program prompts the user to enter a phrase and, optionally, a separator for the acronym. It removes punctuation, splits the phrase into words, and generates the acronym by taking the first letter of each word.

## Features

- **Generate Acronym**: Converts any phrase into an acronym by extracting the first letter of each word.
- **Custom Separator**: Allows users to specify a separator between acronym letters (e.g., `-` or `.`).
- **Input Validation**: Handles empty or invalid input gracefully.
- **Exit Option**: Type `quit` to exit the program.

## Installation

No installation is required to use this program, as it is a standalone Python script. Ensure that you have Python 3.x installed on your system.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python:

   ```bash
   python acronym_creator.py
   ```
3. The program will prompt you to enter a phrase. You can also provide an optional separator for the acronym letters.
4. Enter quit to exit the program.
   ```bash
   Enter a phrase to create an acronym (or 'quit' to exit): Random Access Memory
   Enter a separator (or press Enter to skip): -
   The acronym is: R-A-M
   Enter a phrase to create an acronym (or 'quit' to exit): Central Processing Unit
   Enter a separator (or press Enter to skip):
   The acronym is: CPU
   ```

# Task - 3
# BMI Calculator

This is a simple BMI (Body Mass Index) Calculator GUI application built using Python's Tkinter library. The program allows users to input their weight (in kilograms) and height (in meters) to calculate their BMI and interpret the result based on standard BMI categories.

## Features

- Input fields for weight and height.
- BMI calculation based on the formula: `BMI = weight (kg) / height (m)^2`.
- BMI interpretation, categorized as:
  - Underweight: BMI < 18.5
  - Normal weight: 18.5 <= BMI < 24.9
  - Overweight: 25 <= BMI < 29.9
  - Obesity: BMI >= 30
- Error handling for invalid inputs (non-numeric or zero/negative values).
- Clear button to reset the input fields and results.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)

## Installation

1. Ensure Python 3.x is installed on your machine. You can download it from [python.org](https://www.python.org/).
2. Tkinter is bundled with Python, so you don't need to install it separately.
3. Download or clone this repository.

## Usage

1. Run the Python script (`bmi_calculator.py`).
2. Enter your weight (in kilograms) and height (in meters) into the input fields.
3. Click on "Calculate BMI" to compute your BMI and see the result.
4. If you'd like to reset the fields, click on the "Clear" button.

## Error Handling

- If non-numeric values are entered, an error message will appear asking for numerical values.
- If weight or height is entered as zero or negative, an error message will prompt for valid positive values.

## Acknowledgements

- Tkinter library for creating the graphical user interface.
- BMI categories as per the World Health Organization (WHO) guidelines.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

