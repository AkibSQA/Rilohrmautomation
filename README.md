# RiloHRM Automation

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/Selenium-4.0+-green.svg)](https://www.selenium.dev/)
[![PyCharm](https://img.shields.io/badge/PyCharm-2024.3.5-yellow.svg)](https://www.jetbrains.com/pycharm/)

Automated testing suite for RiloHRM, an HR management system. This project contains Selenium-based automation scripts for testing login functionality, dashboard navigation, and employee management features.

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup](#setup)
- [Running Tests](#running-tests)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## 🔧 Prerequisites

- Python 3.9 or higher
- PyCharm Community Edition 2024.3.5
- Selenium WebDriver
- Web browser (Chrome/Firefox) with corresponding WebDriver

## 💾 Installation

1. Clone the repository or download as a ZIP file:

   ```bash
   # Option 1: Clone the repository
   git clone https://github.com/AkibSQA/Rilohrmautomation.git
   
   # Option 2: Download as ZIP
   # Visit https://github.com/AkibSQA/Rilohrmautomation and click "Download ZIP"
   ```

2. If you downloaded as ZIP, extract the files to your desired location.

## 🛠️ Setup

1. Open PyCharm Community Edition 2024.3.5
2. Select "Open" and navigate to the project directory
3. Select the folder and click "OK"
4. Wait for PyCharm to index the project
5. Install required dependencies:
   ```bash
   pip install selenium
   pip install pytest
   ```

## ▶️ Running Tests

### Login Automation

To verify login functionality, dashboard appearance, and navigation to the Employee list page:

```bash
# Run the login test script
python Logintest.py
```

This script will:
- Launch the browser
- Navigate to the RiloHRM login page
- Enter credentials
- Verify successful login
- Check dashboard elements
- Navigate to the Employee list page

### Employee Management Automation

To test the employee addition functionality:

```bash
# Run the employee addition test script
python addemployeeform.py
```

This script will:
- Login to the system
- Navigate to the "Add Employee" section
- Fill out the employee form with test data
- Submit the form
- Verify the employee was added successfully

## ✨ Features

- **Login Automation**: Tests the authentication system and verifies access to protected areas
- **Dashboard Verification**: Ensures all dashboard components load correctly
- **Navigation Testing**: Verifies menu functionality and page transitions
- **Employee Management**: Tests the complete employee addition workflow

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add some amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

© 2024 RiloHRM Automation | Created by [AkibSQA](https://github.com/AkibSQA)
