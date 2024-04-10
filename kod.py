from bs4 import BeautifulSoup
import requests

url = 'https://www.chess.com/pl/article/view/10-najlepszych-szachistow-wszech-czasow'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

section = soup.find_all('div', class_='post-view-content')[0]

imiona = section.find_all('li')
clean_text = []

for item in range(4,14):
    text = imiona[item].get_text()
    print(text)
    clean_text += text.split()[1:]
    #clean_text = ' '.join(text.split()[1:])

print(clean_text)

wstep = section.find_all('p')
opis_full = ''

for item in range(4):
    text = wstep[item].get_text()
    opis_full = opis_full + text

with open('index.md', 'w', encoding='utf-8') as file:
    file.write("Witaj na stronie dedykowanej najlepszym szachistom! Stworzyłem ją z fascynacji talentem i umiejętnościami mistrzów szachowych oraz z pasji do samej gry. Jestem głęboko przekonany, że warto poznać historię i osiągnięcia tych niezwykłych graczy, którzy inspirują i podnoszą poprzeczkę dla kolejnych pokoleń szachistów. Szachy to nie tylko gra, to także nauka, kreatywność i wyzwanie umysłowe. Dlatego zgłębianie informacji o najlepszych szachistach może być nie tylko źródłem wiedzy na temat samej gry, ale także inspiracją do rozwoju umiejętności intelektualnych i strategicznych. Ta strona powstała przy użyciu techniki web scrappingu jako część mojego projektu z przedmiotu 'Aplikacje WWW'. Zapraszam do odkrywania świata szachów i poznawania historii oraz osiągnięć ich mistrzów!")
    file.write("TUTAJ ZNAJDZIESZ 10 NAJLEPSZYCH szachistówwszech czasów - [Lista Szachistów](szachisci.md)\n")

with open('szachisci.md', 'w', encoding='utf-8') as file:
    file.write(opis_full)
    for i in clean_text:
      file.write(i +"\n")

