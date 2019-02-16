from bottle import default_app, get, run
from beaker.middleware import SessionMiddleware

#设置session参数
session_opts = {
    'session.type': 'file',
    'session.cookie_expirse': '3600',
    'session.data_dir': '/tmp/sessions/simple',
    'session.auto': True,
}

@get('/index/')
def callback():
    return 'Hello World'

if __name__ == '__main__':
    app_argv = SessionMiddleware(default_app(), session_opts)
    run(app=app_argv, host='localhost', port=81, debug=True, reloader=True)