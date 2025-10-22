import os

def quick_change_extension():
    """Простая версия для быстрого изменения расширения"""
    file_path = input("Введите путь к файлу: ").strip()
    
    if not os.path.isfile(file_path):
        print("Файл не найден!")
        return
    
    print("Выберите расширение: 1 - PNG, 2 - JPG")
    choice = input("Ваш выбор: ").strip()
    
    if choice == "1":
        new_ext = ".png"
    elif choice == "2":
        new_ext = ".jpg"
    else:
        print("Неверный выбор!")
        return
    
    # Создаем новое имя файла
    directory = os.path.dirname(file_path)
    filename = os.path.basename(file_path)
    name_without_ext = os.path.splitext(filename)[0]
    new_file_path = os.path.join(directory, name_without_ext + new_ext)
    
    try:
        os.rename(file_path, new_file_path)
        print(f"Файл переименован: {new_file_path}")
    except Exception as e:
        print(f"Ошибка: {e}")