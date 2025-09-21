from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.clock import Clock

from plyer import notification, vibrator

from bot_logic import get_signals_and_data
from charting import plot_chart
from fundamentals import get_latest_news


class TradingUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.label = Label(
            text="Robot Trading Live\nAuto Update tiap 30 detik + Notifikasi",
            halign="center"
        )
        self.add_widget(self.label)

        self.timeframe_spinner = Spinner(
            text="15m",
            values=("1m","5m","15m","1h","4h","1d"),
            size_hint=(1, 0.2)
        )
        self.add_widget(self.timeframe_spinner)

        btn_refresh = Button(text="Analisa Sekarang", size_hint=(1, 0.2))
        btn_refresh.bind(on_press=self.update_signals)
        self.add_widget(btn_refresh)

        self.scroll = ScrollView(size_hint=(1, 0.4))
        self.results = Label(text="Belum ada sinyal", halign="left", valign="top")
        self.results.bind(size=self.results.setter('text_size'))
        self.scroll.add_widget(self.results)
        self.add_widget(self.scroll)

        self.chart_box = BoxLayout(size_hint=(1, 1))
        self.add_widget(self.chart_box)

        # simpan sinyal lama
        self.last_signals = ""

        # Auto refresh tiap 30 detik
        Clock.schedule_interval(self.auto_update, 30)

    def auto_update(self, dt):
        self.update_signals(None)

    def update_signals(self, instance):
        timeframe = self.timeframe_spinner.text
        signals, data_dict, entries = get_signals_and_data(timeframe)

        # ambil berita fundamental
        news = get_latest_news()

        # update teks
        self.results.text = f"{signals}\n\n[Fundamental Terbaru]\n{news}"

        # cek sinyal baru
        if signals != self.last_signals:
            self.send_alert("Sinyal Trading Baru", "Cek chart untuk entry!")
            self.last_signals = signals

        # update chart
        self.chart_box.clear_widgets()
        if "BTC/USDT" in data_dict:
            fig = plot_chart("BTC/USDT", data_dict["BTC/USDT"], entries.get("BTC/USDT"))
            self.chart_box.add_widget(FigureCanvasKivyAgg(fig))

    def send_alert(self, title, message):
        try:
            notification.notify(title=title, message=message, timeout=5)
            vibrator.vibrate(1)  # getar 1 detik
        except Exception as e:
            print(f"Notifikasi error: {e}")


class TradingApp(App):
    def build(self):
        return TradingUI()


if __name__ == '__main__':
    TradingApp().run()
