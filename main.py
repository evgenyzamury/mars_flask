from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def page():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    site = ['Человечество вырастает из детства.',
            'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.',
            'И начнем с Марса!',
            'Присоединяйся!', ]
    return '<br>'.join(site)


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/MARS.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                        <p>Вот она какая, красная планета.</p>
                  </body>
                </html>'''


@app.route('/promotion_image')
def promotion_image():
    return f"""
    <!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/MARS.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-dark" role="alert">
                      Человечество выростет из детсва.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнём с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>
"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    print(request.method)
    if request.method == 'GET':
        return f"""
                     <!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <h2 align='center'>Анкета претендента</h2>
                                <h3 align='center'>на участие в миссии</h3>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                        <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                        <br>
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование?</label>
                                            <select class="form-control" id="educationSelect" name="education">
                                              <option>Начальное</option>
                                              <option>Среднее</option>
                                              <option>Высшее</option>
                                              <option>Послевузовское</option>
                                            </select>
                                         </div>
                                         <br>
                                         <div class="form-group">
                                            <label for="professions">Какие у вас есть профессии?</label>
                                            <div class="professions">
                                                <input type="checkbox" class="selectProfessions" name="prof" value="prof" id="proff1">
                                                <label for="proff1">Инженер-исследователь</label>
                                            </div>
                                            <div class="professions">
                                                <input type="checkbox" class="selectProfessions" name="prof" value="prof" id="proff2">
                                                <label for="proff2">Инженер-строитель</label>
                                            </div>
                                            <div class="professions">
                                                <input type="checkbox" class="selectProfessions" name="prof" value="prof" id="proff3">
                                                <label for="proff3">Пилот</label>
                                            </div>
                                            <div class="professions">
                                                <input type="checkbox" class="selectProfessions" name="prof" value="prof" id="proff4">
                                                <label for="proff4">Метеоролог</label>
                                            </div>
                                            <div class="professions">
                                                <input type="checkbox" class="selectProfessions" name="prof" value="prof" id="proff5">
                                                <label for="proff5">Инженер по жизнеобеспечению</label>
                                            </div>
                                            <div class="professions">
                                                <input type="checkbox" class="selectProfessions" name="prof" value="prof" id="proff6">
                                                <label for="proff6">Инженер по радиационной защите</label>
                                            </div>
                                            <div class="professions">
                                                <input type="checkbox" class="selectProfessions" name="prof" value="prof" id="proff7">
                                                <label for="proff7">Врач</label>
                                            </div>
                                            <div class="professions">
                                                <input type="checkbox" class="selectProfessions" name="prof" value="prof" id="proff8">
                                                <label for="proff8">Экзобиолог</label>
                                            </div>
                                            <br>
                                         </div>
                                         <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <br>
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <br>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <br>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>
                        """
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def planet(planet_name: str):
    if planet_name.lower() == 'марс':
        first = 'Это планета близка к Земле'
        second = 'На ней много необходимых ресурсов'
        third = 'На ней есть вода и атмосфера'
        four = 'На ней есть небольшое магнитное поле'
        five = 'Наконец, она просто красива!'
    elif planet_name.lower() == 'венера':
        first = 'Это планета близка к Земле'
        second = 'На ней очень жарко'
        third = 'На очень плотная атмосфера'
        four = 'На ней есть небольшое магнитное поле'
        five = 'Наконец, она просто красива!'
    elif planet_name.lower() == 'меркурий':
        first = 'Это планета самая близкая к Солнцу'
        second = 'На ней очень жарко'
        third = 'На сильно разряженная атмосфера'
        four = 'На ней есть небольшое магнитное поле'
        five = 'Наконец, она очень маленькая'
    elif planet_name.lower() == 'земля':
        first = 'Это планета наша родная'
        second = 'На ней очень хорошо'
        third = 'На ней хорошая атмосфера'
        four = 'На ней есть магнитное поле'
        five = 'Наконец, она живая'
    elif planet_name.lower() == 'юпитер':
        first = 'Это планета газовый гигант'
        second = 'На ней нет твёрдой поверхности'
        third = 'На ней крупнейшая атмосфера'
        four = 'Пятая планета по удалённости от Солнца'
        five = 'Наконец, она самая большая'
    elif planet_name.lower() == 'сатурн':
        first = 'Это планета газовый гигант'
        second = 'На ней нет твёрдой поверхности'
        third = 'У неё очень много спутников'
        four = 'Самая низкая плотность планеты'
        five = 'Наконец, у неё есть кольца'
    elif planet_name.lower() == 'уран':
        first = 'Это планета газовый гигант'
        second = 'На ней нет твёрдой поверхности'
        third = 'Она очень холодная'
        four = 'На ней долгие полярные день и ночь'
        five = 'Наконец, она очень красивая'
    elif planet_name.lower() == 'уран':
        first = 'Это планета газовый гигант'
        second = 'На ней нет твёрдой поверхности'
        third = 'Самая отдалённая от Солнца планета'
        four = 'На ней самые сильные ветры'
        five = 'Наконец, она планета'
    else:
        first = 'У нас нет данных этой планеты'
        second = '-----'
        third = '-----'
        four = '-----'
        five = '-----'
    return f"""
    <!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                  </head>
                  <body>
                    <h2>Мое предложение: {planet_name}</h2>
                    <h3>{first};</h3>
                    <div class="alert alert-success"><h3>{second};</h3></div>
                    <div class="alert alert-dark"><h3>{third};</h3></div>
                    <div class="alert alert-warning"><h3>{four};</h3></div>
                    <div class="alert alert-danger"><h3>{five}</h3></div>
                  </body>
                </html>
        """


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname: str, level: int, rating: float):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                  </head>
                  <body>
                    <h2>Результаты отбора</h2>
                    <h3>Претендента на участие в миссии {nickname}</h3>
                    <div class="alert-success"><br><h3>Поздравляем! Ваш рейтинг после {level} этапа отбора</h3></div>
                    <h3><br>составляет {rating}!</h3>
                    <div class="alert-warning"><br><h3>Желаем удачи!</h3></div>
                  </body>
                </html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'POST':
        with open('static/img/user.png', 'wb') as file:
            file.write(request.files['file'].read())
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                  </head>
                  <body>
                    <h2 align='center'>Загрузка фотографии</h2>
                    <h3 align='center'>для участия в миссии</h3>
                    <div>
                        <form method="post" enctype="multipart/form-data" class="login_form">
                            <div class="form-group">
                                <label for="photo">Приложите фотографию</label>
                                <input type="file" class="form-control-file" id="photo" name="file">
                            </div>
                            <br>
                            <img src={url_for('static', filename='img/user.png')}
                            alt="Ошибка отображения изображения">
                            <br>
                            <br>
                            <button type="submit" class="btn btn-primary">Отправить</button>
                        </form>
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
