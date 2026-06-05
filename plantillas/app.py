import web

urls = (
    '/', 'Index',
    '/clientes', 'Clientes',
    '/productos', 'Productos',
    '/usuarios', 'usuarios'
)
app = web.application(urls, globals())


class Index:
    def GET(self):
        return render.index()
    
class Clientes:
    def GET(self):
        return render.Clientes()
    
class Productos:
    def GET(self):
        return render.Productos()

class usuarios:
    def GET(self):
        return render.usuarios()

if __name__ == "__main__":
    app.run() 