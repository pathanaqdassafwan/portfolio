from flask import Flask, render_template, send_from_directory, url_for
import os
import time

app = Flask(__name__)

# Add timestamp to static files to prevent caching
@app.context_processor
def override_url_for():
    return dict(url_for=versioned_url_for)

def versioned_url_for(endpoint, **values):
    if endpoint == 'static':
        values['v'] = int(time.time())
    return url_for(endpoint, **values)

@app.route('/')
def home():
    css_url = url_for('static', filename='css/style.css')
    print(f"CSS URL: {css_url}")
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/download-resume')
def download_resume():
    # Serve the PDF file instead of generating a text file
    return send_from_directory('static', 'pathan_cv.pdf', as_attachment=True)

if __name__ == '__main__':
    # Create directories if they don't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('static/images', exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
