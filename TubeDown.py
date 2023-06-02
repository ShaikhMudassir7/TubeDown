from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.app import App
from pytube import YouTube
from tkinter import filedialog, messagebox
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.selectioncontrol import MDCheckbox

path1 = ""

class DownTube(MDApp):
    def browse_directory(self):
        global path1
        path1 = filedialog.askdirectory()
        self.root.ids.lbl_path_show.text = f"Path: {path1}"
        if len(path1) < 1:
            messagebox.showerror("Error", "Please select a directory")

    def download_video(self):
        url = self.root.ids.ent_link.text
        res = self.root.ids.res1.active
        audio_only = self.root.ids.audio_radio.active

        if len(url) < 1:
            messagebox.showerror("Error", "URL cannot be empty")

        yt = YouTube(url)
        try:
            if res:
                reso_select = yt.streams.get_highest_resolution()
            else:
                reso_select = yt.streams.get_lowest_resolution()

            if audio_only:
                reso_select = yt.streams.filter(only_audio=True).first()

            try:
                reso_select.download(path1)
                messagebox.showinfo("Success", "Video Downloaded!")
                messagebox.showinfo("Follow Me", "For more stuff like this, follow me")
            except:
                messagebox.showerror("Error", "Download failed")
        except:
            messagebox.showerror("Error", "Please try again")

    def build(self):
        self.title = "DownTube"
        self.root = Builder.load_string('''
BoxLayout:
    orientation: "vertical"
    padding: "20dp"
    spacing: "10dp"
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        size_hint_y: None
        height: self.minimum_height

        MDLabel:
            text: "DownTube – By Shaikh Mudassir"
            font_style: "H2"
            theme_text_color: "Secondary"
            halign: "center"



    BoxLayout:
        orientation: "horizontal"
        spacing: "10dp"

        MDLabel:
            text: "Link"
            theme_text_color: "Secondary"

        MDTextField:
            id: ent_link
            font_size: "14sp"
            mode: "fill"

    BoxLayout:
        orientation: "horizontal"
        spacing: "10dp"

        MDLabel:
            text: "Path"
            theme_text_color: "Secondary"

        MDRaisedButton:
            text: "Browse"
            on_release: app.browse_directory()

    MDLabel:
        id: lbl_path_show
        text: "Path: "
        theme_text_color: "Secondary"
        font_style: "Caption"

    MDLabel:
        text: "Select Quality"
        theme_text_color: "Secondary"

    MDLabel:
        text: "Note: By default, the quality will be set to Highest"
        theme_text_color: "Secondary"
        font_style: "Caption"

    BoxLayout:
        orientation: "horizontal"
        spacing: "10dp"

        MDCheckbox:
            id: res1
            group: "res"
            size_hint: None, None
            size: "24dp", "24dp"
            active: True
            theme_text_color: "Secondary"

        MDLabel:
            text: "High"
            theme_text_color: "Secondary"
            font_style: "Caption"

        MDCheckbox:
            id: res2
            group: "res"
            size_hint: None, None
            size: "24dp", "24dp"
            theme_text_color: "Secondary"

        MDLabel:
            text: "Low"
            theme_text_color: "Secondary"
            font_style: "Caption"

    BoxLayout:
        orientation: "horizontal"
        spacing: "10dp"

        MDCheckbox:
            id: audio_radio
            group: "audio"
            size_hint: None, None
            size: "24dp", "24dp"
            theme_text_color: "Secondary"

        MDLabel:
            text: "Audio Only"
            theme_text_color: "Secondary"
            font_style: "Caption"

    MDRaisedButton:
        text: "Download"
        size_hint: None, None
        size: "160dp", "48dp"
        pos_hint: {"center_x": 0.5}
        font_size: "16sp"
        md_bg_color: 0, 0.8, 0.8, 1
        text_color: 1, 1, 1, 1
        on_release: app.download_video()
''')
        return self.root


DownTube().run()
