""""------------------------------------------ *
Fatec
São
Caetano
do
Sul
Atividade
B1 - 1

Author[1681432612017]
Objetivo: X
data: 24 / 02 / 2026
*------------------------------------------ * """

catalog = {}


def add_movie(id_movie, title, director):
    if catalog.get(id_movie) is None:
        catalog[id_movie] = {
            "title": title,
            "director": director
        }
        return
    print(f"There is already a movie with id: {id_movie}")


def get_movie(id_movie):
    movie = catalog.get(id_movie)

    if movie is None:
        print(f"There are not a movie with id: {id_movie}")
        return
    print(f"Title: {movie.get('title')}")
    print(f"Director: {movie.get('director')}")
    print("=========================")



def remove_movie(id_movie):
    if catalog.get(id_movie) is None:
        print(f"There is no movie with id: {id_movie}")
        return
    title = catalog[id_movie]["title"]
    catalog.pop(id_movie)
    print(f"Movie deleted: {id_movie}")

def list_all():
    if not catalog:
        print("\n catalog is null")
    else:
        print("\n --- Movie List --- ")
        for id_m, dados in catalog.items():
            print(f"ID: {id_m} | Title: {dados['title']} | Director: {dados['director']}")


add_movie(1, "Harry Potter", "Diretor de Harry Potter")
add_movie(2, "Interstellar", "Diretor de Interestelar")
add_movie(3, "Eduardosim", "Augustobobo")
remove_movie(2)
get_movie(1)
list_all()
get_movie(3)