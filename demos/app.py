import web

urls = (
    '/', 'Index',
    '/clientes', 'Clientes',
    '/productos', 'Productos',
    '/usuarios', 'usuarios'
)
app = web.application(urls, globals())
render = web.template.render('templates')


class Index:
    def GET(self):
        return render.index()
    
class Clientes:
    def GET(self):
        return render.clientes()
    
class Productos:
    def GET(self):
        return render.productos()

class usuarios:
    def GET(self):
        return render.usuarios()

if __name__ == "__main__":
    app.run() 