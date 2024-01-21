import json

MAX_TLF_DIGITS = 11


def list_operations():
    print("\nOperaciones con LISTAS:")
    my_list = [1, 2]
    print(f"La lista inicial: my_list == {my_list}")

    my_list.append(3)
    print(f"La lista tras añadir un 3:")
    print("""    my_list.append(3)""")
    print(f"    my_list == {my_list}")

    my_list.extend([4, 5])
    print(f"La lista tras añadir [4, 5]:")
    print("""    my_list.extend([4, 5])""")
    print(f"    my_list == {my_list}")

    last = my_list.pop()
    print(f"La lista tras eliminar el último valor ({last}):")
    print("""    last = my_list.pop()""")
    print(f"    my_list == {my_list}")

    my_list.remove(2)
    print(f"La lista tras eliminar el 2:")
    print("""    my_list.remove(2)""")
    print(f"    my_list == {my_list}")

    my_list[2] = 0
    print(f"La lista tras actualizar su tercer valor:")
    print("""    my_list[2] = 0""")
    print(f"    my_list == {my_list}")

    print(f"La lista ordenada, sin modificar la original: {sorted(my_list)}")
    print(f"Efectivamente, la lista sigue siendo {my_list}")

    my_list.sort(reverse=True)
    print(f"Ahora hemos ordenado la lista in-place, en order inverso:")
    print("""    my_list.sort(reverse=True)""")
    print(f"    my_list == {my_list}")


def tuple_operations():
    print("\nOperaciones con TUPLAS:")
    my_tuple = (1, 2)
    print(f"La tupla inicial: my_tuple == {my_tuple}")

    my_tuple = my_tuple + (3, 4, 5)
    print("Las tuplas no se pueden modificar.", end="")
    print(" Para extenderla tendremos que crear una nueva tupla (que puede sobreescribir la original):")
    print("""    my_tuple = my_tuple + (3, 4, 5)""")
    print(f"    my_tuple == {my_tuple}")

    print("Las tuplas, por tanto, no pueden tener valores añadidos, eliminados, o modificados.")
    print(f"La tupla se puede ordenar sin modificar la original:")
    print(f"    x = tuple(sorted(my_tuple, reverse=True))")
    print(f"    x == {tuple(sorted(my_tuple, reverse=True))}")
    print(f"Pero, lógicamente, no puede ordenarse in-place.")


def set_operations():
    print("\nOperaciones con SETS:")
    my_set = {1, 2}
    print(f"El set inicial: my_set == {my_set}")

    print("En un set se puede insertar un valor:")
    my_set.add(3)
    print(f"    my_set.add(3)")
    print(f"    my_set == {my_set}")

    print("Si añadimos un valor duplicado, no tendrá efecto:")
    my_set.add(2)
    print(f"    my_set.add(2)")
    print(f"    my_set == {my_set}")

    print("Podemos unir dos sets, y obtendremos un tercer set que contendrá a ambos, pero sin duplicados:")
    other_set = {2, 3, 4}
    third_set = my_set | other_set
    print("    other_set = {2, 3, 4}")
    print("    third_set = my_set | other_set")
    print(f"    third_set == {third_set}")

    print("Podemos eliminar elementos de un set mediante su valor:")
    my_set.remove(2)
    print("    my_set.remove(2)")
    print(f"    my_set == {my_set}")

    print("En cuanto a actualizar un set, hemos visto que podemos añadir o eliminar elementos.")
    print("Sin embargo, los sets son colecciones desordenadas. A diferencia de una lista, no tendría")
    print("sentido pedir a un set que se cambie el valor de su enésimo elemento. Adicionalmente, los")
    print("elementos de un set tienen que ser inmutables (aunque el set en sí es mutable).")

    print("Como hemos dicho, un set es una colección desordenada. No tiene sentido ordenar un set in-place.")
    print("Lo que sí podemos es pedir una representación ordenada del set (como con listas o tuples):")
    print("    x = tuple(sorted(my_set, reverse=True))")
    print(f"    x == {tuple(sorted(my_set, reverse=True))}")
    print("Sin embargo:")
    print("    x = set(sorted(my_set, reverse=True))")
    print(f"    x == {set(sorted(my_set, reverse=True))}")


def dict_operations():
    print("\nOperaciones con DICCIONARIOS:")
    my_dict = {"a": 1, "b": 2}
    print(f"El diccionario original: my_dict == {my_dict}")

    my_dict["c"] = 3
    print("Podemos insertar valores en un diccionario accediendo a una clave que todavía no existía:")
    print("""    my_dict["c"] = 3""")
    print(f"    my_dict == {my_dict}")

    other_dict = {"d": 4, "f": 5}
    my_dict.update(other_dict)
    print(f"También podemos insertar valores de un diccionario en otro:")
    print("""    other_dict = {"d": 4, "f": 5}""")
    print("""    my_dict.update(other_dict)""")
    print(f"    my_dict == {my_dict}")

    del my_dict["b"]
    print(f"Podemos eliminar un par clave/valor del dicionario usando la clave:")
    print("""    del my_dict["b"]""")
    print(f"    my_dict == {my_dict}")

    my_dict["a"] = 11
    print(f"Si la clave ya existe, en vez de insertar, lo que hacemos es actualizar el valor:")
    print("""    my_dict["a"] = 11""")
    print(f"    my_dict == {my_dict}")

    other_dict = {"c": -1, "d": -2}
    my_dict.update(other_dict)
    print("Si insertamos valores de un diccionario en otro, y una o varias claves ya existen, serán actualizadas:")
    print("""    other_dict = {"c": -1, "d": -2}""")
    print("""    my_dict.update(other_dict)""")
    print(f"    my_dict == {my_dict}")

    print("Un diccionario es una colección de elementos sin orden, por lo tanto no tiene sentido ordenarlo in-place.")
    print("Sin embargo si podemos generar una representación ordenada. Por ejemplo, por orden de clave inversa:")
    print(f"    x = dict(sorted(my_dict.items(), reverse=True))")
    print(f"    x == {dict(sorted(my_dict.items(), reverse=True))}")

    print("También podemos ordenar por valor (o cualquier función arbitraria que use claves y/o valores).")
    print("Por ejemplo, ordenemos numéricamente por valor:")
    print(f"    x = dict(sorted(my_dict.items(), key=lambda e: e[1]))")
    print(f"    x == {dict(sorted(my_dict.items(), key=lambda e: e[1]))}")


def extra():
    """
    Given the simplicity of the request, we could implement the contacts as a dict
    where the key is the name, and the value is the telephone number. However, for
    extensibility, we will implement a dictionary {id: contact}, where 'contact'
    is a dict {"name": ..., "phone": ...}.
    """
    contacts = {}

    while True:
        option = input("Escoge accion: [0] imprimir, [1] insertar, [2] buscar, [3] actualizar, [4] eliminar, [q] salir: ")

        if option == "q":
            break
        elif option == "0":
            print(json.dumps(contacts, indent=4))
        elif option == "1":
            contacts = insert_into_contacts(contacts)
        else:
            print("Opción desconocida. Ignorando.")


def insert_into_contacts(contacts: dict) -> dict:
    """
    Given current contacts 'contacts', insert a new contact and return updated contacts.

    Args:
        contacts (dict):
            Current contact dict.

    Returns:
        A dictionary with updated contacts.
    """
    name = input("Introduce el nombre del nuevo contacto: ")

    if not name:
        print("No introdujiste ningún nombre. Abortando inserción...")
        return contacts

    if find_contacts(contacts, name=name):
        res = input(f"Un contacto llamado '{name}' ya existe. ¿Deseas añadir otro con el mismo nombre? [y/n]: ")
        if res == "y":
            print("De acuerdo, proseguimos...")
        else:
            print("De acuerdo, abortamos inserción...")
            return contacts

    tlf = input(f"Introduce el número de teléfono de '{name}': ")
    while True:
        try:
            tlf = int(tlf)
        except ValueError:
            tlf = input("Introdujiste un valor no numérico. Por favor, introduce un teléfono válido: ")
            continue

        if tlf >= 10**MAX_TLF_DIGITS:
            tlf = input(f"Introdujiste un teléfono con más de {MAX_TLF_DIGITS} dígitos. Por favor, introduce un teléfono válido: ")
            continue

        break

    new_id = get_new_id(contacts)
    print(f"Introduciendo contacto '{name}' con teléfono '{tlf}' con ID = {new_id}")

    contacts[new_id] = {
        "name": name,
        "phone": tlf,
    }

    return contacts


def get_new_id(contacts: dict) -> int:
    """
    Given a contact directory 'contacts', find a free ID, in the form of the first
    integer larger than the largest ID so far.
    """
    if not contacts:
        return 1

    return sorted(contacts.keys())[-1] + 1


def find_contacts(contacts: dict, name: str | None = None, phone: int | None = None) -> list[int]:
    """
    Given a contact directory 'contacts', find and return the IDs of the contact within it
    matching the query parameters. If 'name' is provided, filter contacts by that name.
    If tlf is given, filter contacts by that number.

    Args:
        contacts (dict):
            Contact directory where the contacts will be searched.
        name (optional str):
            Filter contacts by that name.
        phone (optional int):
            Filter contacts by that number.

    Returns:
        List of IDs of contacts matching the filtering criteria.
    """
    filtered_ids = []
    for contact_id, contact in contacts.items():
        if name is not None and contact["name"] != name:
            continue

        if phone is not None and contact["phone"] != phone:
            continue

        filtered_ids.append(contact_id)

    return filtered_ids


def main():
    list_operations()
    tuple_operations()
    set_operations()
    dict_operations()


if __name__ == "__main__":
    main()
    extra()
