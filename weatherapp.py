import requests
import streamlit as st

api_key = "Your api key"


def convert_to_celcius(temperature_in_kelvin):
    return temperature_in_kelvin - 273.15


def find_weather(city):

    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
    data = response.json()

    try:
        general = data['weather'][0]['main']
        icon_id = data['weather'][0]['icon']
        temperature = round(convert_to_celcius(data['main']['temp']))
        icon = f'https://openweathermap.org/img/wn/{icon_id}@4x.png'
    except KeyError:
        st.error("City Not Found")
        st.stop()
    return general,temperature,icon


def main():

    st.header("Find the Weather")
    city = st.text_input("Enter the City ").lower()
    if st.button("find"):
        general, temperature, icon = find_weather(city)
        col_1,col_2=st.columns(2)
        with col_1:
            st.metric(label='Temperature',value=f'{temperature}℃ ')
        with col_2:
            st.write(general)
            st.image(icon)




if __name__ == '__main__':
    main()
