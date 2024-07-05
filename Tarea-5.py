import os


def format_text(text: str, max_width: int) -> list:
    """
    Formatea el texto para que cada línea tenga como máximo `max_width` caracteres,
    justificando completamente el texto (excepto la última línea).

    Argumentos:
        text (str): El texto a formatear.
        max_width (int): El ancho máximo de cada línea.

    Retorna:
        list: Una lista de líneas con el texto formateado.
    """
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) > max_width:
            for i in range(max_width - current_length):
                current_line[i % (len(current_line) - 1 or 1)] += ' '
            lines.append(''.join(current_line))
            current_line, current_length = [], 0
        current_line.append(word)
        current_length += len(word)

    lines.append(' '.join(current_line))
    return lines


def main() -> None:
    """
    Función principal que gestiona la entrada del usuario, lee el archivo, 
    formatea el texto y maneja la salida según las opciones del usuario.
    """
    file_path = input("Por favor, ingrese la dirección del archivo .txt: ")

    if not os.path.isfile(file_path):
        print("El archivo no existe. Por favor, verifique la dirección e intente de nuevo.")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    max_width = int(input("Por favor, ingrese el ancho de línea para el formato: "))

    formatted_lines = format_text(text, max_width)
    formatted_text = '\n'.join(formatted_lines)

    print(
        "¿Desea guardar el archivo en la misma ubicación, sobrescribirlo, "
        "o solo mostrar el texto en la terminal?"
    )
    print("1. Guardar en la misma ubicación")
    print("2. Sobrescribir el archivo original")
    print("3. Mostrar el texto en la terminal")

    option = input("Seleccione una opción (1, 2, o 3): ")

    if option == '1':
        new_file_path = os.path.splitext(file_path)[0] + '_formatted.txt'
        with open(new_file_path, 'w', encoding='utf-8') as file:
            file.write(formatted_text)
        print(f"Archivo guardado en: {new_file_path}")
    elif option == '2':
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(formatted_text)
        print(f"Archivo sobrescrito: {file_path}")
    elif option == '3':
        print("Texto formateado:")
        print(formatted_text)
    else:
        print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
