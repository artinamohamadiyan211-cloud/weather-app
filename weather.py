# import requests
# from customtkinter import *
# from PIL  import Image,ImageTk
# import time
# api,json="",""
# # print(round(json['main']['temp']))

# root=CTk()
# root.title("weather")
# root.geometry("400x665+950+20")
# set_appearance_mode("light")
# root.resizable(False,False)
# f=("arial",20,"bold")
# ##function
# def getcity():
#     canvas.delete("moon")
#     canvas.delete("sun")
#     canvas.delete("suncloud")
#     canvas.delete("haze")
#     canvas.delete("rain")
#     canvas.delete("snow")
#     canvas.delete("q")
#     global api,json
#     api=requests.get("http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API key}")
#     api = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
#                         + cityent.get() + "&units=metric&appid="+"29171285ba661813da249648693cfaf7")
#     json=api.json()
#     lon=json["coord"]["lon"]
#     lat=json["coord"]["lat"]
#     aqi=requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid=29171285ba661813da249648693cfaf7")
#     j=aqi.json()
#     citynamelbl.configure(text=f"{cityent.get()}/{json["sys"]["country"]}")
#     templbl.configure(text=str(round(json['main']['temp']))+"°")
#     mainlbl.configure(text=json["weather"][0]["main"])
#     print(json["weather"][0]["main"])
#     feellbl.configure(text=f"feels like : {round(json['main']['feels_like'])}°")
#     humiditylbl.configure(text=f"humidity: {json["main"]["humidity"]}")
#     if j["list"][0]["main"]["aqi"] == 1:
#         aqilbl.configure(text="good")
#         progressaqi.set(0.25)
#         progressaqi.configure(progress_color="green")
#     elif j["list"][0]["main"]["aqi"] == 2:
#         aqilbl.configure(text="moderate")
#         progressaqi.set(0.5)
#         progressaqi.configure(progress_color="yellow")
#     elif j["list"][0]["main"]["aqi"] == 3:
#         aqilbl.configure(text="unhealthy")
#         progressaqi.set(0.75)
#         progressaqi.configure(progress_color="orange")    
#     else:
#         aqilbl.configure(text="hazardous")
#         progressaqi.configure(progress_color="red")   
#         progressaqi.set(1)
#     if json["sys"]["sunrise"] <time.time() <json["sys"]["sunset"]:
#         canvas.configure(bg="#6AC9EE")
#         citynamelbl.configure(fg_color="#6AC9EE")
#         templbl.configure(fg_color="#6AC9EE")
#         feellbl.configure(fg_color="#6AC9EE")
#         humiditylbl.configure(fg_color="#6AC9EE")
#         mainlbl.configure(fg_color="#6AC9EE")
#         aqilbl.configure(fg_color="#6AC9EE")
#         citylbl.configure(fg_color="#6AC9EE")
#         gobtn.configure(fg_color="#6AC9EE",bg_color="#6AC9EE")
#         if  json["weather"][0]["main"] =="Clear":
#             canvas.create_image(200,150,image=sunimage,tag="sun")
#             return
#     else:
#         canvas.configure(bg="#041A40")
#         citynamelbl.configure(fg_color="#041A40")
#         templbl.configure(fg_color="#041A40")
#         feellbl.configure(fg_color="#041A40")
#         humiditylbl.configure(fg_color="#041A40")
#         aqilbl.configure(fg_color="#041A40")
#         mainlbl.configure(fg_color="#041A40")
#         citylbl.configure(fg_color="#041A40")
#         gobtn.configure(fg_color="#041A40",bg_color="#041A40")
#         if  json["weather"][0]["main"] =="Clear":
#             canvas.create_image(200,150,image=moonimage,tag="moon")
#             return

#     if  json["weather"][0]["main"] =="Clouds":
#         canvas.create_image(200,150,image=suncloudimage,tag="suncloud")
#     elif  json["weather"][0]["main"] =="Haze":
#         canvas.create_image(200,150,image=fogimage,tag="haze")
#     elif  json["weather"][0]["main"] =="Rain":
#         canvas.create_image(200,150,image=cloudrainimage,tag="rain")
#     elif  json["weather"][0]["main"] =="Snow":
#         canvas.create_image(200,150,image=snowimage,tag="snow")
#     else:
#         canvas.create_image(200,150,image=qimage,tag="q")



    

#     # print(json)
# ##canvas
# canvas=CTkCanvas(root,width=400,height=665,bg="#6AC9EE",highlightthickness=0)
# canvas.pack()

# ##label
# citynamelbl=CTkLabel(canvas,text="----",font=f,fg_color="#6AC9EE",text_color="white")
# citynamelbl.place(x=170,y=20)

# templbl=CTkLabel(root,text="----",font=("arial",60,"bold"),fg_color="#6AC9EE",text_color="white")
# templbl.place(x=170,y=250)

# feellbl=CTkLabel(root,text="----",font=f,fg_color="#6AC9EE",text_color="white")
# feellbl.place(x=30,y=380)

# mainlbl=CTkLabel(root,text="----",font=f,fg_color="#6AC9EE",text_color="white")
# mainlbl.place(x=180,y=320)

# humiditylbl=CTkLabel(root,text="----",font=f,fg_color="#6AC9EE",text_color="white")
# humiditylbl.place(x=30,y=420)

# aqilbl=CTkLabel(root,text="----",font=f,fg_color="#6AC9EE",text_color="white")
# aqilbl.place(x=30,y=470)

# citylbl=CTkLabel(canvas,text="city:",font=f,fg_color="#6AC9EE",text_color="white")
# citylbl.place(x=80,y=630)
# ##entry
# cityent=CTkEntry(canvas,text_color="#71AEC6",font=f)
# cityent.insert(0,"tehran")
# cityent.place(x=150,y=630)

# ##progressbar

# progressaqi=CTkProgressBar(canvas)
# progressaqi.place(x=50,y=550)
# progressaqi.set(0)
# progressaqi.step()


# ##Button
# gobtn=CTkButton(canvas,text="Go",font=f,fg_color="#AAD7E9",text_color="white",hover_color="#ACDFF4",width=50,command=getcity)
# gobtn.place(x=310,y=630)
# ##photos
# sunimage=ImageTk.PhotoImage(Image.open("pic/1sunny.png").resize((200,200)))

# suncloudimage=ImageTk.PhotoImage(Image.open("pic/1partlysunny.png").resize((200,200)))

# moonimage=ImageTk.PhotoImage(Image.open("pic/1moon.png").resize((200,200)))

# cloudrainimage=ImageTk.PhotoImage(Image.open("pic/1cloudrain.png").resize((200,200)))

# fogimage=ImageTk.PhotoImage(Image.open("pic/1fog.png").resize((200,200)))

# snowimage=ImageTk.PhotoImage(Image.open("pic/1snow.png").resize((200,200)))

# windimage=ImageTk.PhotoImage(Image.open("pic/1wind.png").resize((200,200)))

# qimage=ImageTk.PhotoImage(Image.open("pic/q.png").resize((200,200)))


# getcity()

# root.mainloop()



from __future__ import annotations

import json
import os
import re
import sys
import threading
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import customtkinter as ctk
import requests
from PIL import Image

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #
BASE_DIR = Path(__file__).resolve().parent
SETTINGS_FILE = BASE_DIR / "settings.json"
API_URL = "https://api.openweathermap.org/data/2.5"
DEFAULT_CITY = "London"

if sys.platform.startswith("win"):
    FONT_FAMILY = "Segoe UI"
elif sys.platform == "darwin":
    FONT_FAMILY = "Helvetica Neue"
else:
    FONT_FAMILY = "DejaVu Sans"

THEMES = {
    "day": {
        "bg": "#4FB3E8",
        "card": "#6CC2EF",
        "text": "#FFFFFF",
        "sub": "#E3F4FD",
        "accent": "#2E8BC0",
    },
    "night": {
        "bg": "#0B1D3F",
        "card": "#162F5C",
        "text": "#FFFFFF",
        "sub": "#A8BADB",
        "accent": "#3A5FA8",
    },
}

AQI_LEVELS = {
    1: ("Good", 0.2, "#4CAF50"),
    2: ("Fair", 0.4, "#C0CA33"),
    3: ("Moderate", 0.6, "#FFB300"),
    4: ("Poor", 0.8, "#FB8C00"),
    5: ("Very poor", 1.0, "#E53935"),
}


def load_api_key() -> str | None:
    """Read the API key from the environment or from a local .env file."""
    key = os.getenv("OPENWEATHER_API_KEY")
    if key:
        return key.strip()
    env_file = BASE_DIR / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            name, _, value = line.partition("=")
            if name.strip() == "OPENWEATHER_API_KEY":
                return value.strip().strip("\"'")
    return None


def load_settings() -> dict:
    try:
        return json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_settings(data: dict) -> None:
    try:
        SETTINGS_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except OSError:
        pass


# --------------------------------------------------------------------------- #
# Data layer
# --------------------------------------------------------------------------- #
class WeatherError(Exception):
    """Raised with a user-friendly message when data can't be fetched."""


@dataclass
class DayForecast:
    day: date
    low: float
    high: float
    main: str


@dataclass
class Report:
    city: str
    country: str
    temp: float
    feels_like: float
    humidity: int
    wind: float          # m/s
    pressure: int        # hPa
    visibility_km: float
    description: str
    main: str
    sunrise: datetime
    sunset: datetime
    is_day: bool
    aqi: int | None
    forecast: list[DayForecast]


class WeatherService:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.session = requests.Session()

    def _get(self, endpoint: str, **params) -> dict:
        params.update(appid=self.api_key, units="metric")
        try:
            response = self.session.get(f"{API_URL}/{endpoint}", params=params, timeout=10)
        except requests.exceptions.ConnectionError:
            raise WeatherError("No internet connection.") from None
        except requests.exceptions.Timeout:
            raise WeatherError("The request timed out. Try again.") from None
        except requests.exceptions.RequestException:
            raise WeatherError("Network error. Try again.") from None

        if response.status_code == 401:
            raise WeatherError("Invalid API key (new keys can take up to 2 hours to activate).")
        if response.status_code == 404:
            raise WeatherError("City not found. Check the spelling.")
        if response.status_code == 429:
            raise WeatherError("Too many requests. Wait a minute and try again.")
        if not response.ok:
            raise WeatherError(f"Server error ({response.status_code}).")
        return response.json()

    def fetch(self, city: str) -> Report:
        current = self._get("weather", q=city)
        lat, lon = current["coord"]["lat"], current["coord"]["lon"]
        forecast_raw = self._get("forecast", lat=lat, lon=lon)

        try:
            aqi = self._get("air_pollution", lat=lat, lon=lon)["list"][0]["main"]["aqi"]
        except (WeatherError, KeyError, IndexError):
            aqi = None  # air quality is optional

        tz = timezone(timedelta(seconds=current.get("timezone", 0)))
        sunrise = datetime.fromtimestamp(current["sys"]["sunrise"], tz)
        sunset = datetime.fromtimestamp(current["sys"]["sunset"], tz)
        now = datetime.fromtimestamp(current["dt"], tz)

        days: dict[date, list[dict]] = defaultdict(list)
        for item in forecast_raw["list"]:
            days[datetime.fromtimestamp(item["dt"], tz).date()].append(item)

        forecast = []
        for day, items in list(days.items())[:5]:
            temps = [i["main"]["temp"] for i in items]
            main = Counter(i["weather"][0]["main"] for i in items).most_common(1)[0][0]
            forecast.append(DayForecast(day, min(temps), max(temps), main))

        return Report(
            city=current["name"],
            country=current["sys"].get("country", ""),
            temp=current["main"]["temp"],
            feels_like=current["main"]["feels_like"],
            humidity=current["main"]["humidity"],
            wind=current["wind"]["speed"],
            pressure=current["main"]["pressure"],
            visibility_km=current.get("visibility", 0) / 1000,
            description=current["weather"][0]["description"].capitalize(),
            main=current["weather"][0]["main"],
            sunrise=sunrise,
            sunset=sunset,
            is_day=sunrise <= now <= sunset,
            aqi=aqi,
            forecast=forecast,
        )


# --------------------------------------------------------------------------- #
# UI layer
# --------------------------------------------------------------------------- #
class WeatherApp(ctk.CTk):
    def __init__(self, service: WeatherService | None, problem: str = "") -> None:
        super().__init__()
        self.service = service
        self.problem = problem
        self.report: Report | None = None
        self.mode = "day"
        self.settings = load_settings()
        self.imperial = self.settings.get("units") == "imperial"
        self._image_cache: dict[tuple[str, int], ctk.CTkImage | None] = {}
        self._registry: dict[str, list] = {"bg": [], "card": [], "text": [], "sub": []}

        self.title("Weather Dashboard")
        self.geometry("440x740")
        self.resizable(False, False)

        self._build_fonts()
        self._build_ui()
        self.apply_theme("day")

        if self.service is None:
            self.show_status(
                self.problem or "No API key found. Add OPENWEATHER_API_KEY to a .env file.",
                error=True,
            )
            self.search_btn.configure(state="disabled")
        else:
            self.entry.insert(0, self.settings.get("city", DEFAULT_CITY))
            self.search()

    # ---- building ---------------------------------------------------------
    def _build_fonts(self) -> None:
        F = lambda size, weight="normal": ctk.CTkFont(family=FONT_FAMILY, size=size, weight=weight)
        self.f_city = F(28, "bold")
        self.f_temp = F(76, "bold")
        self.f_desc = F(16)
        self.f_title = F(12, "bold")
        self.f_value = F(18, "bold")
        self.f_small = F(12)
        self.f_ui = F(14)

    def _track(self, kind: str, widget):
        self._registry[kind].append(widget)
        return widget

    def _label(self, parent, kind="text", **kwargs) -> ctk.CTkLabel:
        label = ctk.CTkLabel(parent, fg_color="transparent", **kwargs)
        return self._track(kind, label)

    def _card(self, parent) -> ctk.CTkFrame:
        return self._track("card", ctk.CTkFrame(parent, corner_radius=18))

    def _build_ui(self) -> None:
        pad = {"padx": 20}

        # Search bar
        bar = self._track("bg", ctk.CTkFrame(self, fg_color="transparent"))
        bar.pack(fill="x", pady=(20, 10), **pad)
        self.entry = ctk.CTkEntry(
            bar, placeholder_text="Search city…", font=self.f_ui, height=38,
            corner_radius=12, border_width=0,
        )
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", lambda _e: self.search())
        self.search_btn = ctk.CTkButton(
            bar, text="Search", width=76, height=38, corner_radius=12,
            font=self.f_ui, command=self.search,
        )
        self.search_btn.pack(side="left", padx=(8, 0))
        self.unit_btn = ctk.CTkSegmentedButton(
            bar, values=["°C", "°F"], width=80, height=38, font=self.f_ui,
            command=self.set_units,
        )
        self.unit_btn.set("°F" if self.imperial else "°C")
        self.unit_btn.pack(side="left", padx=(8, 0))

        # Status line (right under the search bar so errors are always visible)
        self.status_lbl = self._label(self, "sub", font=self.f_small, text="", wraplength=400)
        self.status_lbl.pack(**pad)

        # Hero section
        self.city_lbl = self._label(self, font=self.f_city, text="—")
        self.city_lbl.pack(pady=(10, 0))
        self.desc_lbl = self._label(self, "sub", font=self.f_desc, text="")
        self.desc_lbl.pack()
        self.icon_lbl = self._label(self, text="")
        self.icon_lbl.pack(pady=(6, 0))
        self.temp_lbl = self._label(self, font=self.f_temp, text="--°")
        self.temp_lbl.pack()
        self.feels_lbl = self._label(self, "sub", font=self.f_desc, text="")
        self.feels_lbl.pack()

        # Detail tiles
        details = self._card(self)
        details.pack(fill="x", pady=(18, 10), **pad)
        for col in range(3):
            details.grid_columnconfigure(col, weight=1)
        self.tiles: dict[str, ctk.CTkLabel] = {}
        names = ["Humidity", "Wind", "Pressure", "Visibility", "Sunrise", "Sunset"]
        for i, name in enumerate(names):
            cell = ctk.CTkFrame(details, fg_color="transparent")
            cell.grid(row=i // 3, column=i % 3, pady=10, sticky="nsew")
            self._label(cell, "sub", font=self.f_title, text=name.upper()).pack()
            value = self._label(cell, font=self.f_value, text="--")
            value.pack()
            self.tiles[name] = value

        # Air quality
        aqi_card = self._card(self)
        aqi_card.pack(fill="x", pady=(0, 10), **pad)
        row = ctk.CTkFrame(aqi_card, fg_color="transparent")
        row.pack(fill="x", padx=16, pady=(12, 4))
        self._label(row, "sub", font=self.f_title, text="AIR QUALITY").pack(side="left")
        self.aqi_lbl = self._label(row, font=self.f_title, text="--")
        self.aqi_lbl.pack(side="right")
        self.aqi_bar = ctk.CTkProgressBar(aqi_card, height=8, corner_radius=4)
        self.aqi_bar.set(0)
        self.aqi_bar.pack(fill="x", padx=16, pady=(0, 14))

        # Forecast
        fc_card = self._card(self)
        fc_card.pack(fill="x", pady=(0, 10), **pad)
        self._label(fc_card, "sub", font=self.f_title, text="5-DAY FORECAST").pack(
            anchor="w", padx=16, pady=(12, 0)
        )
        strip = ctk.CTkFrame(fc_card, fg_color="transparent")
        strip.pack(fill="x", padx=8, pady=(4, 12))
        self.forecast_cells = []
        for col in range(5):
            strip.grid_columnconfigure(col, weight=1)
            cell = ctk.CTkFrame(strip, fg_color="transparent")
            cell.grid(row=0, column=col, sticky="nsew")
            day = self._label(cell, "sub", font=self.f_small, text="--")
            day.pack()
            icon = self._label(cell, text="")
            icon.pack(pady=2)
            hi = self._label(cell, font=self.f_title, text="--")
            hi.pack()
            lo = self._label(cell, "sub", font=self.f_small, text="--")
            lo.pack()
            self.forecast_cells.append((day, icon, hi, lo))

    # ---- theme ------------------------------------------------------------
    def apply_theme(self, mode: str) -> None:
        self.mode = mode
        t = THEMES[mode]
        self.configure(fg_color=t["bg"])
        for w in self._registry["bg"]:
            w.configure(fg_color="transparent")
        for w in self._registry["card"]:
            w.configure(fg_color=t["card"])
        for w in self._registry["text"]:
            w.configure(text_color=t["text"])
        for w in self._registry["sub"]:
            w.configure(text_color=t["sub"])
        self.entry.configure(fg_color=t["card"], text_color=t["text"],
                             placeholder_text_color=t["sub"])
        self.search_btn.configure(fg_color=t["accent"], hover_color=t["card"],
                                  text_color=t["text"])
        self.unit_btn.configure(fg_color=t["card"], selected_color=t["accent"],
                                selected_hover_color=t["accent"],
                                unselected_color=t["card"],
                                unselected_hover_color=t["bg"], text_color=t["text"])
        self.aqi_bar.configure(fg_color=t["bg"])

    # ---- images -----------------------------------------------------------
    @staticmethod
    def icon_name(main: str, is_day: bool) -> str:
        if main == "Clear":
            return "1sunny.png" if is_day else "1moon.png"
        if main == "Clouds":
            return "1partlysunny.png"
        if main in {"Rain", "Drizzle", "Thunderstorm"}:
            return "1cloudrain.png"
        if main == "Snow":
            return "1snow.png"
        if main in {"Haze", "Mist", "Fog", "Smoke", "Dust", "Sand", "Ash"}:
            return "1fog.png"
        return "q.png"

    def image(self, name: str, size: int) -> ctk.CTkImage | None:
        key = (name, size)
        if key not in self._image_cache:
            image = None
            for folder in (BASE_DIR / "pic", BASE_DIR):
                path = folder / name
                if path.exists():
                    img = Image.open(path)
                    image = ctk.CTkImage(light_image=img, dark_image=img, size=(size, size))
                    break
            self._image_cache[key] = image
        return self._image_cache[key]

    # ---- actions ----------------------------------------------------------
    def search(self) -> None:
        city = self.entry.get().strip()
        if not city or self.service is None:
            return
        self.search_btn.configure(state="disabled")
        self.show_status("Loading…")
        threading.Thread(target=self._worker, args=(city,), daemon=True).start()

    def _worker(self, city: str) -> None:
        try:
            report = self.service.fetch(city)
        except WeatherError as exc:
            self.after(0, self._on_error, str(exc))
        except Exception:  # unexpected API shape etc.
            self.after(0, self._on_error, "Something went wrong. Try again.")
        else:
            self.after(0, self._on_success, report)

    def _on_success(self, report: Report) -> None:
        self.report = report
        self.search_btn.configure(state="normal")
        self.show_status("")
        self.render()
        self._save()

    def _on_error(self, message: str) -> None:
        self.search_btn.configure(state="normal")
        self.show_status(message, error=True)

    def set_units(self, value: str) -> None:
        self.imperial = value == "°F"
        self._save()
        if self.report:
            self.render()

    def show_status(self, text: str, error: bool = False) -> None:
        colour = "#FFB4AB" if error else THEMES[self.mode]["sub"]
        self.status_lbl.configure(text=text, text_color=colour)

    def _save(self) -> None:
        if self.report:
            save_settings({
                "city": self.report.city,
                "units": "imperial" if self.imperial else "metric",
            })

    # ---- rendering --------------------------------------------------------
    def temp(self, celsius: float) -> str:
        value = celsius * 9 / 5 + 32 if self.imperial else celsius
        return f"{round(value)}°"

    def render(self) -> None:
        r = self.report
        self.apply_theme("day" if r.is_day else "night")

        self.city_lbl.configure(text=f"{r.city}, {r.country}")
        self.desc_lbl.configure(text=r.description)
        self.temp_lbl.configure(text=self.temp(r.temp))
        self.feels_lbl.configure(text=f"Feels like {self.temp(r.feels_like)}")
        self.icon_lbl.configure(image=self.image(self.icon_name(r.main, r.is_day), 150))

        wind = f"{r.wind * 2.237:.0f} mph" if self.imperial else f"{r.wind:.1f} m/s"
        vis = f"{r.visibility_km * 0.621:.1f} mi" if self.imperial else f"{r.visibility_km:.1f} km"
        values = {
            "Humidity": f"{r.humidity}%",
            "Wind": wind,
            "Pressure": f"{r.pressure} hPa",
            "Visibility": vis,
            "Sunrise": r.sunrise.strftime("%H:%M"),
            "Sunset": r.sunset.strftime("%H:%M"),
        }
        for name, value in values.items():
            self.tiles[name].configure(text=value)

        if r.aqi in AQI_LEVELS:
            label, progress, colour = AQI_LEVELS[r.aqi]
            self.aqi_lbl.configure(text=label)
            self.aqi_bar.configure(progress_color=colour)
            self.aqi_bar.set(progress)
        else:
            self.aqi_lbl.configure(text="Unavailable")
            self.aqi_bar.set(0)

        today = datetime.now(r.sunrise.tzinfo).date()
        for cell, fc in zip(self.forecast_cells, r.forecast):
            day, icon, hi, lo = cell
            day.configure(text="Today" if fc.day == today else fc.day.strftime("%a"))
            icon.configure(image=self.image(self.icon_name(fc.main, True), 36))
            hi.configure(text=self.temp(fc.high))
            lo.configure(text=self.temp(fc.low))


def main() -> None:
    api_key = load_api_key()
    problem = ""
    if api_key and not re.fullmatch(r"[0-9a-fA-F]{32}", api_key):
        problem = ("OPENWEATHER_API_KEY in .env is not a valid key. It must be only the "
                   "32-character key from openweathermap.org (My API keys), not a URL.")
        api_key = None
    service = WeatherService(api_key) if api_key else None
    WeatherApp(service, problem).mainloop()


if __name__ == "__main__":
    main()