import eel

eel.init('web')
@eel.expose
def say_hello_py(x):
    print('Hello %s' % x)
say_hello_py('Python World!')
eel.say_hello_js('Python World!')
eel.start('helloworld.html', size=(300, 200))