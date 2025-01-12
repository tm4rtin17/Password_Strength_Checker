# Password Strength Checker v1.0.1

## Description
This Python program allows users to verify the strength of their passwords. Based on specific criteria such as length, the presence of uppercase letters, and special characters, the program assigns a strength rating to the password (“weak,” “average,” “strong,” or “very strong”). It also provides feedback on how users can improve their password strength.

---

## Features
- **Password Strength Classification:** 
  - Weak: Less than 6 characters.
  - Average: At least 6 but fewer than 8 characters, mixed letters and numbers, no symbols.
  - Strong: At least 8 characters, contains one uppercase letter, one number, and one special character.
  - Very Strong: At least 12 characters, contains one uppercase letter, one number, and one special character.
- **Dynamic Feedback:** Offers suggestions to improve password strength based on criteria.
- **Loop for Reuse:** Users can check multiple passwords in a single session.
- **Secure Input Handling:** Uses the `pyinputplus` library for password entry validation.
- **Exit Option:** Close the program by typing 'q'.

---

## Requirements
- Python 3.13.1 or higher
- `pyinputplus` library (install using `pip install pyinputplus`)

---

## Installation
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/your-repository/password-strength-checker.git
   ```
2. Navigate to the project directory.
   ```bash
   cd password-strength-checker
   ```
3. Install dependencies.
   ```bash
   pip install pyinputplus
   ```

---

## Usage
1. Run the program.
   ```bash
   python password_strength_checker.py
   ```
2. Follow the prompts to input a password.
3. Review the password strength rating and improvement suggestions.
4. Choose whether to check another password or exit the program.

---

## Example
### Input:
```
Enter the password you would like to verify [Enter 'q' at to exit program.]: Secure@123
```
### Output:
```
Your password is strong
- Increase password length by 4 characters.
Would you like to check another password? (y/n): 
```

---

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your updates or improvements.

---
## Changelog v1.0.1
Several flow improvements made to make code more readable and helps the code appear more organized.

- Created a second program `Main.py` to house the main control flow of the program.
- Kept all of the functions on `Pass_Func.py` for separation from the main program.
- Created `main()` which calls for user input and the the linked functions for checking the password.

---

## Future Improvements
- Update password strength to a score based system to eliminate "hard coding" password requirements.
---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- **pyinputplus** library for secure and efficient user input handling.
- Python community for ongoing support and resources.
