import os
import subprocess
from datetime import datetime

def time_to_seconds(t: str) -> int:
    """Преобразует строку времени (чч:мм:сс) в секунды"""
    try:
        parts = list(map(int, t.strip().split(':')))
        if len(parts) != 3 or parts[1] > 59 or parts[2] > 59:
            raise ValueError
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    except:
        raise ValueError(f"Некорректный формат времени: {t}. Используйте ЧЧ:ММ:СС")

def cut_video_by_timestamps(video_path: str, timestamps: str, output_dir: str = "clips"):
    times = timestamps.split(",")
    if len(times) < 2:
        print("Нужно минимум два таймкода для нарезки.")
        return

    os.makedirs(output_dir, exist_ok=True)
    
    ffmpeg_path = r"C:\Users\hero1\Downloads\ffmpeg-2025-05-29-git-75960ac270-full_build\bin\ffmpeg.exe"
    
    if not os.path.exists(ffmpeg_path):
        raise FileNotFoundError(f"FFmpeg не найден по пути: {ffmpeg_path}")

    for i in range(len(times) - 1):
        start = time_to_seconds(times[i])
        end = time_to_seconds(times[i + 1])
        output_path = os.path.join(output_dir, f"clip_{i + 1}.mp4")
        
        try:
            cmd = [
                ffmpeg_path,
                '-i', video_path,
                '-ss', str(start),
                '-to', str(end),
                '-c:v', 'libx264',
                '-c:a', 'aac',
                output_path
            ]
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при обработке отрезка {i+1}: {e}")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")

if __name__ == "__main__":
    cut_video_by_timestamps("input.mp4", "00:00:10,00:00:30")
