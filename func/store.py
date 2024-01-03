import requests

#Tests with the module requests and the fakeapi of platzi
def get_categories():
    r = requests.get("https://api.escuelajs.co/api/v1/categories")

    status = r.status_code #This brings the status of the api
    
    categories = r.json() #This get the data of the api like a json format
    
    for category in categories:
        print(category["name"])