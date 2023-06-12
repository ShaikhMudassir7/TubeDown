
# TubeDown

TubeDown is a video downloading application built with Kivy and KivyMD that allows users to download videos from YouTube. It provides a user-friendly interface for entering the video URL, selecting the download quality, and specifying the download path.

## Features

- Video downloading from YouTube
- Option to select video quality
- Option to download only audio
- Browse and select download path
- User-friendly interface

## Requirements

- Python 3.6 or higher
- Kivy 2.0.0 or higher
- KivyMD 0.104.2 or higher
- pytube 10.5.0 or higher

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/DownTube.git

2. Install the required libraries:
   ```shell
   pip install kivy kivymd pytube

3. Run the application:
   ```shell
   python main.py

## Contact Information
For any questions or suggestions, please feel free to contact me:

- Name: Shaikh Mudassir 
- Email: send2mudassir@gmail.com
- LinkedIn: https://www.linkedin.com/in/shaikhmudassir7
- Website: https://shaikhmudassir7.github.io

## Modules Required

```python
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
```
## Program Output:
![Home Screen](output/op1)
![Downloaded](output/op1)
![Console](output/op1)
