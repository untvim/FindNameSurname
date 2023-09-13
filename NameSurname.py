import re
from googletrans import Translator

file_path = "text.txt"
output_file_path = "output.txt"

translator = Translator()

try:
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

        pattern = r'([A-Z][a-zA-Z]+) ([A-Z][a-zA-Z]+)'

        matches = re.findall(pattern, text)

        if matches:
            with open(output_file_path, "w", encoding="utf-8") as output_file:
                for match in matches:
                    last_name = match[0]
                    first_name = match[1]

                    last_name_translation = translator.translate(last_name, src='ru', dest='en').text
                    first_name_translation = translator.translate(first_name, src='ru', dest='en').text

                    formatted_name = f"{last_name_translation}_{first_name_translation}"
                    output_file.write(formatted_name + "\n")
                    print(f"Фамилия и Имя (EN): {formatted_name}")

            print(f"Переведенные имена записаны в файл: {output_file_path}")
        else:
            print("Фамилии и имена не найдены.")

except FileNotFoundError:
    print(f"Файл '{file_path}' не найден.")

except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
