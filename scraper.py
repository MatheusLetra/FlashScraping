from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from unidecode import unidecode
from webdriver_manager.chrome import ChromeDriverManager

def scrape_results():
    # Iniciando o WebDriver
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://www.flashscore.com.br/")

    # Aceitando cookies
    accept_cookies = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    accept_cookies.click()

    # Interagindo com a página
    live_matches = driver.find_element(By.XPATH, '//*[@id="live-table"]/div[1]/div/div[2]')
    live_matches.click()

    matches_table = driver.find_element(By.XPATH, '//*[@id="live-table"]/section/div/div')
    html_content = matches_table.get_attribute('outerHTML')

    # Usando BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Capturando os dados dos times e resultados
    home_teams = soup.find_all("div", class_='event__homeParticipant')
    away_teams = soup.find_all("div", class_='event__awayParticipant')
    score_home_teams = soup.find_all("div", class_='event__score--home')
    score_away_teams = soup.find_all("div", class_='event__score--away')
    stages = soup.find_all("div", class_='event__stage--block')

    # Listando os jogos
    matches_list = []
    for index in range(len(home_teams)):
        championship_info = home_teams[index].find_previous("div", class_="event__titleBox")
        if championship_info:
            championship = championship_info.find("a").get_text(strip=True)
        else:
            championship = "Desconhecido"

        matches_list.append({
            "Home": unidecode(home_teams[index].get_text(strip=True)),
            "Score_Home": score_home_teams[index].get_text(strip=True),
            "Score_Away": score_away_teams[index].get_text(strip=True),
            "Away": unidecode(away_teams[index].get_text(strip=True)),
            "Minutagem": stages[index].get_text(strip=True),
            "Championship": unidecode(championship)
        })

    # Fechando o driver
    driver.quit()

    return matches_list
