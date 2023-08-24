# Конвертер валют [easy](https://currency--converter.streamlit.app/)
# 🧾 → 📸 → 🪄  ✨  →  💱> 

> Ознакомиться с [приложением можно тут](https://currency--converter.streamlit.app/).

## О проекте
Сервис позволяет конвертировать валюту с фотографий ценников в выбранную вами валюту. Поддерживается 161 мировая валюта.

 1. Выберите валюту для конвертации
 <img src="https://i.imgur.com/vYS8u4z.png" width="500">
 
 2. Сделайте или загрузите фото
<img src="https://i.imgur.com/56epkYA.jpg" width="300">
 
 3. Готово! 
 <img src="https://i.imgur.com/7ygGojW.jpg" width="300">

## Реализация

 - Computer Vision. Для оптического распознавания символов (optical character recognition, OCR) был использован [EasyOCR](https://github.com/JaidedAI/EasyOCR) — модуль Python для извлечения текста из изображения. Настроен для распознавания чисел
 
 `reader = easyocr.Reader(lang_list=['en'])`

 `reader.readtext(photo, allowlist ='.,0123456789')`

 - Currency conversion rates. Актульные курсы валют обновляются через запрос к API [ExchangeRate](https://www.exchangerate-api.com/).

`url = f'https://v6.exchangerate-api.com/v6/{key}/pair/{currency_from}/{currency_to}/{price}'`

`response = requests.get(url)`

`result = response.json()`

 - Web App. Приложение написано с помощью [Streamlit](https://streamlit.io/) - фреймворк для создания интерактивных панелей визуализации данных машинного обучения с готовым UI решением.