import re


def street_filter(streets):
    for i in range(len(streets)):
        streets[i] = re.sub(r',', '', streets[i])
        streets[i] = re.sub(r'([Уу]лица|\b[Уу]л\b)\.?', 'ул.', streets[i])
        streets[i] = re.sub(r'([Пп]роспект|b[Пп]росп\b)\.?',
                            'просп.', streets[i])
        streets[i] = re.sub(r'([Пп]роезд|\b[Пп]р\b)\.?', 'пр-д', streets[i])
        streets[i] = re.sub(r'([Шш]оссе|\b[Шш]\b)\.?', 'ш.', streets[i])
        streets[i] = re.sub(r'([Бб]ульвар|\b[Бб]ульв\b)\.?',
                            'бульв.', streets[i])
        streets[i] = re.sub(r'([Пп]ереулок|\b[Пп]ер\b)\.?', 'пер.', streets[i])
    return streets
