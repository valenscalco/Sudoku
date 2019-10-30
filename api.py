import requests


def api(tam):
    resp = requests.get(
        'http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=1&size=' + str(tam)
        )

    lista = [[0 for __ in range(tam)] for _ in range(tam)]

    for item in resp.json()["squares"]:
        lista[item["y"]][item["x"]] = item["value"]

    return lista


api(9)
