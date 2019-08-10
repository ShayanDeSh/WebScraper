import requests as request
from bs4 import BeautifulSoup
import os as os


class ImdbScraper:

    @staticmethod
    def get_movies():
        html = request.get('https://www.imdb.com/chart/top').text
        soup = BeautifulSoup(html, 'html5lib')
        soup.prettify()
        all_movies_full_td = soup.find_all('td', {'class': 'titleColumn'})
        all_movies_stripped = [
            ' '.join(td.text.strip().replace('\n', '').replace(':', '').split()[1:]) for td in all_movies_full_td]
        print(all_movies_stripped)
        return all_movies_stripped

    @staticmethod
    def make_imdb_folder(path):
        if not os.path.exists(path):
            os.makedirs(path)
            movies = ImdbScraper.get_movies()
            for i in range(movies.__len__()):
                movie_path = path + "\\" + (i + 1).__str__() + '. ' + movies[i]
                os.makedirs(movie_path)
        else:
            print('This Path already exists')

    @staticmethod
    def update_imdb_folder(path):
        if os.path.exists(path):
            movies = ImdbScraper.get_movies()
            files_list = os.listdir(path)
            for i in range(movies.__len__()):
                found = False
                for j in range(files_list.__len__()):
                    if files_list[j].__contains__(movies[i]):
                        found = not found
                        if files_list[j].split()[0] == (i + 1).__str__() + ".":
                            break
                        else:
                            new_name = path + "\\" + (i + 1).__str__() + '. ' + movies[i]
                            os.rename(path + '\\' + files_list[j], new_name)
                            print('Renamed: ' + files_list[j] + ' To ' + (i + 1).__str__() + '. ' + movies[i])
                if not found:
                    movie_path = path + "\\" + (i + 1).__str__() + '. ' + movies[i]
                    os.makedirs(movie_path)
                    print('Created: ' + (i + 1).__str__() + '. ' + movies[i])


# Imdb_Scraper.get_movies()
# ImdbScraper.make_imdb_folder('C:\\Users\\NothingRealm\\Desktop\\IMDB')
ImdbScraper.update_imdb_folder('C:\\Users\\NothingRealm\\Desktop\\IMDB')
