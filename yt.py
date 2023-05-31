from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from pytube import YouTube

class VideoDownloaderApp(MDApp):
    selected_path = ""
    selected_resolution = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.url_textfield = None
        self.resolution_textfield = None

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"

        main_layout = BoxLayout(orientation="vertical", spacing="10dp", padding="10dp")

        heading_label = MDLabel(text="Video Downloader", font_style="H5", theme_text_color="Secondary")
        main_layout.add_widget(heading_label)

        self.url_textfield = MDTextField(hint_text="URL", required=True)
        main_layout.add_widget(self.url_textfield)

        browse_button = MDFlatButton(text="Browse", on_release=self.browse_directory)
        main_layout.add_widget(browse_button)

        self.resolution_textfield = MDTextField(hint_text="Select Quality", required=True)
        main_layout.add_widget(self.resolution_textfield)

        download_button = MDFlatButton(text="Download", on_release=self.download_video)
        main_layout.add_widget(download_button)

        return main_layout

    def browse_directory(self, instance):
        manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path
        )
        manager.show('/')

    def exit_manager(self, *args):
        self.file_manager.close()

    def select_path(self, path):
        self.selected_path = path
        self.file_manager.close()

    def download_video(self, instance):
        url = self.url_textfield.text
        resolution = self.resolution_textfield.text

        if not url or not resolution:
            self.show_error_dialog("Error", "URL and Resolution are required.")
            return

        try:
            yt = YouTube(url)
            if resolution.lower() == "highest":
                self.selected_resolution = yt.streams.get_highest_resolution()
            elif resolution.lower() == "lowest":
                self.selected_resolution = yt.streams.get_lowest_resolution()
            elif resolution.lower() == "audio":
                self.selected_resolution = yt.streams.filter(only_audio=True).first()
            else:
                self.show_error_dialog("Error", "Invalid resolution.")
                return

            self.selected_resolution.download(self.selected_path)

            self.show_info_dialog("Success", "Video Downloaded!")
        except Exception as e:
            self.show_error_dialog("Error", str(e))

    def show_error_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            buttons=[
                MDFlatButton(text="OK", on_release=self.close_dialog)
            ]
        )
        dialog.open()

    def show_info_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            buttons=[
                MDFlatButton(text="OK", on_release=self.close_dialog)
            ]
        )
        dialog.open()

    def close_dialog(self, instance):
        instance.parent.parent.parent.dismiss()

if __name__ == "__main__":
    VideoDownloaderApp().run()
