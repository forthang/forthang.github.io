import requests  # Импортируем библиотеку для выполнения HTTP-запросов
import xml.etree.ElementTree as ET  # Импортируем модуль для работы с XML
import json  # Импортируем модуль для работы с JSON


def request(url: str) -> None:
    # Выполняем GET-запрос к API OpenStreetMap для получения информации об здании
    response = requests.get(url)
    # Парсим XML-ответ от API в дерево элементов
    root = ET.fromstring(response.content)
    # Инициализируем список для хранения ID узлов
    node_refs = []
    # Инициализируем список для хранения координат узлов
    coordinates = []
    # Инициализируем переменную для хранения названия
    name = None

    # Перебираем элементы внутри XML-документа
    for element in root:
        if element.tag == "way":  # Ищем элемент <way>
            for nd in element.findall("nd"):  # Ищем все элементы <nd> внутри <way>
                ref = nd.attrib.get("ref")  # Получаем атрибут ref (ID узла)
                if ref:  # Если ref существует, добавляем его в список node_refs
                    node_refs.append(ref)
            for tag in element.findall("tag"):  # Ищем все элементы <tag> внутри <way>
                if tag.attrib.get("k") == "name":  # Если атрибут k равен "name"
                    name = tag.attrib.get("v")  # Сохраняем значение атрибута v (имя)
        elif element.tag == "relation":  # Ищем элемент <relation>
            for member in element.findall("member"):  # Ищем все элементы <member> внутри <relation>
                ref = member.attrib.get("ref")  # Получаем атрибут ref (ID узла)
                if member.attrib.get("type") == "node" and ref:  # Если тип node
                    node_refs.append(ref)
                elif member.attrib.get("type") == "way" and ref:  # Если тип way
                    # Выполняем запрос для получения данных о way
                    way_response = requests.get(f"https://www.openstreetmap.org/api/0.6/way/{ref}")
                    way_response.raise_for_status()
                    way_root = ET.fromstring(way_response.content)
                    for way in way_root.findall("way"):
                        for nd in way.findall("nd"):
                            way_node_ref = nd.attrib.get("ref")
                            if way_node_ref:
                                node_refs.append(way_node_ref)
            for tag in element.findall("tag"):  # Ищем все элементы <tag> внутри <relation>
                if tag.attrib.get("k") == "name":  # Если атрибут k равен "name"
                    name = tag.attrib.get("v")  # Сохраняем значение атрибута v (имя)

    # Заменяем кавычки в имени на пустоту
    name = name.replace('"', "")

    # Для каждого ID узла выполняем запрос для получения его координат
    for node_id in node_refs:
        # Выполняем GET-запрос к API OpenStreetMap для получения данных о конкретном узле
        node_response = requests.get(f"https://www.openstreetmap.org/api/0.6/node/{node_id}")
        # Парсим XML-ответ в дерево элементов
        node_root = ET.fromstring(node_response.content)
        for node in node_root.findall("node"):  # Ищем все элементы <node> в ответе
            lat = node.attrib.get("lat")  # Получаем атрибут lat (широта)
            lon = node.attrib.get("lon")  # Получаем атрибут lon (долгота)
            if lat and lon:  # Если широта и долгота существуют
                # Добавляем координаты в список в формате (широта, долгота)
                coordinates.append((float(lat), float(lon)))

    # Создаем итоговый словарь с именем и списком координат
    result = {
        "name": name,  # Имя
        "coordinates": coordinates  # Список координат
    }

    # Записываем результат в файл output.json в формате JSON
    with open("output.json", 'a', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=4)  # Указываем отступы для читаемости

    # Открываем файл для замены "}{", чтобы объединить объекты
    with open("output.json", 'r', encoding='utf-8') as file:
        json_data = file.read()

    # Заменяем "}{", чтобы корректно объединить объекты
    json_data = json_data.replace("}{", ",")

    # Записываем обновлённые данные обратно в файл
    with open("output.json", 'w', encoding='utf-8') as file:
        file.write(json_data)

# Пример вызова
url = input("Введите ссылку: ")
request(url)
