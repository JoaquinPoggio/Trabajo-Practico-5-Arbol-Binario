class Nodo:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe
        self.izq = None
        self.der = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, es_heroe):
        if self.raiz is None:
            self.raiz = Nodo(nombre, es_heroe)
        else:
            self._insertar(self.raiz, nombre, es_heroe)

    def _insertar(self, nodo, nombre, es_heroe):
        if nombre < nodo.nombre:
            if nodo.izq is None:
                nodo.izq = Nodo(nombre, es_heroe)
            else:
                self._insertar(nodo.izq, nombre, es_heroe)
        else:
            if nodo.der is None:
                nodo.der = Nodo(nombre, es_heroe)
            else:
                self._insertar(nodo.der, nombre, es_heroe)

    def listar_villanos(self):
        villanos = []
        self._listar_villanos(self.raiz, villanos)
        print("Villanos ordenados alfabéticamente:")
        for villano in sorted(villanos):
            print(villano)

    def _listar_villanos(self, nodo, villanos):
        if nodo:
            if not nodo.es_heroe:
                villanos.append(nodo.nombre)
            self._listar_villanos(nodo.izq, villanos)
            self._listar_villanos(nodo.der, villanos)

    def heroes_con_C(self):
        heroes = []
        self._heroes_con_C(self.raiz, heroes)
        print("Superhéroes que empiezan con 'C':")
        for heroe in heroes:
            print(heroe)

    def _heroes_con_C(self, nodo, heroes):
        if nodo:
            if nodo.es_heroe and nodo.nombre.startswith('C'):
                heroes.append(nodo.nombre)
            self._heroes_con_C(nodo.izq, heroes)
            self._heroes_con_C(nodo.der, heroes)

    def contar_heroes(self):
        return self._contar_heroes(self.raiz)

    def _contar_heroes(self, nodo):
        if nodo is None:
            return 0
        contador = 1 if nodo.es_heroe else 0
        contador += self._contar_heroes(nodo.izq)
        contador += self._contar_heroes(nodo.der)
        return contador

    def corregir_doctor_strange(self):
        self._corregir_doctor_strange(self.raiz)

    def _corregir_doctor_strange(self, nodo):
        if nodo:
            if "Strange" in nodo.nombre:
                print(f"Modificando {nodo.nombre} a 'Doctor Strange'")
                nodo.nombre = "Doctor Strange"
            self._corregir_doctor_strange(nodo.izq)
            self._corregir_doctor_strange(nodo.der)

    def listar_heroes_descendente(self):
        heroes = []
        self._listar_heroes_descendente(self.raiz, heroes)
        print("Superhéroes en orden descendente:")
        for heroe in sorted(heroes, reverse=True):
            print(heroe)

    def _listar_heroes_descendente(self, nodo, heroes):
        if nodo:
            if nodo.es_heroe:
                heroes.append(nodo.nombre)
            self._listar_heroes_descendente(nodo.izq, heroes)
            self._listar_heroes_descendente(nodo.der, heroes)

    def generar_bosque(self):
        arbol_heroes = ArbolBinarioBusqueda()
        arbol_villanos = ArbolBinarioBusqueda()
        self._generar_bosque(self.raiz, arbol_heroes, arbol_villanos)
        return arbol_heroes, arbol_villanos

    def _generar_bosque(self, nodo, arbol_heroes, arbol_villanos):
        if nodo:
            if nodo.es_heroe:
                arbol_heroes.insertar(nodo.nombre, nodo.es_heroe)
            else:
                arbol_villanos.insertar(nodo.nombre, nodo.es_heroe)
            self._generar_bosque(nodo.izq, arbol_heroes, arbol_villanos)
            self._generar_bosque(nodo.der, arbol_heroes, arbol_villanos)

    def contar_nodos(self):
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.izq) + self._contar_nodos(nodo.der)

    def barrido_ordenado(self):
        self._barrido_ordenado(self.raiz)

    def _barrido_ordenado(self, nodo):
        if nodo:
            self._barrido_ordenado(nodo.izq)
            print(nodo.nombre)
            self._barrido_ordenado(nodo.der)

if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()
    
    arbol.insertar("Iron Man", True)
    arbol.insertar("Thanos", False)
    arbol.insertar("Captain America", True)
    arbol.insertar("Doctor Strange", True)
    arbol.insertar("Loki", False)
    arbol.insertar("Ultron", False)
    arbol.insertar("Black Widow", True)
    arbol.insertar("Hela", False)

    arbol.listar_villanos()

    arbol.heroes_con_C()

    print(f"\nNúmero de superhéroes: {arbol.contar_heroes()}")

    arbol.corregir_doctor_strange()

    arbol.listar_heroes_descendente()

    arbol_heroes, arbol_villanos = arbol.generar_bosque()

    print(f"\nNodos en el árbol de héroes: {arbol_heroes.contar_nodos()}")
    print(f"Nodos en el árbol de villanos: {arbol_villanos.contar_nodos()}")

    print("\nHéroes en orden alfabético:")
    arbol_heroes.barrido_ordenado()

    print("\nVillanos en orden alfabético:")
    arbol_villanos.barrido_ordenado()
