import bottle

@bottle.route('/')
def home_page():
    return "Welcome"

@bottle.route('/testpage')
def test_page():
    return "Test page"


bottle.debug(True)
bottle.run(host='localhost', port=8080)


