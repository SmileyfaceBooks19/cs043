import wsgiref.simple_server


def application(environ, start_response):
    headers = [('Content-Type', 'text/html;charset=utf-8')]
    start_response('200 OK', headers)

    path = environ['PATH_INFO']
    if path == '/biography':
        page = '''</DOCTYPE html>
        <html>
        <h1 style='color: purple'>Shivapragna Guntupalli</h1>
        <h2>Teenage girl extraordinaire</h2>
        <i style="background-color: powderblue">Tempered<br>Passionate<br>Empathetic<br></i>
        <p>These are how those closes to Shivapragna (more commonly known as Pragna) 
        describe her.<br>She currently attends 
        <a href='https://www.dvhigh.net/'><img src='dv_school.jpg' alt="Dougherty Valley High School, San Ramon"></a>.e
        She is a diverse being in every sense of the word - musically, 
        philosophically, and in words. She often can't sort out her thoughts into 
        words - <br>
        <hr>
        <i style="background-color: powderblue"> my thoughts are constellations i cannot fathom into stars </i><br>
        <hr>
        - and often looks to poetry to help decipher the profound complexities of
        the world. Her personal favorite is Caroline Kaufman 
        (<a href="https://www.instagram.com/poeticpoison/?hl=en">@poeticpoison</a>) - <br>
        <hr>
        <i style="background-color: powderblue"> the trees write in cursive roots<br>
        that you cannot decipher.<br>
        you were promised<br>
        block-letter branches.<br>
        experience never quite matches up<br>
        to the textbook,<br>
        but remember that you<br>
        are not illiterate.<br>
        life is learning to read<br>
        the messy handwriting<br>
        of the earth<br>
        when school only showed you<br>
        clear-cut letters. </i><br>
        <hr>
        - as she writes about body image in a way Pragna understands. Being a 
        very insecure person, she takes it upon herself to encourage others in all 
        their dreams.</p>
        <p>So far, Shivapragna has no clue as of what her role as a speck 
        in the universe, but hopes with all her heart that she will find a career 
        she loves and helps people.</p>'''

        return [page.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()
