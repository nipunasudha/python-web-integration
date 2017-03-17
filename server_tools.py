from tornado.ioloop import IOLoop


def parse_command(request):
    cmd = request.form['cmd']
    data = request.form.getlist('data[]')
    commander(cmd, data)


def commander(cmd, data):
    if cmd == "EXIT":
        IOLoop.instance().stop()

    elif cmd == "PRINT":
        print("Ok, printed")
