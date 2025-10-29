import os
import shutil

def quick_change_extension():
    """Изменение расширения"""
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

def move_file():
    """Перемещение файла между папками"""
    file_path = input("Введите путь к файлу: ").strip()
    
    if not os.path.isfile(file_path):
        print("Файл не найден!")
        return
    
    destination_folder = input("Введите путь к папке назначения: ").strip()
    
    if not os.path.isdir(destination_folder):
        create_dir = input("Папка не существует. Создать? (y/n): ").strip().lower()
        if create_dir == 'y':
            try:
                os.makedirs(destination_folder)
                print(f"Папка создана: {destination_folder}")
            except Exception as e:
                print(f"Ошибка создания папки: {e}")
                return
        else:
            return
    
    try:
        # Получаем имя файла для создания полного пути назначения
        filename = os.path.basename(file_path)
        destination_path = os.path.join(destination_folder, filename)
        
        # Проверяем, не существует ли уже файл в папке назначения
        if os.path.exists(destination_path):
            overwrite = input("Файл уже существует в папке назначения. Перезаписать? (y/n): ").strip().lower()
            if overwrite != 'y':
                print("Операция отменена.")
                return
        
        shutil.move(file_path, destination_path)
        print(f"Файл перемещен: {destination_path}")
    except Exception as e:
        print(f"Ошибка перемещения: {e}")

def main_menu():
    """Главное меню"""
    while True:
        print("\n" + "="*30)
        print("1 - Изменить расширение файла")
        print("2 - Переместить файл")
        print("3 - Выход")
        print("="*30)
        
        choice = input("Выберите действие: ").strip()
        
        if choice == "1":
            quick_change_extension()
        elif choice == "2":
            move_file()
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main_menu()