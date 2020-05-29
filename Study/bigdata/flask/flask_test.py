from flask import Flask, request, session, render_template, redirect, url_for, make_response
app = Flask(__name__)
#
# users = {'id': 'admin', 'pwd': '1234'}
#
#
# @app.route('/')
# def root_world():
#     result = 'root world'
#     return result
#
#
# @app.route('/admin/<userid>')
# def admin(userid):
#     result = userid
#     return userid
#
#
# @app.route('/guest/<guest>')
# def guest(guest):
#     result = f'hello {guest} as guest.'
#     return result
#
#
# @app.route('/users/<userid>')
# def users(userid):
#     if userid == 'admin':
#         return redirect(url_for('admin'), userid='admin')
#     else:
#         return redirect(url_for('guest'), guest=userid)
#
#
# @app.route('/login_form_get')
# def login_form_get():
#     return render_template('login_form_get.html')
#
#
# @app.route('/login_get_proc', methods=['GET'])
# def login_get_proc():
#     user_id = request.args.get('user_id')
#     user_pwd = request.args.get('user_pwd')
#     if not len(user_id) or not len(user_pwd):
#         return '잘못된 접근'
#     return f'{user_id}, {user_pwd}'
#
#
# @app.route('/plays')
# def plays():
#     title = 'SPORTS & GAMES'
#     games = ['갤러그', '너구리', '리니지']
#     sports = ['야구', '축구', '농구']
#     return render_template('plays/play.html', title=title, games=games, sports=sports)
#
#
# @app.route('/input_form')
# def input_form():
#     return render_template('input.html')
#
#
# @app.route('/result', methods=['POST'])
# def result():
#     if request.method == 'POST':
#         result = request.form
#         return render_template('plays/result.html', result=result)


@app.route('/')
def index():
    return render_template('cookie/setcookie.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user_id = request.form['user_id']
    resp = make_response(render_template('cookie/readcookie.html'))
    resp.set_cookie('user_id', user_id)
    return resp


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('user_id')
    return '<h1>welcome {}</h1>'.format(name)


if __name__ == '__main__':
    # root_world()
    app.debug = True
    app.run()
