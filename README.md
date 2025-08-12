# Python-Projects
## This repository shoecases some of the python projects of mine.
### Enjoy running the projects........ 

# Project 1: Project AI Agent with Python
Framework used in this project: Lang Chain \
LLMs used in this project: Calude, ChatGPT 

Use requirements.txt to install langchain wikipedia langchain-community langchain-openai langchain-anthropic python-dotenv pydantic duckduckgo-search 

For ChatGPT API Key: https://platform.openai.com/api-keys \
For Calude API Key: https://console.anthropic.com/settings/keys \
In this both you can use what ever you want \
## **For apis, we need to buy credit otherwise the api will not work** 

in tools.py we will add prebuild tools, one for looking in wikipedia, one to go in duckduckgo to search something, another is a custom tool \
Tools can be used freely. But can not be used too much


# Project 2: Basic games project with Python

## 1. Simple Quize Game
## 2. Rock, Paper, Scissor Gmae with Computer

# Project 3: Fully Workable Youtube Video Downloader with Python

- Install yt-dlp 
- Download ffmepg from Here - https://github.com/BtbN/FFmpeg-Builds/releases 
- Download Exactly this one: ffmpeg-master-latest-win64-gpl-shared.zip 
- Extract it in the same folder of the Project 
- Rename the folder as ffmpeg 
- The path has to be defined into the code like this: 'project path\ffmpeg\bin\ffmpeg.exe' 

### Role of ffmpeg: 
### **ffmpeg plays a crucial role in YouTube video downloading when using tools like yt-dlp**. Here's a breakdown of its role: 

1. Stream Merging (Most Common Use Case) \
YouTube often provides: \
Video-only streams (high quality video without audio) \
Audio-only streams (high quality audio without video) \
FFmpeg combines  separate streams into a single playable  

2. Format Conversion \
Converts downloaded videos to different formats: \
MP4 → WEBM, MOV, AVI, etc. \
Audio extraction (MP4 → MP3, WAV) 

3. Quality Optimization \
Adjusts bitrates, resolution, and framerates \
Optimizes file size vs quality balance 

4. Metadata Handling \
Adds title, artist, thumbnail, and other metadata to downloaded files \
Preserves YouTube's original metadata 

5. Repair and Processing \
Fixes corrupted downloads \
Trims/edits videos without re-encoding 

** After running the project it will ask you the url and the location to save the file. **


# Project 4: Automate Finance with Python, Pandas, Streamlit and Plotpy

This projects aim to showcase your bank transactions in a very efficent and productive way \
For this I have used a dummy data which is given in the folder as .csv file.\
Here we will catch the category for a prticular product which will then be used automatically when that product will be called.\
**First install Stramlit, Numpy, Pandas, Plotly**

The app will be run by Streamlit. It keeps the python scripts running all the time \
From Terminal write streamlit run xyz.py (the main file) \
It will run on 8501 port \
With streamlit, we will make the project look good and productive 

Important lines are commented in the code. \
**This is an one of a kind project with streamlit. Just had a great fun doing it.**
## To run the project: **streamlit run automate_finance.py**

# Project 5: Single Queue Simulation Math Problem Solved with Python
## Detail of the pre defined problem can be found in the pdf file inside the project folder

# Project 6: Slot Machine (betting) Project with Python

## It mimics a slot machine with 3 rows and 3columns
The Symblos are also defined in the coding.\
With deposit() function, we will get the user's balance.\
With lines() function, we will get the number of lines in which the user will gonna bet on.\
With bet() function, we will get the amount which the user wants to bet on each line. The total bet amount has to be equal or less than the users balance.\
with get_slot_machine_spin(rows, cols, symbols) we are defining the spin. we will pass our row, col, and symbol list in this function. Check code.\
def print_slot_machine() we will print the slot machine.\
def spin() will initialize a  game.\
def main() will start everything, it will take the deposit amount, then the play will start and it will end untill the deposit amount vanishes. The user can quit any time.\
## **  Slot machine is a complex architecture. Here, Tried to initiate the project in a very simple manner. **
