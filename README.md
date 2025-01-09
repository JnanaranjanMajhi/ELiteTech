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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

