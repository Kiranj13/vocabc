import requests
from bs4 import BeautifulSoup

def scan_website(url):
    result = {}

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            result['Security Headers'] = check_security_headers(response)
            result['XSS'] = check_xss(url)
            result['SQL Injection'] = check_sql_injection(url)
            result['Open Directories'] = check_open_directories(url)
            result['Command Injection'] = check_command_injection(url)

        else:
            result['error'] = f"Website returned status code {response.status_code}"

    except requests.RequestException as e:
        result['error'] = f"Failed to connect: {str(e)}"

    return result if isinstance(result, dict) else {"error": "Unexpected result format"}


def check_security_headers(response):
    headers = response.headers
    issues = []

    # Check for common security headers
    if 'X-Frame-Options' not in headers:
        issues.append("Missing X-Frame-Options header")

    if 'X-Content-Type-Options' not in headers:
        issues.append("Missing X-Content-Type-Options header")

    if 'Content-Security-Policy' not in headers:
        issues.append("Missing Content-Security-Policy header")

    return {
        "status": "Possible Vulnerability" if issues else "No issues found",
        "explanation": ", ".join(issues) if issues else "All security headers present."
    }


def check_xss(url):
    # Dummy function to simulate XSS check
    return {
        "status": "Possible Vulnerability",
        "explanation": "Found potential XSS vulnerability."
    }


def check_sql_injection(url):
    # Dummy function to simulate SQL Injection check
    return {
        "status": "No issues found",
        "explanation": "No SQL Injection vulnerabilities detected."
    }


def check_open_directories(url):
    # Dummy function to simulate Open Directory check
    return {
        "status": "Possible Vulnerability",
        "explanation": "Open directories found on server."
    }


def check_command_injection(url):
    # Dummy function to simulate Command Injection check
    return {
        "status": "No issues found",
        "explanation": "No Command Injection vulnerabilities detected."
    }


# Detailed explanations for vulnerabilities
vulnerability_explanations = {
    "XSS": "Cross-Site Scripting (XSS) allows attackers to inject malicious scripts into web pages viewed by others.",
    "SQL Injection": "SQL Injection vulnerabilities allow attackers to execute arbitrary SQL commands on your database.",
    "Open Directories": "Open directories allow unauthorized access to files and directories, revealing sensitive information.",
    "Command Injection": "Command Injection vulnerabilities allow attackers to execute arbitrary system commands.",
    "Security Headers": "Missing security headers can leave your website vulnerable to attacks."
}


