# Password Strength Checker

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
Enter the password you would like to verify: Secure@123
```
### Output:
```
Your password is strong
- Increase password length by 4 characters.
Would you like to check another password or retry? (y/n): 
```

---

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your updates or improvements.

---

## Future Improvements
- Update password strength to a score based system to eliminate "hard coding" password requirements.
- Break logic into smaller functions to make the code more maintainable.
- Optimize re-runs by giving users the option to exit the program by typing "exit" at any time.
- Simplify variable naming

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- **pyinputplus** library for secure and efficient user input handling.
- Python community for ongoing support and resources.
