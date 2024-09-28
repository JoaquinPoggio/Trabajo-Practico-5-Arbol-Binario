class Nodo:
    def __init__(self, nombre_criatura, derrotado_por, descripcion=""):
        self.nombre_criatura = nombre_criatura
        self.derrotado_por = derrotado_por
        self.descripcion = descripcion
        self.capturada = None
        self.izq = None
        self.der = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre_criatura, derrotado_por, descripcion=""):
        if self.raiz is None:
            self.raiz = Nodo(nombre_criatura, derrotado_por, descripcion)
        else:
            self._insertar(self.raiz, nombre_criatura, derrotado_por, descripcion)

    def _insertar(self, nodo, nombre_criatura, derrotado_por, descripcion):
        if nombre_criatura < nodo.nombre_criatura:
            if nodo.izq is None:
                nodo.izq = Nodo(nombre_criatura, derrotado_por, descripcion)
            else:
                self._insertar(nodo.izq, nombre_criatura, derrotado_por, descripcion)
        else:
            if nodo.der is None:
                nodo.der = Nodo(nombre_criatura, derrotado_por, descripcion)
            else:
                self._insertar(nodo.der, nombre_criatura, derrotado_por, descripcion)

    def listado_inorden(self):
        criaturas = []
        self._listado_inorden(self.raiz, criaturas)
        print("\n Listado en orden de criaturas y quienes las derrotaron:")
        for criatura in criaturas:
            print(f"{criatura[0]} - Derrotado por: {criatura[1]}")

    def _listado_inorden(self, nodo, criaturas):
        if nodo:
            self._listado_inorden(nodo.izq, criaturas)
            criaturas.append((nodo.nombre_criatura, nodo.derrotado_por))
            self._listado_inorden(nodo.der, criaturas)

    def modificar_descripcion(self, nombre_criatura, descripcion):
        nodo = self.buscar(nombre_criatura)
        if nodo:
            nodo.descripcion = descripcion
            print(f"\n Descripción de {nombre_criatura} modificada.")
        else:
            print("Criatura no encontrada.")

    def mostrar_informacion(self, nombre_criatura):
        nodo = self.buscar(nombre_criatura)
        if nodo:
            print(f"Criatura: {nodo.nombre_criatura}")
            print(f"Derrotado por: {nodo.derrotado_por}")
            print(f"Descripción: {nodo.descripcion}")
            print(f"Capturada: {nodo.capturada if nodo.capturada else 'No capturada'}")
        else:
            print("Criatura no encontrada.")

    def contar_derrotas(self):
        derrotas = {}
        self._contar_derrotas(self.raiz, derrotas)
        top_3 = sorted(derrotas.items(), key=lambda item: item[1], reverse=True)[:3]
        print("\n Los 3 héroes o dioses que derrotaron mayor cantidad de criaturas:")
        for heroe, cantidad in top_3:
            print(f"\n {heroe}: {cantidad} criaturas")

    def _contar_derrotas(self, nodo, derrotas):
        if nodo:
            if nodo.derrotado_por not in derrotas:
                derrotas[nodo.derrotado_por] = 0
            derrotas[nodo.derrotado_por] += 1
            self._contar_derrotas(nodo.izq, derrotas)
            self._contar_derrotas(nodo.der, derrotas)

    def criaturas_derrotadas_por(self, nombre_heroe):
        criaturas = []
        self._criaturas_derrotadas_por(self.raiz, nombre_heroe, criaturas)
        print(f"\n Criaturas derrotadas por {nombre_heroe}:")
        for criatura in criaturas:
            print(criatura)

    def _criaturas_derrotadas_por(self, nodo, nombre_heroe, criaturas):
        if nodo:
            if nodo.derrotado_por == nombre_heroe:
                criaturas.append(nodo.nombre_criatura)
            self._criaturas_derrotadas_por(nodo.izq, nombre_heroe, criaturas)
            self._criaturas_derrotadas_por(nodo.der, nombre_heroe, criaturas)

    def criaturas_no_derrotadas(self):
        criaturas = []
        self._criaturas_no_derrotadas(self.raiz, criaturas)
        print("\n Criaturas que no han sido derrotadas:")
        for criatura in criaturas:
            print(criatura)

    def _criaturas_no_derrotadas(self, nodo, criaturas):
        if nodo:
            if nodo.derrotado_por == "-":
                criaturas.append(nodo.nombre_criatura)
            self._criaturas_no_derrotadas(nodo.izq, criaturas)
            self._criaturas_no_derrotadas(nodo.der, criaturas)

    def capturar_criatura(self, nombre_criatura, nombre_heroe):
        nodo = self.buscar(nombre_criatura)
        if nodo:
            nodo.capturada = nombre_heroe
            print(f"\n {nombre_criatura} ha sido capturada por {nombre_heroe}.")
        else:
            print("\n Criatura no encontrada.")

    def atrapar_criaturas(self, criaturas):
        for criatura in criaturas:
            self.capturar_criatura(criatura, "Heracles")

    def buscar(self, nombre_criatura):
        return self._buscar(self.raiz, nombre_criatura)

    def _buscar(self, nodo, nombre_criatura):
        if nodo is None or nodo.nombre_criatura == nombre_criatura:
            return nodo
        if nombre_criatura < nodo.nombre_criatura:
            return self._buscar(nodo.izq, nombre_criatura)
        else:
            return self._buscar(nodo.der, nombre_criatura)

    def eliminar(self, nombre_criatura):
        self.raiz = self._eliminar(self.raiz, nombre_criatura)

    def _eliminar(self, nodo, nombre_criatura):
        if nodo is None:
            return nodo
        if nombre_criatura < nodo.nombre_criatura:
            nodo.izq = self._eliminar(nodo.izq, nombre_criatura)
        elif nombre_criatura > nodo.nombre_criatura:
            nodo.der = self._eliminar(nodo.der, nombre_criatura)
        else:
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            temp = self._minimo(nodo.der)
            nodo.nombre_criatura, nodo.derrotado_por = temp.nombre_criatura, temp.derrotado_por
            nodo.der = self._eliminar(nodo.der, temp.nombre_criatura)
        return nodo

    def _minimo(self, nodo):
        while nodo.izq is not None:
            nodo = nodo.izq
        return nodo

    def modificar_aves_estinfalo(self, nuevo_texto):
        nodo = self.buscar("Aves del Estínfalo")
        if nodo:
            nodo.derrotado_por = nuevo_texto
            print("\n Descripción de Aves del Estínfalo modificada.")
        else:
            print("\n Criatura no encontrada.")

    def modificar_nombre_ladon(self, nuevo_nombre):
        nodo = self.buscar("Ladón")
        if nodo:
            nodo.nombre_criatura = nuevo_nombre
            print("\n Nombre de la criatura Ladón modificado a Dragón Ladón.")
        else:
            print("Criatura no encontrada.")

    def listado_por_nivel(self):
        niveles = {}
        self._listado_por_nivel(self.raiz, niveles, 0)
        for nivel, criaturas in niveles.items():
            print(f"Nivel {nivel}: {criaturas}")

    def _listado_por_nivel(self, nodo, niveles, nivel):
        if nodo:
            if nivel not in niveles:
                niveles[nivel] = []
            niveles[nivel].append(nodo.nombre_criatura)
            self._listado_por_nivel(nodo.izq, niveles, nivel + 1)
            self._listado_por_nivel(nodo.der, niveles, nivel + 1)

    def criaturas_capturadas_por(self, nombre_heroe):
        criaturas = []
        self._criaturas_capturadas_por(self.raiz, nombre_heroe, criaturas)
        print(f"Criaturas capturadas por {nombre_heroe}:")
        for criatura in criaturas:
            print(criatura)

    def _criaturas_capturadas_por(self, nodo, nombre_heroe, criaturas):
        if nodo:
            if nodo.capturada == nombre_heroe:
                criaturas.append(nodo.nombre_criatura)
            self._criaturas_capturadas_por(nodo.izq, nombre_heroe, criaturas)
            self._criaturas_capturadas_por(nodo.der, nombre_heroe, criaturas)

arbol = ArbolBinarioBusqueda()

criaturas = [
    ("Ceto", "-"),
    ("Tifón", "Zeus"),
    ("Equidina", "Argos Panoptes"),
    ("Dino", "-"),
    ("Pefredo", "-"),
    ("Enio", "Gerión"),
    ("Escila", "Cloto"),
    ("Caribdis", "Láquesis"),
    ("Eurialé", "-"),
    ("Esteno", "Perseo"),
    ("Medusa", "Perseo"),
    ("Ladón", "Heracles"),
    ("Águila del Cáucaso", "Belerofonte"),
    ("Quimera", "Belerofonte"),
    ("Hidra de Lerna", "Heracles"),
    ("León de Nemea", "Heracles"),
    ("Esfinge", "Edipo"),
    ("Dragón de la Cólquida", "-"),
    ("Cerbero", "-"),
    ("Cerda de Crómion", "Teseo"),
    ("Toro de Creta", "Teseo"),
    ("Jabalí de Calidón", "Atalanta"),
    ("Carcinos", "-"),
    ("Minotauro de Creta", "Teseo"),
    ("Argos Panoptes", "Hermes"),
    ("Aves del Estínfalo", "-"),
    ("Sirenas", "-"),
    ("Pitón", "Apolo"),
    ("Cierva de Cerinea", "-"),
    ("Basilisco", "-"),
    ("Jabalí de Erimanto", "-"),
]

for criatura, derrotado in criaturas:
    arbol.insertar(criatura, derrotado)

arbol.listado_inorden()
arbol.modificar_descripcion("Cerbero", "Perro de tres cabezas que guarda la entrada del inframundo.")
arbol.mostrar_informacion("Talos")
arbol.contar_derrotas()
arbol.criaturas_derrotadas_por("Heracles")
arbol.criaturas_no_derrotadas()
arbol.atrapar_criaturas(["Cerbero", "León de Nemea", "Hidra de Lerna"])
arbol.listado_por_nivel()
arbol.criaturas_capturadas_por("Heracles")
arbol.eliminar("Basilisco")
arbol.eliminar("Sirenas")
arbol.modificar_aves_estinfalo("Heracles")
arbol.modificar_nombre_ladon("Dragón Ladón")

