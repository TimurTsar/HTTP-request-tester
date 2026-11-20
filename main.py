#this is my third lab work. Today i'm gonna make HTTP Request Tester. Thank you and enjoy! :)

import requests

def pairs(dictionary): 
    hm = int(input('HOW MANY PAIRS?: '))
    for i in range(hm):
        key = input("KEY: ")
        value = input('VALUE: ')
        dictionary[key] = value
    return dictionary 

def response_analyze(method,response): #DRY function
    print(str(method)+' REQUEST CONFIRMED...')
    print('URL: '+str(response.url))
    print('STATUS CODE: '+str(response.status_code))
    print('HEADERS: '+str(response.headers))
    print('RESPONSE BODY: '+str(response.text))
    print('TIME: '+str(response.elapsed))



print('===========================================HTTP-REQUEST-TESTER===========================================')
print('GET\nPOST\nPUT\nPATCH\nDELETE')
method = input('CHOOSE THE METHOD: ').upper()
url = input('CHOOSE THE URL: ')

print('SELECTED METHOD: '+method)
print('SELECTED URL: '+url)

#######

methods = ['GET','POST','PUT','PATCH','DELETE']
if method in methods:
    print('METHOD CONFIRMED...')
    if url.startswith('http://') or url.startswith('https://'): #urls without http(s) are forbidden
        print('URL CONFIRMED...')
        if method == 'GET':
            try: #get method
                response = requests.get(url, timeout=5)
                response_analyze(method, response=response)
                
                
            except requests.exceptions.RequestException as e:
                print('ERROR: '+str(e))
        elif method == 'POST':
            try: #post method
                print("POST REQUEST CONFIRMED...")
                dictionary = {}
                pairs(dictionary)
                dj = input('(DATA / JSON?): ').upper()
                if dj == 'DATA': #post method with data
                    print('DATA CONFIRMED...')
                    response = requests.post(url=url, data=dictionary, timeout=5)
                    response_analyze(method=method,response=response)
                elif dj == 'JSON': #post method with json
                    response = requests.post(url=url, json=dictionary, timeout=5)
                    response_analyze(method=method, response=response)
                else:
                    print('UNKNOWN TYPE!')
                    exit()
            except requests.exceptions.RequestException as e:
                print('ERROR: '+str(e))
            except ValueError:
                print('VALUE MUST BE INTEGER!')
                exit()
        elif method == 'PUT':
            try: #put method
                print('PUT REQUEST CONFIRMED...')
                dictionary = {}
                pairs(dictionary=dictionary)
                way = input('DATA / JSON?: ').upper()
                if way == 'DATA': #put, data
                    response = requests.put(url=url, data=dictionary, timeout=5)
                    response_analyze(method=method, response=response)
                elif way == 'JSON': #put, json
                    response = requests.put(url=url, json=dictionary, timeout=5)
                    response_analyze(method=method, response=response)
                else:
                    print('UNKNOWN TYPE!')
                    exit()

            except requests.exceptions.RequestException as e:
                print('ERROR: '+str(e))
                exit()
            except ValueError:
                print('VALUE MUST BE INTEGER!')
                exit()
        elif method == 'PATCH':
            try: #patch
                print('PATCH METHOD CONFIRMED...')
                dictionary = {}
                pairs(dictionary=dictionary)
                way = input('DATA / JSON?: ').upper()
                if way == 'DATA': #patch, data 
                    response = requests.patch(url=url, data=dictionary, timeout=5)
                    response_analyze(method=method, response=response)
                elif way == 'JSON': #patch, json
                    response = requests.patch(url=url, timeout=5, json=dictionary)
                    response_analyze(response=response, method=method)
                else:
                    print('UNKNOWN TYPE!')
                    exit()
            except requests.exceptions.RequestException as e:
                print('ERROR: '+str(e))
                exit()
            except ValueError:
                print('VALUE MUST BE INTEGER!')
                exit()
        elif method == 'DELETE':
            try: #delete method
                print('DELETE METHOD CONFIRMED...')
                response = requests.delete(url=url, timeout=5)
                response_analyze(method=method, response=response)
            except requests.exceptions.RequestException as e:
                print('ERROR: '+str(e))
        else:
            print('UNKNOWN METHOD!')
            exit()

    else:
        print('ERROR! URL IS NOT CONFIRMED. IT MUST BE STARTED WITH HTTP OR HTTPS\nEXIT...')
        exit()

elif method not in methods:
    print('ERROR! SELECTED METHOD DOES NOT EXIST!')
    exit()


#this is my third project. Thank you for your attention and enjoy! :)