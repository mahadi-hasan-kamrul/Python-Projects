#Fully Workable Youtube Video Downloader with Python

- Install yt-dlp \
- Download ffmepg from Here - https://github.com/BtbN/FFmpeg-Builds/releases \
- Download Exactly this one: ffmpeg-master-latest-win64-gpl-shared.zip \
- Extract it in the same folder of the Project \
- Rename the folder as ffmpeg \
- The path has to be defined into the code like this: 'project path\ffmpeg\bin\ffmpeg.exe' \

Role of ffmpeg: \
FFmpeg plays a crucial role in YouTube video downloading when using tools like yt-dlp. Here's a breakdown of its role: \

1. Stream Merging (Most Common Use Case) \
YouTube often provides: \
Video-only streams (high quality video without audio) \
Audio-only streams (high quality audio without video) \
FFmpeg combines  separate streams into a single playable  \

2. Format Conversion \
Converts downloaded videos to different formats: \
MP4 → WEBM, MOV, AVI, etc. \
Audio extraction (MP4 → MP3, WAV) \

3. Quality Optimization \
Adjusts bitrates, resolution, and framerates \
Optimizes file size vs quality balance \

4. Metadata Handling \
Adds title, artist, thumbnail, and other metadata to downloaded files \
Preserves YouTube's original metadata \

5. Repair and Processing \
Fixes corrupted downloads \
Trims/edits videos without re-encoding \

After running the project it will ask you the url and the location to save the file. \
Run and Enjoy \
