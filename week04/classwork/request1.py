import requests
import threading

#response = requests.get("https://swapi.dev/api/")

#response_json = response.json()
#print(f"{response_json=}")

#print(f"{response_json['starships']=}")
#starships_response = requests.get(response_json['starships'])
#print(f'{starships_response.json()=}')
#starships = starships_response.json()['results']
#for ship in starships:
    #print(f"{ship['name']}")
    
class Request_thread(threading.Thread):

    def __init__(self, url):
        # Call the Thread class's init function
        threading.Thread.__init__(self)
        self.url = url
        self.response = {}

    def run(self):
        #print(f'URL = {self.url}')
        response = requests.get(self.url)
        # Check the status code to see if the request succeeded.
        if response.status_code == 200:
            self.response = response.json()
        else:
            print('RESPONSE = ', response.status_code)
            exit()

t = Request_thread("https://swapi.dev/api/starships")
t.start()

# you would want to start all the threads before joining

t.join()
print(f'{t.response}')