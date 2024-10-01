from flask import Flask, render_template
from scraper import scrape_results

app = Flask(__name__)

@app.route('/')
def home():
    matches_list = scrape_results()  # Obter os resultados dos jogos
    return render_template('index.html', matches=matches_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)