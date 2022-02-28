from hashlib import new
from urllib import response
import requests
from  flask import Flask, jsonify
from bs4 import BeautifulSoup as bs
import json, random, string

from config import PORT
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return '''
	            <!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8">
      <h1 class="project-name">Welcome to Baby Name API 👶🍼</h1>
      <h2 class="project-tagline">An API which returns Baby Names</h2
<h2 id="usage">Usage:</h2>
<ul>
<p>The Endpoints Of The API</p>
  <li><code class="language-plaintext highlighter-rouge">/A</c ode> will return all names with meanings starting with the letter A</li>
   <li><code class="language-plaintext highlighter-rouge">/B</c ode> will return all names with meanings starting with the letter B</li>
     <li><code class="language-plaintext highlighter-rouge">/C</c ode> will return all names with meanings starting with the letter C</li>
   <li><code class="language-plaintext highlighter-rouge">/D</c ode> will return all names with meanings starting with the letter D</li>
     <li><code class="language-plaintext highlighter-rouge">/E</c ode> will return all names with meanings starting with the letter E</li>
   <li><code class="language-plaintext highlighter-rouge">/F</c ode> will return all names with meanings starting with the letter F</li>
     <li><code class="language-plaintext highlighter-rouge">/G</c ode> will return all names with meanings starting with the letter G</li>
   <li><code class="language-plaintext highlighter-rouge">/H</c ode> will return all names with meanings starting with the letter H</li>
     <li><code class="language-plaintext highlighter-rouge">/I</c ode> will return all names with meanings starting with the letter I</li>
   <li><code class="language-plaintext highlighter-rouge">/J</c ode> will return all names with meanings starting with the letter J</li>
     <li><code class="language-plaintext highlighter-rouge">/K</c ode> will return all names with meanings starting with the letter K</li>
   <li><code class="language-plaintext highlighter-rouge">/L</c ode> will return all names with meanings starting with the letter L</li>
     <li><code class="language-plaintext highlighter-rouge">/M</c ode> will return all names with meanings starting with the letter M</li>
   <li><code class="language-plaintext highlighter-rouge">/N</c ode> will return all names with meanings starting with the letter N</li>
     <li><code class="language-plaintext highlighter-rouge">/O</c ode> will return all names with meanings starting with the letter O</li>
   <li><code class="language-plaintext highlighter-rouge">/P</c ode> will return all names with meanings starting with the letter P</li>
     <li><code class="language-plaintext highlighter-rouge">/Q</c ode> will return all names with meanings starting with the letter Q</li>
   <li><code class="language-plaintext highlighter-rouge">/R</c ode> will return all names with meanings starting with the letter R</li>
     <li><code class="language-plaintext highlighter-rouge">/S</c ode> will return all names with meanings starting with the letter S</li>
   <li><code class="language-plaintext highlighter-rouge">/T</c ode> will return all names with meanings starting with the letter T</li>
     <li><code class="language-plaintext highlighter-rouge">/U</c ode> will return all names with meanings starting with the letter U</li>
   <li><code class="language-plaintext highlighter-rouge">/V</c ode> will return all names with meanings starting with the letter V</li>
     <li><code class="language-plaintext highlighter-rouge">/W</c ode> will return all names with meanings starting with the letter W</li>
   <li><code class="language-plaintext highlighter-rouge">/X</c ode> will return all names with meanings starting with the letter X</li>
     <li><code class="language-plaintext highlighter-rouge">/Y</c ode> will return all names with meanings starting with the letter Y</li>
   <li><code class="language-plaintext highlighter-rouge">/Z</c ode> will return all names with meanings starting with the letter Z</li>
   <li><code class="language-plaintext highlighter-rouge">/Random</c ode> will return random names with meanings</li>
</ul>
    </main>
  </body>
</html>
 '''

@app.route('/A', methods=['GET'])
def letter_a():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/A/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/B', methods=['GET'])
def letter_b():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/B/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/C', methods=['GET'])
def letter_c():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/C/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/D', methods=['GET'])
def letter_d():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/D/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/E', methods=['GET'])
def letter_e():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/E/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/F', methods=['GET'])
def letter_f():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/F/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/G', methods=['GET'])
def letter_g():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/G/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/H', methods=['GET'])
def letter_h():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/H/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/I', methods=['GET'])
def letter_i():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/I/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/J', methods=['GET'])
def letter_j():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/J/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/K', methods=['GET'])
def letter_k():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/k/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/L', methods=['GET'])
def letter_l():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/L/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/M', methods=['GET'])
def letter_m():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/M/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/N', methods=['GET'])
def letter_n():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/N/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/O', methods=['GET'])
def letter_o():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/O/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/P', methods=['GET'])
def letter_p():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/P/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/Q', methods=['GET'])
def letter_q():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/Q/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/R', methods=['GET'])
def letter_r():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/R/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/S', methods=['GET'])
def letter_s():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/S/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/T', methods=['GET'])
def letter_t():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/T/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/U', methods=['GET'])
def letter_u():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/U/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/v', methods=['GET'])
def letter_v():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/V/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/W', methods=['GET'])
def letter_w():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/W/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/X', methods=['GET'])
def letter_x():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/X/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/Y', methods=['GET'])
def letter_y():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/Y/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/Z', methods=['GET'])
def letter_z():
    url = F"https://parenting.firstcry.com/baby-names/starting-with/Z/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

@app.route('/Random', methods=['GET'])
def Random():
    length = int(1) 
    upper = string.ascii_lowercase
    data = random.sample(upper,length)
    keyword = "".join(data)
    url = F"https://parenting.firstcry.com/baby-names/starting-with/{keyword}/"
    baby_list = []

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
        name = name.text.strip()
        meaning = meaning.text.strip() 

        Baby_Name = {
        'Baby_Name': name,
        'Meaning': meaning,
        }

        baby_list.append(Baby_Name)
        New_List = json.dumps(baby_list, indent =2)
        with open("baby.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))  

    return jsonify(baby_list)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port= PORT)    
