# vuln_scanner 

## 👥 Team Information
**Team Name:** [Zeal]  

**Team Members:**
- Kiran
- (https://github.com/kiranj13) 

## 💡 Project Idea
This project aims to develop a web-based vulnerability scanner that allows users to check websites for common security issues such as XSS, SQL Injection, Open Directories, Command Injection, and missing Security Headers. It provides real-time analysis with detailed explanations and recommended solutions to help improve website security.

## ✨ Key Features
- 🔍  Real-time Website Scanning : Scan any URL instantly for common web vulnerabilities.

- 🛡️ Detection of Common Vulnerabilities
       Identifies issues like:
      • Cross-Site Scripting (XSS)
      •  Command Injection
      •  Directory Traversal
      •  Open Directories
      •  Missing Security Headers
      •  Content-Security-Policy
      •  X-Frame-Options
      •  X-XSS-Protection
      •  Strict-Transport-Security
      •  Exposed Admin Interfaces
      •  Unrestricted File Upload (basic checks)
      •  Open Ports/Services (via nmap)
      •  Cross-Site Request Forgery (CSRF) (basic detection)
      •  Information Disclosure (emails, comments in source code, etc.)
  
 - 📝 Detailed Vulnerability Explanations : Provides clear, concise descriptions of each vulnerability found.

💡 Suggested Fixes & Recommendations : Offers practical solutions to help patch the vulnerabilities.
🔗 Direct Link to Scanned Site :View the target site directly from the results page.

📄 Expandable Detail View
Click "View Details" for in-depth insights on each specific vulnerability.

🔒 Built with Flask (Python)
Lightweight and fast backend using Flask for secure and scalable performance.

## 🛠️ Tech Stack
| Technology        | Version  | Purpose                                                      |
| ----------------- | -------- | ------------------------------------------------------------ |
| Python            | 3.10+    | Main programming language                                    |
| requests          | v2.31.0  | Sending HTTP requests to interact with web pages             |
| BeautifulSoup     | v4.12.2  | Parsing and extracting data from HTML pages                  |
| urllib            | Built-in | Handling URLs and encoding/decoding query parameters         |
| selenium          | v4.14.0  | Automating browser actions (used for login/session handling) |
| socket            | Built-in | Performing low-level network checks                          |
| nmap              | v7.94    | Port scanning and service discovery                          |
| sslscan           | v2.0.15  | Scanning SSL/TLS configurations and certificate issues       |
| OWASP ZAP API     | v2.12.0  | External security scanning API                               |
| Nikto             | v2.5.0   | Web server vulnerability scanning                            |
| Flask             | v2.3.3   | Creating a simple web interface for the scanner              |
| SQLite            | v3.41.2  | Storing scan history or results locally                      |
| jinja2            | v3.1.2   | Templating engine for HTML report generation                 |
| reportlab         | v4.0.7   | Generating PDF reports                                       |
| argparse          | Built-in | Handling command-line arguments                              |
| json              | Built-in | Handling data in JSON format                                 |


## 🛠️ Setup Instructions

### Prerequisites
- Node.js v16+ / Python 3.8+
- npm/yarn/pip
- [Any other requirements]

### Installation
Step 1: Clone the repository
git clone https://github.com/Kiranj13/vuln_scanner
cd vuln-scanner

Step 2: (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate

 Step 3: Install all required dependencies
pip install -r requirements.txt

 Step 4: (OInstall external tools
 Install nmap and sslscan if not already installed
sudo apt install nmap sslscan  

 Basic scan of a website
python scanner.py --url https://example.com

 Run the optional Flask web interface (if available)
python app.py


### Running the Project
# Basic scan of a website
python scanner.py --url https://example.com

# Run the optional Flask web interface (if available)
python app.py


## 🤝 How to Contribute
We welcome contributions! Whether it's fixing bugs, writing better docs, or adding new features — your help is appreciated.

### Good First Issues
- [ ] Implement feature: Add login authentication scanner
- [ ] Improve documentation: Add screenshots to README
- [ ] Fix bug: Scanner fails on redirecting URLs (#123)

### Contribution Workflow
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -m "Add: brief message describing your change"`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a Pull Request


## Acknowledgments
Inspired by ::-

1.OWASP(https://www.zaproxy.org/)

2.Nikto(https://cirt.net/Nikto2)


Used documentation from:

1.OWASP ZAP API(https://www.zaproxy.org/docs/api/)

2.BeautifulSoup Docs(https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

3.Python Requests Library(https://docs.python-requests.org/en/latest/)
