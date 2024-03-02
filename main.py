def open_file(file_name: str) -> list:
    """
    This function reads file and saves its content into a list.
    :param file_name:
    :return:
    """

    content = list()

    with open(file_name, "r") as file:
        for line in file:
            content.append(line.strip())

    return content


def compare_files_content(file_1: str, file_2: str) -> str:
    """
    This function compares two files content and returns lines from first file which is missing in
    a second file.
    :param file_1:
    :param file_2:
    :return:
    """

    first_file_content = open_file(file_1)
    second_file_content = open_file(file_2)

    return "\n".join([x for x in first_file_content if x not in second_file_content])
