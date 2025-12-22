import json
import os
from datetime import datetime


DATA_FILE = "secrets.json"


secrets = []


def encrypt_text(text):

    encryption_dict = {
        # Русские буквы
        "а": "@",
        "б": "ß",
        "в": "Ⅴ",
        "г": "Γ",
        "д": "Δ",
        "е": "€",
        "ё": "€",
        "ж": "Ψ",
        "з": "Ζ",
        "и": "И",
        "й": "Й",
        "к": "Κ",
        "л": "Λ",
        "м": "Μ",
        "н": "Η",
        "о": "Θ",
        "п": "Π",
        "р": "Ρ",
        "с": "$",
        "т": "Τ",
        "у": "У",
        "ф": "Φ",
        "х": "Χ",
        "ц": "Ц",
        "ч": "Ч",
        "ш": "Ш",
        "щ": "Щ",
        "ъ": "Ъ",
        "ы": "Ы",
        "ь": "Ь",
        "э": "Э",
        "ю": "Ю",
        "я": "Я",
        # Английские буквы
        "a": "@",
        "b": "β",
        "c": "¢",
        "d": "∂",
        "e": "ε",
        "f": "ƒ",
        "g": "φ",
        "h": "η",
        "i": "!",
        "j": "נ",
        "k": "κ",
        "l": "ℓ",
        "m": "μ",
        "n": "η",
        "o": "θ",
        "p": "π",
        "q": "ℚ",
        "r": "ρ",
        "s": "$",
        "t": "τ",
        "u": "μ",
        "v": "ν",
        "w": "ω",
        "x": "χ",
        "y": "¥",
        "z": "ζ",
    }

    encrypted = ""
    for char in text:
        if char.lower() in encryption_dict:
            if char.isupper():
                encrypted += encryption_dict[char.lower()].upper()
            else:
                encrypted += encryption_dict[char.lower()]
        else:
            encrypted += char
    return encrypted


def decrypt_text(encrypted_text):

    decryption_dict = {
        "@": "а",
        "ß": "б",
        "Ⅴ": "в",
        "Γ": "г",
        "Δ": "д",
        "€": "е",
        "Ψ": "ж",
        "Ζ": "з",
        "И": "и",
        "Й": "й",
        "Κ": "к",
        "Λ": "л",
        "Μ": "м",
        "Η": "н",
        "Θ": "о",
        "Π": "п",
        "Ρ": "р",
        "$": "с",
        "Τ": "т",
        "У": "у",
        "Φ": "ф",
        "Χ": "х",
        "Ц": "ц",
        "Ч": "ч",
        "Ш": "ш",
        "Щ": "щ",
        "Ъ": "ъ",
        "Ы": "ы",
        "Ь": "ь",
        "Э": "э",
        "Ю": "ю",
        "Я": "я",
        "β": "b",
        "¢": "c",
        "∂": "d",
        "ε": "e",
        "ƒ": "f",
        "φ": "g",
        "η": "h",
        "!": "i",
        "נ": "j",
        "κ": "k",
        "ℓ": "l",
        "μ": "m",
        "θ": "o",
        "π": "p",
        "ℚ": "q",
        "ρ": "r",
        "τ": "t",
        "ν": "v",
        "ω": "w",
        "χ": "x",
        "¥": "y",
        "ζ": "z",
    }

    decrypted = ""
    for char in encrypted_text:
        if char in decryption_dict:
            decrypted += decryption_dict[char]
        else:
            decrypted += char
    return decrypted


def load_secrets():

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Ошибка загрузки файла: {e}")
            return []
    return []


def save_secrets():

    try:
        data_to_save = []
        for secret in secrets:
            data_to_save.append(
                {
                    "id": secret["id"],
                    "title": secret["title"],
                    "encrypted": secret["encrypted"],
                    "date": secret["date"],
                }
            )

        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=2)
        print("✓ Данные сохранены в файл")
    except IOError as e:
        print(f"Ошибка сохранения: {e}")


def add_secret():

    print("\n" + "=" * 40)
    print("ДОБАВИТЬ НОВЫЙ СЕКРЕТ")
    print("=" * 40)

    title = input("Введите название секрета: ").strip()
    if not title:
        print("✗ Название не может быть пустым!")
        return

    text = input("Введите текст секрета: ").strip()
    if not text:
        print("✗ Текст не может быть пустым!")
        return

    encrypted = encrypt_text(text)
    secret = {
        "id": len(secrets) + 1,
        "title": title,
        "original": text,
        "encrypted": encrypted,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    secrets.append(secret)
    save_secrets()
    print(f"\n✓ Секрет '{title}' успешно добавлен!")
    print(
        f"Зашифрованный текст: {encrypted[:50]}..."
        if len(encrypted) > 50
        else f"Зашифрованный текст: {encrypted}"
    )


def show_all(show_encrypted=False):

    print("\n" + "=" * 40)
    print("ВСЕ СЕКРЕТЫ" + (" (ЗАШИФРОВАННЫЕ)" if show_encrypted else ""))
    print("=" * 40)

    if not secrets:
        print("Секретов пока нет.")
        return

    for secret in secrets:
        print(f"\n[{secret['id']}] {secret['title']}")
        print(f"   Дата: {secret['date']}")
        if show_encrypted:
            print(
                f"   Зашифрованный: {secret['encrypted'][:50]}..."
                if len(secret["encrypted"]) > 50
                else f"   Зашифрованный: {secret['encrypted']}"
            )
        else:
            print(
                f"   Оригинал: {secret['original'][:50]}..."
                if len(secret["original"]) > 50
                else f"   Оригинал: {secret['original']}"
            )


def delete_secret():

    show_all(False)

    if not secrets:
        return

    try:
        secret_id = int(input("\nВведите ID секрета для удаления: "))

        for i, secret in enumerate(secrets):
            if secret["id"] == secret_id:
                confirm = input(
                    f"Вы уверены, что хотите удалить '{secret['title']}'? (да/нет): "
                )
                if confirm.lower() == "да":
                    deleted = secrets.pop(i)
                    # Обновляем ID оставшихся секретов
                    for j, s in enumerate(secrets[i:], start=i):
                        s["id"] = j + 1
                    save_secrets()
                    print(f"✓ Секрет '{deleted['title']}' удален!")
                else:
                    print("✗ Удаление отменено.")
                return

        print(f"✗ Секрет с ID {secret_id} не найден.")
    except ValueError:
        print("✗ Введите корректный номер ID!")


def search_secrets():

    keyword = input("Введите слово для поиска: ").lower().strip()

    if not keyword:
        print("✗ Введите слово для поиска!")
        return

    found = []
    for secret in secrets:
        if (
            keyword in secret["title"].lower()
            or keyword in secret["original"].lower()
            or keyword in secret["encrypted"].lower()
        ):
            found.append(secret)

    if found:
        print(f"\nНайдено секретов: {len(found)}")
        for secret in found:
            print(f"\n[{secret['id']}] {secret['title']}")
            print(f"   Дата: {secret['date']}")
            print(f"   Текст: {secret['original'][:50]}...")
    else:
        print("✗ Секреты не найдены.")


def test_encryption():

    print("\n" + "=" * 40)
    print("ТЕСТ ШИФРОВАНИЯ")
    print("=" * 40)

    test_text = input("Введите текст для теста: ")

    if not test_text:
        print("✗ Введите текст для теста!")
        return

    encrypted = encrypt_text(test_text)
    decrypted = decrypt_text(encrypted)

    print("\nРезультаты теста:")
    print("-" * 30)
    print(f"Исходный текст:    {test_text}")
    print(f"Зашифрованный текст: {encrypted}")
    print(f"Расшифрованный текст: {decrypted}")
    print("-" * 30)

    if test_text == decrypted:
        print("✓ Шифрование работает корректно!")
    else:
        print("✗ Ошибка в шифровании/дешифровании!")


def show_statistics():

    print("\n" + "=" * 40)
    print("СТАТИСТИКА")
    print("=" * 40)

    print(f"Всего секретов: {len(secrets)}")

    if secrets:
        dates = [datetime.strptime(s["date"], "%Y-%m-%d %H:%M") for s in secrets]
        oldest = min(dates).strftime("%Y-%m-%d")
        newest = max(dates).strftime("%Y-%m-%d")

        print(f"Период: с {oldest} по {newest}")

        longest = max(secrets, key=lambda x: len(x["original"]))
        print(
            f"Самый длинный секрет: '{longest['title']}' ({len(longest['original'])} символов)"
        )

        total_chars = sum(len(s["original"]) for s in secrets)
        print(f"Всего символов: {total_chars}")


def main():

    global secrets

    print("\n" + "=" * 50)
    print("        ТЕКСТОВЫЙ 'СЕЙФ' v1.0")
    print("=" * 50)
    print("Программа для безопасного хранения секретов")
    print("=" * 50)

    print("\nЗагрузка данных...")
    secrets_data = load_secrets()

    for secret_data in secrets_data:
        secret = {
            "id": secret_data["id"],
            "title": secret_data["title"],
            "original": decrypt_text(secret_data["encrypted"]),
            "encrypted": secret_data["encrypted"],
            "date": secret_data["date"],
        }
        secrets.append(secret)

    print(f"✓ Загружено {len(secrets)} секретов")

    while True:
        print("\n" + "=" * 50)
        print("ГЛАВНОЕ МЕНЮ")
        print("=" * 50)
        print("1. Добавить новый секрет")
        print("2. Показать все секреты (оригиналы)")
        print("3. Показать все секреты (зашифрованные)")
        print("4. Удалить секрет")
        print("5. Поиск секретов")
        print("6. Тестирование шифрования")
        print("7. Статистика")
        print("8. Выход")
        print("=" * 50)

        choice = input("\nВыберите действие (1-8): ").strip()

        if choice == "1":
            add_secret()
        elif choice == "2":
            show_all(show_encrypted=False)
        elif choice == "3":
            show_all(show_encrypted=True)
        elif choice == "4":
            delete_secret()
        elif choice == "5":
            search_secrets()
        elif choice == "6":
            test_encryption()
        elif choice == "7":
            show_statistics()
        elif choice == "8":
            save_secrets()
            print("\n" + "=" * 50)
            print("Спасибо за использование Текстового 'Сейфа'!")
            print("Все данные сохранены в файл secrets.json")
            print("=" * 50)
            break
        else:
            print("\n✗ Неверный выбор. Введите число от 1 до 8.")

        input("\nНажмите Enter чтобы продолжить...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана. Сохранение данных...")
        save_secrets()
        print("До свидания!")
    except Exception as e:
        print(f"\n✗ Произошла ошибка: {e}")
        print("Попробуйте перезапустить программу.")
