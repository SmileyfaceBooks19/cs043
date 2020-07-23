import wsgiref.simple_server
import http.cookies


def application(environ, start_response):
    headers = [
        ('Content-Type', 'text/plain; charset=utf-8'),
        ('Set Cookie', 'favoriteColor=red'),
        ('Set Cookie', 'favoriteNumber=4'),
        ('Set Cookie', 'name=Jason')
    ]
    start_response('200 OK', headers)

    if 'HTTP_COOKIE' in environ:
        element = environ['HTTP_COOKIE']

        cookies = http.cookies.SimpleCookie()
        cookies.load(str(element))

        lst = ''
        for key in cookies:
            lst += str(key+': '+cookies[key].value)

        return [lst.encode()]

    else:
        start_response('404 Not Found',headers)
        return ['Status 404: Resource not found'.encode()]

httpd = wsgiref.simple_server.make_server('', 8000, application)

print("Serving on port 8000...")

httpd.serve_forever()
