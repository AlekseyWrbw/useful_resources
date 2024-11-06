import requests

def check_website(url):
    try:
        response = requests.get(url)
        # Проверяем код состояния
        if response.status_code == 200:
            print(f"Сайт '{url}' доступен. Код состояния: {response.status_code}")
        else:
            print(f"Сайт '{url}' недоступен. Код состояния: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при доступе к '{url}': {e}")

if __name__ == "__main__":
    # Укажите URL для проверки
    url_to_check = "https://www.example.com"  # Замените на нужный URL
    check_website(url_to_check)