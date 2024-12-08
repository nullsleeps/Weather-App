import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

API_KEY = 'ENTER_YOUR_API_KEY_HERE'
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city, api_key):
    try:
        response = requests.get(BASE_URL, params={'q': city, 'units': 'metric', 'appid': api_key})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching weather data: {e}")
        return None

def display_weather(city, weather_data, result_label, temp_label, icon_label):
    if weather_data and weather_data.get('cod') == 200:
        weather = weather_data['weather'][0]['main']
        temp = round(weather_data['main']['temp'])
        icon_code = weather_data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        
        logging.info(f"Weather data for {city} retrieved successfully.")

        result_label.config(text=f"The weather in {city} is: {weather}")
        temp_label.config(text=f"The temperature is: {temp}ºC")
        
        try:
            icon_image = Image.open(requests.get(icon_url, stream=True).raw)
            icon_image = icon_image.resize((100, 100), Image.Resampling.LANCZOS)
            icon_photo = ImageTk.PhotoImage(icon_image)
            icon_label.config(image=icon_photo)
            icon_label.image = icon_photo
        except Exception as e:
            logging.error(f"Error loading icon: {e}")
            icon_label.config(image="")
        
    else:
        logging.warning(f"No weather data found for {city}.")
        messagebox.showerror("Error", "No City Found or unable to retrieve data.")

def on_search_button_click(city_entry, result_label, temp_label, icon_label):
    city = city_entry.get().strip()
    
    if not city:
        logging.error("City name is empty. Exiting.")
        messagebox.showerror("Input Error", "City name cannot be empty.")
        return

    weather_data = get_weather_data(city, API_KEY)
    display_weather(city, weather_data, result_label, temp_label, icon_label)

def create_gui():
    window = tk.Tk()
    window.title("Weather App")
    window.geometry("650x650")
    window.config(padx=30, pady=30, bg="black")

    title_label = ttk.Label(window, text="Weather Forecast", font=("Garamond", 36, "bold"), foreground="white", background="black")
    title_label.grid(row=0, column=0, columnspan=2, pady=40)

    city_label = ttk.Label(window, text="Enter City:", font=("Georgia", 18), foreground="white", background="black")
    city_label.grid(row=1, column=0, padx=10, pady=10)

    style = ttk.Style()
    style.configure("Rounded.TEntry",
                    font=("Georgia", 18),
                    padding=10,
                    relief="flat",
                    background="white",
                    foreground="black",
                    borderwidth=1,
                    highlightthickness=0)

    city_entry = ttk.Entry(window, style="Rounded.TEntry")
    city_entry.grid(row=1, column=1, padx=10, pady=10)

    search_button = ttk.Button(window, text="Get Weather", command=lambda: on_search_button_click(city_entry, result_label, temp_label, icon_label))
    search_button.grid(row=2, column=0, columnspan=2, pady=25)
    search_button.configure(style="BaroqueButton.TButton")

    result_label = ttk.Label(window, text="", font=("Georgia", 20), foreground="white", background="black")
    result_label.grid(row=3, column=0, columnspan=2, pady=15)

    temp_label = ttk.Label(window, text="", font=("Georgia", 20), foreground="white", background="black")
    temp_label.grid(row=4, column=0, columnspan=2, pady=15)

    icon_label = ttk.Label(window, background="black")
    icon_label.grid(row=5, column=0, columnspan=2, pady=15)

    style.configure("BaroqueButton.TButton",
                    padding=15,
                    relief="flat",
                    background="black",
                    foreground="black",
                    font=("Georgia", 16, "bold"),
                    anchor="center")
    style.map("BaroqueButton.TButton",
              background=[('active', '#A0522D')],
              foreground=[('active', 'black')])

    window.mainloop()

if __name__ == "__main__":
    create_gui()
