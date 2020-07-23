import wsgiref.simple_server
import urllib.parse
import sqlite3
import http.cookies
import random

connection = sqlite3.connect('users.db')
stmt = "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
cursor = connection.cursor()
result = cursor.execute(stmt)
r = result.fetchall()
if r == []:
    exp = 'CREATE TABLE users (username,password)'
    connection.execute(exp)


def application(environ, start_response):
    headers = [('Content-Type', 'text/html; charset=utf-8')]

    path = environ['PATH_INFO']
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])
    un = params['username'][0] if 'username' in params else None
    pw = params['password'][0] if 'password' in params else None

    if path == '/register' and un and pw:
        user = cursor.execute('SELECT * FROM users WHERE username = ?', [un]).fetchall()
        if user:
            start_response('200 OK', headers)
            return ['Sorry, username {} is taken'.format(un).encode()]
        else:  # EDITED
            connection.execute('INSERT INTO users VALUES (?, ?)', [un, pw])
            connection.commit()
            headers.append(('Set-Cookie', 'session={}:{}'.format(un, pw)))
            start_response('200 OK', headers)
            return ['Username {} was successfully registered'.format(un).encode()]

    elif path == '/login' and un and pw:
        user = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [un, pw]).fetchall()
        if user:
            headers.append(('Set-Cookie', 'session={}:{}'.format(un, pw)))
            start_response('200 OK', headers)
            return ['User {} successfully logged in. <a href="/account">Account</a>'.format(un).encode()]
        else:
            start_response('200 OK', headers)
            return ['Incorrect username or password'.encode()]

    elif path == '/logout':
        headers.append(('Set-Cookie', 'session=0; expires=Thu, 01 Jan 1970 00:00:00 GMT'))
        start_response('200 OK', headers)
        return ['Logged out. <a href="/">Login</a>'.encode()]

    elif path == '/account':
        start_response('200 OK', headers)

        if 'HTTP_COOKIE' not in environ:
            return ['Not logged in <a href="/">Login</a>'.encode()]

        cookies = http.cookies.SimpleCookie()
        cookies.load(environ['HTTP_COOKIE'])
        if 'session' not in cookies:
            return ['Not logged in <a href="/">Login</a>'.encode()]

        [un, pw] = cookies['session'].value.split(':')
        user = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [un, pw]).fetchall()

        # This is where the game begins. This section of is code only executed if the login form works, and if the
        # user is successfully logged in
        if user:
            correct = 0
            wrong = 0

            cookies = http.cookies.SimpleCookie()
            if 'HTTP_COOKIE' in environ:
                # [INSERT CODE FOR COOKIES HERE]
                [correct, wrong] = cookies['score'].value.split(':')

            page = '<!DOCTYPE html><html><head><title>Multiply with Score</title></head><body>'
            if 'factor1' in params and 'factor2' in params and 'answer' in params:
                # [INSERT CODE HERE. If the answer is right, show the ìcorrectî message. If itís wrong, show the ìwrongî message.]
                factor1 = params['factor1'][0]
                factor2 = params['factor2'][0]
                ans = params['answer'][0]
                if (int(factor1) * int(factor2)) == ans:
                    page = page + "<p style='background-color: lightgreen'>'Correct, {} x {} = {}'.format(factor1,factor2,ans)</p>"
                    correct += 1
                else:
                    page += "<p style='background-color: red'>'Incorrect'</p>"
                    wrong += 1

            elif 'reset' in params:
                correct = 0
                wrong = 0

            headers.append(('Set-Cookie', 'score={}:{}'.format(correct, wrong)))

            f1 = random.randrange(10) + 1
            f2 = random.randrange(10) + 1

            page = page + '<h1>What is {} x {}</h1>'.format(f1, f2)

            # [INSERT CODE HERE. Create a list that stores f1*f2 (the right answer) and 3 other random answers]
            lst = []
            ans = f1 * f2
            lst.append(ans)
            for i in range(3):
                num = random.randrange(100) + 1
                lst.append(num)
            random.shuffle(lst)

            hyperlink = '<a href="/account?username={}&amp;password={}&amp;factor1={}&amp;factor2={}&amp;answer={}">{}: {}</a><br>'

            # [INSERT CODE HERE. Create the 4 answer hyperlinks here using string formatting.]
            a = hyperlink.format(un, pw, f1, f2, ans, 'A', lst[0])
            b = hyperlink.format(un, pw, f1, f2, ans, 'B', lst[1])
            c = hyperlink.format(un, pw, f1, f2, ans, 'C', lst[2])
            d = hyperlink.format(un, pw, f1, f2, ans, 'D', lst[3])
            page += '''{}<br>{}<br>{}<br>{}<br>'''.format(a,b,c,d)

            page += '''<h2>Score</h2>
            Correct: {}<br>
            Wrong: {}<br>
            <a href="/account?reset=true">Reset</a>
            </body></html>'''.format(correct, wrong)

            return [page.encode()]
        else:
            return ['Not logged in. <a href="/">Login</a>'.encode()]

    elif path == '/':
        start_response('200 OK', headers)
        # [INSERT CODE HERE. Create the two forms, one to login, the other to register a new account]
        page = '''
        <html>
        <head><title>Log in/Sign up</title></head>
        <body>
        <h1>Log in</h1>
        <form action="/login">
        Username <input type='text' name='username'><br>
        Password <input type='text' name='password'><br>
        <input type='submit' value='Log in'>
        </form>
        <hr>
        <h1>Sign Up</h1>
        <form action="/register">
        Username <input type='text' name='Username'><br>
        Password <input type='text' name='Password'><br>
        <input type='submit' value='Register'
        </form>
        <hr>
        <p>PATH_INFO: {}</p>
        <p>QUERY_STRING: {}</p>
        </body>
        </html>'''.format(environ['PATH_INFO'], environ['QUERY_STRING'])

        return [page.encode()]

    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()
