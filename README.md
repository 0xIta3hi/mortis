
# Mortis - Web Application Vulnerability Scanner

A comprehensive Python-based automated vulnerability scanner designed to detect a wide range of web application security vulnerabilities. Mortis performs in-depth analysis of web applications to identify common attack vectors and security flaws including injection attacks, client-side vulnerabilities, and more.

## Features

### Vulnerability Detection Modules
- **SQL Injection (SQLi)**: Detects SQL injection vulnerabilities in web forms through payload injection and response analysis
- **Extensible Architecture**: Modular design allows easy addition of new vulnerability checks

### Core Capabilities
- **Automated Form Discovery**: Parses HTML to find and extract all forms from target websites
- **Intelligent Field Mapping**: Recognizes common field types (username, password, email, search, etc.)
- **Baseline Response Analysis**: Compares application responses to identify anomalies caused by payload injection
- **Dynamic Payload Injection**: Tests input fields with malicious payloads to expose vulnerabilities
- **Time-Based Detection**: Identifies vulnerabilities through response time analysis
- **Content-Based Detection**: Detects changes in response content from injected payloads

## Project Structure

```
mortis/
├── Scanner.py           # Main scanner entry point & orchestration
├── checks/
│   ├── sqli.py         # SQL Injection detection module
│   └── [additional modules for other vulnerabilities]
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

The `checks/` directory contains modular vulnerability detection modules that can be independently developed and integrated.

## Installation

1. Clone or download the project:
```bash
cd mortis
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Requirements

The scanner uses the following Python libraries:
- **requests**: For making HTTP requests to target websites
- **BeautifulSoup4**: For parsing HTML and extracting form data

## Usage

Run the scanner with:
```bash
python Scanner.py
```

The scanner will prompt you to enter the target URL, then automatically:
1. Fetch the webpage content
2. Parse all HTML forms
3. Analyze form fields and their attributes
4. Inject test payloads to identify vulnerabilities
5. Compare responses against baseline behavior

## How It Works

### Form Discovery & Analysis
- Automatically crawls the target website to find all `<form>`, `<input>`, and `<textarea>` elements
- Extracts form attributes: action URL, HTTP method, field names, and requirements
- Maps input types and required fields for intelligent payload injection

### Baseline Response Generation
- Submits legitimate data to establish baseline application behavior
- Records response metrics: status codes, content length, response time
- Uses this baseline to detect anomalies from malicious inputs

### Vulnerability Detection Modules

#### SQL Injection (SQLi)
- Tests fields with SQL payloads to detect time-based and response-based SQLi
- Analyzes response delays to identify blind SQL injection
- Compares response content for union-based injection detection

#### Additional Vulnerability Checks
The scanner architecture is designed to support additional vulnerability detection modules including:
- **CSRF (Cross-Site Request Forgery)**: Identifies missing or weak CSRF token validation
- **LFI/RFI (Local/Remote File Inclusion)**: Detects file inclusion vulnerabilities
- **IDOR (Insecure Direct Object References)**: Finds authorization bypass vulnerabilities
- **Authentication Flaws**: Identifies weak authentication mechanisms
- **Security Headers**: Analyzes missing security headers
- And more custom vulnerability checks

## Disclaimer

**⚠️ Educational Purpose Only**

This tool is designed for authorized security testing and educational purposes only. Unauthorized access to computer systems is illegal. Always:
- Obtain explicit written permission before testing any website
- Only use on systems you own or have permission to test
- Comply with all applicable laws and regulations
- Use responsibly in controlled environments

## Adding New Vulnerability Checks

To extend Mortis with additional vulnerability detection modules:

1. Create a new Python file in the `checks/` directory
2. Implement vulnerability detection logic following the existing module patterns
3. Integrate the module into the main Scanner.py orchestration
4. Add documentation for the new vulnerability type in this README

Example module structure:
```python
def detect_vulnerability(forms, baseline_response):
    """
    Detect a specific vulnerability type
    Args:
        forms: Parsed form data from target website
        baseline_response: Baseline response metrics
    Returns:
        List of detected vulnerabilities
    """
    vulnerabilities = []
    # Implementation here
    return vulnerabilities
```

## Contributing

Contributions are welcome! Please feel free to submit issues, pull requests, or new vulnerability detection modules.

## License

[Add your license here]

## Author

0xIta3hi
