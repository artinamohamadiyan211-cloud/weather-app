# Weather App

A feature-rich desktop weather application built with **Python** and **CustomTkinter**, powered by the **OpenWeatherMap API**.

The application provides real-time weather information, a 5-day forecast, air quality data, and a responsive graphical interface with automatic day/night themes.

## Features

### Weather Information
- Current temperature and feels-like temperature.
- Weather descriptions and conditions.
- Humidity, wind speed, atmospheric pressure and visibility.
- Local sunrise and sunset times.
- 5-day weather forecast with daily high and low temperatures.
- Air Quality Index (AQI) with colour-coded categories.

### User Experience
- Search for cities using the search button or Enter key.
- Switch between Celsius and Fahrenheit.
- Automatic conversion of wind speed (m/s ↔ mph) and visibility (km ↔ miles).
- Automatic day/night theme based on the searched city's local sunrise and sunset.
- Custom weather icons for sunny, cloudy, rainy, snowy and foggy conditions.
- Remembers the last searched city and preferred temperature unit between sessions.
- Platform-specific fonts for Windows and macOS.

### Reliability and Performance
- Background threading for network requests to prevent UI freezing.
- Error handling for invalid cities, API authentication failures, network issues, timeouts and rate limits.
- API key validation to detect malformed credentials.
- Optional air quality requests, ensuring the main weather information remains available if AQI data cannot be retrieved.

### Code Quality
- Separation of the data and UI layers using `WeatherService` and `WeatherApp`.
- Dataclass models for weather reports and forecasts.
- Type hints throughout the codebase.
- API credentials loaded from environment variables rather than hard-coded into the source code.

## Technologies Used

- **Python** – Core programming language.
- **CustomTkinter** – Modern graphical user interface.
- **Requests** – HTTP requests and API integration.
- **Pillow (PIL)** – Image processing and weather icons.
- **OpenWeatherMap API** – Weather forecasts and air quality data.
- **Threading** – Non-blocking network operations.
- **JSON** – Persistent application settings.

## Project Structure

```text
weather-app/
│
├── weather.py
├── .gitignore
├── settings.json
├── pic/
│   ├── 1cloudrain.png
│   ├── 1fog.png
│   ├── 1moon.png
│   ├── 1partlysunny.png
│   ├── 1snow.png
│   ├── 1sunny.png
│   ├── 1wind.png
│   └── q.png
│
└── README.md
```

*Note: settings.json is generated or updated by the application when saving user preferences.*

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/artinamohamadiyan211-cloud/weather-app.git
```

### 2. Navigate to the project directory

```bash
cd weather-app
```

### 3. Install dependencies

```bash
python -m pip install customtkinter requests pillow
```

### 4. Configure your API key

Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).

Store your API key in a `.env` file or environment variable, using the variable name expected by the application.

**Important:** Never commit your API key or `.env` file to GitHub.

### 5. Run the application

```bash
python weather.py
```

##  Security

API credentials are kept outside the source code and excluded from version control through `.gitignore`.

##  Future Improvements

- Weather alerts and severe weather notifications.
- Weather data visualisation.
- More detailed forecast information.
- Additional UI customisation options.

## 👩 Author

**Artina Mohammadiyan**

Computer Science Student | Python Developer

[GitHub Profile](https://github.com/artinamohamadiyan211-cloud)

---

*Built with Python, curiosity, and a passion for software development.*