from flask import Flask, render_template, request, redirect, url_for
from scanner import scan_website, vulnerability_explanations
import validators

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    error = None
    url = None
    has_vulnerability = False  # Flag for red box
    no_vulnerability = True    # Flag for green box (default to true)

    if request.method == 'POST':
        url = request.form.get('url')

        if validators.url(url):
            result = scan_website(url)

            if isinstance(result, dict):
                for vuln, data in result.items():
                    if isinstance(data, dict) and "status" in data:
                        if "Possible" in data.get('status', ''):
                            has_vulnerability = True
                            no_vulnerability = False  # At least one vulnerability found
                            break
                        else:
                            no_vulnerability = no_vulnerability and "No issues found" in data.get('status', '')
            else:
                error = "Unexpected result format."
        else:
            error = "Invalid URL. Please enter a valid website URL."

    return render_template(
        'index.html',
        url=url,
        result=result,
        error=error,
        has_vulnerability=has_vulnerability,
        no_vulnerability=no_vulnerability
    )


@app.route('/vulnerability/<vuln_name>')
def vulnerability_detail(vuln_name):
    """Render detailed vulnerability explanation"""
    explanation = vulnerability_explanations.get(vuln_name, "No details available.")
    return render_template('vulnerability.html', vuln_name=vuln_name, explanation=explanation)


if __name__ == '__main__':
    app.run(debug=True, port=5091)






