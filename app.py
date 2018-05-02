from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('webscrapingHomepage.html')

@app.route("/<language>")
def otherLanguage(language):
    otherLanguageTrending = requests.get('http://github.com/trending/' + language).text
    soup = BeautifulSoup(otherLanguageTrending, 'lxml')

    projectDescriptions=[]

    for project in soup.find_all('li', class_="col-12 d-block width-full py-4 border-bottom"):
        projectDescriptions.append(project)

    return render_template('index.html', projectDescriptions=projectDescriptions, language=language)

if __name__ == "__main__":
    app.run()
