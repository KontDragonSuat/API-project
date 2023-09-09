import requests

class Moviedb:
    def __init__(self):
        self.api_url = 'https://api.themoviedb.org/3'
        self.api_key = '812e8028020c9509bacc00172843c839'

    def getPopular(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getTop(self):
        response = requests.get(f"{self.api_url}/movie/top_rated?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSeach(self,keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

movie = Moviedb()

while True:
    choice = input("Make your choice\n1 - Get Popular Movies\n2 - Get Top Movies\n3 - Search a Movie\n4 - Exit\n..: ")

    if choice == "1":
        response = movie.getPopular()
        a = 1
        for i in response['results']:
            print(f"{a} - {i['title']}")
            a = a + 1
        print()

    elif choice == "2":
        response = movie.getPopular()
        a = 1
        for i in response['results']:
            print(f"{a} - {i['title']}")
            a = a + 1
        print()

    elif choice == "3":
        search = input("Word: ")
        response = movie.getSeach(search)
        a = 1
        for i in response['results']:
            print(f"{a} - {i['name']}")
            a = a + 1
        print()

    elif choice == "4":
        break

    else:
        print("Incorrect!")
        print()