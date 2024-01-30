class Carrito:
    def __init__(self , request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"]= {}
        self.carrito=carrito

    def agregar(self,productos):
        if productos.idProducto not in self.carrito.keys():
            self.carrito[productos.idProducto]={
                "id": productos.idProducto,
                "nombreProducto":productos.nombreProducto,
                "precio":str (productos.precio),
                "descripcion":productos.descripcion,
                "cantidad":1,
                "total":productos.precio
            }
        else:
            for key, value in self.carrito.items():
                if key==productos.idProducto:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] =productos.precio
                    value["total"] = value["total"] + productos.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True

    def eliminar(self, productos):
        id = productos.idProducto
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar (self,productos):
        for key, value in self.carrito.items():
            if key == productos.idProducto:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = float(value["total"])-productos.precio
                if value["cantidad"] <1:
                    self.eliminar(productos)
                break
        self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True