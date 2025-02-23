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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
