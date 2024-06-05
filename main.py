#Импорт
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

#Результаты формы
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # 
        selected_image = request.form.get('image-selector')
        #print(selected_image)
        # Zadanie nr 2. Pobierz tekst
        

        # Zadanie nr 3. Pobierz pozycję tekstu
       

        # Zadanie nr 3. Pobierz kolor tekstu
        

        return render_template('index.html', 
                               # Pobierz tekst 
                               selected_image=selected_image, 

                               # Zadanie nr 2. Wyświetl tekst
                               

                               # Zadanie nr 3. Wyświetl kolor 
                               
                               
                               # Zadanie nr 3. Wyświetl pozycję tekstu

                               )
    else:
        # отображаем первое изображение по умолчанию
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
