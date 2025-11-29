from flask import Flask

app = Flask(__name__)


nav = """
<nav>
    <a href="/">Home</a> | 
    <a href="/about">About</a> | 
    <a href="/resume">Resume</a>
</nav>
<hr>
"""


@app.route("/")
def home():
    return nav + """
    <style>
            body { font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px; }
            .container { max-width: 900px; margin: auto; background: white; padding: 25px; border-radius: 10px; }
            h1, h2 { color: #333; }
            .section { margin-bottom: 25px; }
            .section h2 { border-left: 4px solid #007bff; padding-left: 10px; }
            .skills span { background: #007bff; color: white; padding: 5px 10px; margin: 5px; border-radius: 5px; display: inline-block; }
        </style>
    <h1>Welcome to My Home Page</h1>
    <p>THis website is made in Flask.</p>
    """


@app.route("/about")
def about():
    return nav + """
    <style>
            body { font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px; }
            .container { max-width: 900px; margin: auto; background: white; padding: 25px; border-radius: 10px; }
            h1, h2 { color: #333; }
            .section { margin-bottom: 25px; }
            .section h2 { border-left: 4px solid #007bff; padding-left: 10px; }
            .skills span { background: #007bff; color: white; padding: 5px 10px; margin: 5px; border-radius: 5px; display: inline-block; }
        </style>
    <h1>About Me</h1>
    <p>I am a beginner web developer learning Python and Flask.</p>
    <p>I enjoy coding small projects and learning new things every day!</p>
    """


@app.route("/resume")
def resume():
    return nav + """
    <html>
    <head>
        <title>My Resume</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px; }
            .container { max-width: 900px; margin: auto; background: white; padding: 25px; border-radius: 10px; }
            h1, h2 { color: #333; }
            .section { margin-bottom: 25px; }
            .section h2 { border-left: 4px solid #007bff; padding-left: 10px; }
            .skills span { background: #007bff; color: white; padding: 5px 10px; margin: 5px; border-radius: 5px; display: inline-block; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>ANUBHAV KUMAR</h1>
            <p><strong>Web Developer | Programmer | Designer</strong></p>

            <div class="section">
                <h2>Contact</h2>
                <p>Email:random@gmail.com</p>
                <p>Phone: +91 1234567890</p>
                <p>Location: India</p>
            </div>

            <div class="section">
                <h2>Summary</h2>
                <p>I am a passionate developer skilled in Python, HTML, CSS, and Flask.</p>
            </div>

            <div class="section">
                <h2>Experience</h2>
                <ul>
                    <li>fresher</li>
                    
                 </ul>
            </div>

            <div class="section">
                <h2>Education</h2>
                <ul>
                    <li><strong>Bachelor of Computer Science</strong> VGU</li>
                </ul>
            </div>

            <div class="section skills">
                <h2>Skills</h2>
                <span>Python</span>
                <span>Flask</span>
                <span>HTML</span>
                <span>CSS</span>
                <span>JavaScript</span>
            </div>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    print("Starting Flask server...")
    print("Open http://127.0.0.1:5000 in your browser")
app.run(debug=True)
