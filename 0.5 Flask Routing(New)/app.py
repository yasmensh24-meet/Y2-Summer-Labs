from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return '''<html>
    <h1>welcome home</h1>
    <br/>
    <h2>click on the food photo</h2>
    <br/>
    <a href="/food">
        <img src="https://promova.com/content/mexican_food_examples_e3af752287.png" width =200 height=200>
    </a>
    <br/>
    <a href="http://127.0.0.1:5000/pet">
    <img src="https://images.ctfassets.net/m5ehn3s5t7ec/wp-image-197226/a483c1323fa18227209da8ae4d4ea0ba/Australian-Shepherd-Breed-Information.jpg"width=200 height=200>
    </a>
    <br/>
    <a href="space">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMG8XzdSjuNVV4Q2XrW1QBZwOJKlJFyDaVGg&s">
    </a>
    </html>'''
    
@app.route('/food')
def food():
    return '''<html>
    <h1>food 1</h1>
    
    <a href="http://127.0.0.1:5000/food2">
        <img src="https://promova.com/content/italian_food_words_26076fb3f5.png" width=300 height=300>
        </a>


    </html>'''

@app.route('/food2')
def food2():
    return '''<html>
    <h1>food 2</h1>
    <a href="http://127.0.0.1:5000/food3">
        <img src="https://www.tasteofhome.com/wp-content/uploads/2019/05/Fried-Ice-Cream-Dessert-Bars-_EXPS_SDJJ19_232652_B02_06_1b_rms-2.jpg"width=300 height=300>
        </a>

    </html>'''


@app.route('/food3')
def food3():
    return'''<html>
    <h1>food 3</h1>
    <a href="">
        <img src="https://thumbs.dreamstime.com/b/set-traditional-food-icons-30099902.jpg"width=300 height=300>
        </a>
    </html>'''

@app.route('/pet')
def pet():
    return'''<html>
    <h1>pet 1</h1>
    <a href="/pet2">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVL9tfVWVWLX8jiKGmbm4PhI8VGIqpM0GVxQ&s">
        </a>
    
    
    </html>'''
@app.route('/pet2')
def pet2():
    return'''<html> 
    <h1>pet2</h1>
    <a href="/pet3">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSUwHJogT3nHS07ATOwl_0wrLZ32EnVc2pdw&s">
        </a>
    </html> '''

@app.route('/pet3')
def pet3():
    return'''<html>
    <h1>pet 3</h1>
    <a href="/pet3">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7BSnxk2PA5pzymv7-5RgYRHY6DtBM2njNgg&s">
        </a>
    
    </html>'''

@app.route('/space')
def space():
    return'''<html> 
    <h1>space</h1>
    <a href="space2">
        <img src="https://prd-sc102-cdn.rtx.com/-/media/ca/product-assets/marketing/s/space/space-symposium-graphic_1920x1080.jpg?rev=2a22f490c9c644a5bf69ef3cce59813d">
        </a>
    </html> '''

@app.route('/space2')
def space2():
    return'''<html> 
    <h1>space2</h1>
    <a href="space3">
        <img src="https://starwalk.space/gallery/images/what-is-space/1920x1080.jpg">
        </a>
    </html> '''

@app.route('/space3')
def space3():
    return'''<html> 
    <h1>space3</h1>
        <img src="https://img.freepik.com/free-photo/ultra-detailed-nebula-abstract-wallpaper-4_1562-749.jpg">

    </html> '''

if __name__ == '__main__':
    app.run(debug=True)



