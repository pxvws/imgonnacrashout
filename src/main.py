def main():
    print("Мое приложение: Текстовый 'Сейф'")
    print("Программа для шифрования и хранения секретных текстов.")

if __name__ == "__main__":
    main()



def encrypt_text(text):

    encryption_dict = {
        'а': '@', 'б': 'ß', 'в': 'Ⅴ', 'г': 'Γ', 'д': 'Δ',
        'е': '€', 'ё': '€', 'ж': 'Ψ', 'з': 'Ζ', 'и': 'И',
        'й': 'Й', 'к': 'Κ', 'л': 'Λ', 'м': 'Μ', 'н': 'Η',
        'о': 'Θ', 'п': 'Π', 'р': 'Ρ', 'с': '$', 'т': 'Τ',
        'у': 'У', 'ф': 'Φ', 'х': 'Χ', 'ц': 'Ц', 'ч': 'Ч',
        'ш': 'Ш', 'щ': 'Щ', 'ъ': 'Ъ', 'ы': 'Ы', 'ь': 'Ь',
        'э': 'Э', 'ю': 'Ю', 'я': 'Я',
        'a': '@', 'b': 'β', 'c': '¢', 'd': '∂', 'e': 'ε',
        'f': 'ƒ', 'g': 'φ', 'h': 'η', 'i': '!', 'j': 'נ',
        'k': 'κ', 'l': 'ℓ', 'm': 'μ', 'n': 'η', 'o': 'θ',
        'p': 'π', 'q': 'ℚ', 'r': 'ρ', 's': '$', 't': 'τ',
        'u': 'μ', 'v': 'ν', 'w': 'ω', 'x': 'χ', 'y': '¥',
        'z': 'ζ'
    }

    encrypted = ''
    for char in text:
        encrypted += encryption_dict.get(char.lower(), char)
    return encrypted



def decrypt_text(encrypted_text):
    decryption_dict = {
        '@': 'а', 'ß': 'б', 'Ⅴ': 'в', 'Γ': 'г', 'Δ': 'д',
        '€': 'е', 'Ψ': 'ж', 'Ζ': 'з', 'И': 'и', 'Й': 'й',
        'Κ': 'к', 'Λ': 'л', 'Μ': 'м', 'Η': 'н', 'Θ': 'о',
        'Π': 'п', 'Ρ': 'р', '$': 'с', 'Τ': 'т', 'У': 'у',
        'Φ': 'ф', 'Χ': 'х', 'Ц': 'ц', 'Ч': 'ч', 'Ш': 'ш',
        'Щ': 'щ', 'Ъ': 'ъ', 'Ы': 'ы', 'Ь': 'ь', 'Э': 'э',
        'Ю': 'ю', 'Я': 'я',
        'β': 'b', '¢': 'c', '∂': 'd', 'ε': 'e', 'ƒ': 'f',
        'φ': 'g', 'η': 'h', '!': 'i', 'נ': 'j', 'κ': 'k',
        'ℓ': 'l', 'μ': 'm', 'θ': 'o', 'π': 'p', 'ℚ': 'q',
        'ρ': 'r', 'τ': 't', 'ν': 'v', 'ω': 'w', 'χ': 'x',
        '¥': 'y', 'ζ': 'z'
    }

    decrypted = ''
    for char in encrypted_text:
        decrypted += decryption_dict.get(char, char)
    return decrypted



secrets = []



def add_secret():
    print("\n--- Добавить новый секрет ---")
    title = input("Введите название секрета: ")
    text = input("Введите текст секрета: ")

    encrypted = encrypt_text(text)
    secret = {
        'id': len(secrets) + 1,
        'title': title,
        'original': text,
        'encrypted': encrypted,
        'date': '2024-01-01'  # Позже добавим дату
    }
    secrets.append(secret)
    print(f"✓ Секрет '{title}' добавлен и зашифрован!")
    print(f"Зашифрованный текст: {encrypted}")



def show_all(show_encrypted=False):
    print("\n--- Все секреты ---")
    if not secrets:
        print("Секретов пока нет.")
        return

    for secret in secrets:
        print(f"\n[{secret['id']}] {secret['title']}")
        print(f"   Дата: {secret['date']}")
        if show_encrypted:
            print(f"   Зашифрованный: {secret['encrypted']}")
        else:
            print(f"   Оригинал: {secret['original']}")


def main():
    while True:
        print("\n=== Текстовый 'Сейф' ===")
        print("1. Добавить новый секрет")
        print("2. Показать все секреты (оригиналы)")
        print("3. Показать все секреты (зашифрованные)")
        print("4. Протестировать шифрование")
        print("5. Выход")

        choice = input("\nВыберите действие (1-5): ")

        if choice == '1':
            add_secret()
        elif choice == '2':
            show_all(show_encrypted=False)
        elif choice == '3':
            show_all(show_encrypted=True)
        elif choice == '4':
            test_text = input("Введите текст для теста шифрования: ")
            encrypted = encrypt_text(test_text)
            decrypted = decrypt_text(encrypted)
            print(f"Исходный: {test_text}")
            print(f"Зашифрованный: {encrypted}")
            print(f"Расшифрованный: {decrypted}")
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()