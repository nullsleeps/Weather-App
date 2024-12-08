# Weather App
***This project is a Weather Application built using Python and the Tkinter library to provide a modern graphical user interface (GUI). The application retrieves and displays weather information such as temperature, weather conditions, and an icon representing the current weather in a given city. The app uses the OpenWeatherMap API to fetch weather data and displays it in an intuitive, easy-to-use interface.***

`---------------------------------------------------------------------------------------------`

*The GUI Might not be the best, But hey, It works.*

`---------------------------------------------------------------------------------------------`

***Prerequisites***

**To use this application, you will need:**
```yaml
Python 3.x installed on your computer.
An internet connection to fetch the weather data from the OpenWeatherMap API.
```

***Installation***

***With Git***
**Clone the Repository:**
*Open a terminal and clone the repository to your local machine:*
```bash
git clone https://github.com/nullsleeps/Weather-App.git
cd weather-app
```

***From Giithub***

*Go to the top of the page and click on code, Then download ZIP*

*Extract the folder and open CMD in that folder*


**Get Your OpenWeatherMap API Key:**

*Sign up on OpenWeatherMap to get your free API key.*

*Once you have your API key, replace the placeholder in the code:*

```python
API_KEY = 'ENTER_YOUR_API_KEY_HERE'
```

**Run the Application:**

*Once the dependencies are installed and the API key is set up, run the application:*
```bash
python weather_app.py
```
`The GUI window will open, and you can enter a city name to get the current weather.`

`---------------------------------------------------------------------------------------------`

***Usage***


**1.** **Enter a City Name:**

*In the input field at the top of the window, type the name of a city (e.g., "Alberta").*

**2.** **Click 'Get Weather':**

*After typing the city name, click the "Get Weather" button to retrieve the current weather information for that city.*

**3.** **View the Results:**

*The weather information, including temperature (in Celsius) and weather conditions (e.g., sunny, cloudy, rainy), will be displayed below. Additionally, a corresponding weather icon will appear next to the details.*

**4.** **Error Handling:**

*If the entered city is not found or there’s an issue with the request, an error message will appear to inform the user.*


`---------------------------------------------------------------------------------------------`

**Features**


**1.** ***Real-time Weather Data:***

`Fetches and displays current weather conditions including temperature (in Celsius) and weather description (e.g., sunny, cloudy, rainy, etc.).`


**2.** ***Weather Icon:***

`Displays a dynamic weather icon based on the current conditions in the city.`


**3.** ***Search Functionality:***

`Users can enter any city name to get live weather updates.`


**4.** ***User-friendly Interface:***

`Simple and intuitive GUI built with Tkinter, making it easy for anyone to check the weather with just a few clicks.`


**5.** ***Error Handling:***

`Provides clear error messages when there’s an issue with the city name (e.g., city not found or API error).`


**But Most of all, Have fun :)**
