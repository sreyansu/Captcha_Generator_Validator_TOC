# CAPTCHA Web App

This project is a simple CAPTCHA generator and validator web application. It allows users to generate a CAPTCHA image and validate their input against it. The application is built using Python and Flask for the backend, and HTML, CSS, and JavaScript for the frontend.

## Project Structure

```
captcha-web-app
├── Captcha.py          # Logic for generating and validating CAPTCHA images
├── server.py           # Backend server integrating CAPTCHA functionality
├── templates
│   └── index.html      # HTML file for displaying CAPTCHA and input field
├── static
│   ├── css
│   │   └── style.css    # Styles for the HTML page
│   └── js
│       └── main.js      # Client-side JavaScript for interactions
├── requirements.txt     # Python dependencies for the project
├── .gitignore           # Files and directories to ignore by Git
└── README.md            # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the server:**
   ```
   python server.py
   ```

5. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000` to view the CAPTCHA generator and validator.

## Usage

- The application will display a CAPTCHA image along with an input field.
- Users need to enter the text displayed in the CAPTCHA image.
- If the input matches the CAPTCHA text, access is granted; otherwise, users have a limited number of attempts to enter the correct text.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

