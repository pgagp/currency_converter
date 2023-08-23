import easyocr
from PIL import Image
import json
import pandas as pd
import requests
import streamlit as st
import time



st.title(':orange[Конвертер валют] :violet[easy]')
st.title(':receipt: :orange[→] :camera_with_flash: :orange[→] :magic_wand: :sparkles: :orange[→] :currency_exchange:')

st.divider()
st.markdown('Мгновенно преобразует фотографии ценников в желаемую валюту. Просто сделайте снимок цены, выберите свою валюту и получите мгновенное преобразование. Экономьте время и избавьтесь от сложностей с ручным расчетом.')
st.divider()


# датафрейм название валюты + код валюты
df = pd.read_csv('currency_data.csv', index_col=0)

# функция для запроса актуальных курсов валют
def req_currency(curr_from, curr_to, price):
    url = f'https://v6.exchangerate-api.com/v6/278e5520bb33d953b5446519/pair/{curr_from}/{curr_to}/{price}'
    response = requests.get(url)
    res = response.json()
    return res['conversion_result'], res['conversion_rate']

# функция для распознавания чисел с изображения, возвращает число с самой большой площадью разметки
def predict(photo):
    reader = easyocr.Reader(lang_list=['en'])
    result = reader.readtext(photo, allowlist ='.,0123456789')
    max_area = 0
    for (bbox, text, prob) in result:
        x_min, y_min = map(int, bbox[0])
        x_max, y_max = map(int, bbox[2])
        area = (x_max - x_min) * (y_max - y_min)
        if area > max_area:
            max_area = area
            text_with_max_area = text

    return text_with_max_area

    
st.subheader('Шаг 1. Выберите валюту для конвертации')
col1, col2 = st.columns(2)
with col1:
    currency_from = st.selectbox(':violet[откуда]', (df['currency_name']))
    currency_from = df[df['currency_name'] == currency_from]['currency_code'].iloc[0]
with col2:
    currency_to = st.selectbox(':violet[куда]', (df['currency_name']))
    currency_to = df[df['currency_name'] == currency_to]['currency_code'].iloc[0]
st.markdown('')


st.subheader('Шаг 2. Сделайте или загрузите фото')
st.markdown('')
load = st.checkbox('валюты выбраны, загрузить фото')
if load:
    uploaded_photo = st.file_uploader('')
    if uploaded_photo:
        image = Image.open(uploaded_photo)
        st.image(image)
        st.toast('определяем цену :mag_right:')
        price = predict(image)
        time.sleep(1)
        st.toast('готово! :rocket:')
        st.caption(price)
        
        st.subheader('Шаг 3. Результат :tada:')
        res = req_currency(currency_from, currency_to, price)
        st.divider()
        st.write('текущий курс  1', currency_from, '=', res[1], currency_to)
        variable1 = round(res[0], 2)
        variable2 = currency_to
        st.write(
        f"<style>body {{ font-size: 20px; }}</style>"
        f"{variable1} {variable2}",
        unsafe_allow_html=True)
        st.divider()