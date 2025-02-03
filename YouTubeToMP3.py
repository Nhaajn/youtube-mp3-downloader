import yt_dlp
import os
from pydub import AudioSegment

def download_audio(url, output_folder="downloads"):
    try:
        # Tạo thư mục nếu chưa có
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Cấu hình yt-dlp để tải audio
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Tải xuống thành công!")

    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    video_url = input("Nhập URL YouTube: ")
    download_audio(video_url)
