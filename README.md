
# Mortis - Web Application Vulnerability Scanner

A Python-based automated vulnerability scanner designed to detect common web application security vulnerabilities including SQL Injection (SQLi) and Cross-Site Scripting (XSS).

## Features

- **SQL Injection Detection**: Automatically detects SQL injection vulnerabilities in web forms
- **XSS Detection**: Identifies potential Cross-Site Scripting vulnerabilities
- **Automated Form Discovery**: Parses HTML to find and extract all forms from target websites
- **Baseline Response Analysis**: Compares application responses to identify anomalies caused by payload injection
- **Dynamic Payload Injection**: Tests input fields with malicious payloads to expose vulnerabilities

## Project Structure

```
mortis/
├── Scanner.py           # Main scanner entry point
├── checks/
│   ├── sqli.py         # SQL Injection detection module
│   └── xss.py          # Cross-Site Scripting detection module
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

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

### Vulnerability Detection
- **SQL Injection**: Tests fields with SQL payloads to detect time-based and response-based SQLi
- **XSS**: Injects JavaScript payloads to identify stored and reflected XSS vulnerabilities

## Disclaimer

**⚠️ Educational Purpose Only**

This tool is designed for authorized security testing and educational purposes only. Unauthorized access to computer systems is illegal. Always:
- Obtain explicit written permission before testing any website
- Only use on systems you own or have permission to test
- Comply with all applicable laws and regulations
- Use responsibly in controlled environments

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Author

0xIta3hi




