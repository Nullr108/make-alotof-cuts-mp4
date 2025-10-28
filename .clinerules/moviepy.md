# Описание модуля MoviePy

## Назначение
Библиотека для редактирования видео: нарезка, склейка, обработка, добавление эффектов.

## Структура модуля
```
moviepy/
├── __init__.py
├── Clip.py
├── config.py
├── decorators.py
├── Effect.py
├── tools.py
├── version.py
├── audio/
│   ├── __init__.py
│   ├── AudioClip.py
│   ├── fx/
│   │   ├── __init__.py
│   │   ├── AudioDelay.py
│   │   ├── AudioFadeIn.py
│   │   ├── AudioFadeOut.py
│   │   ├── AudioLoop.py
│   │   ├── AudioNormalize.py
│   │   ├── MultiplyStereoVolume.py
│   │   └── MultiplyVolume.py
│   ├── io/
│   │   ├── __init__.py
│   │   ├── AudioFileClip.py
│   │   ├── ffmpeg_audiowriter.py
│   │   ├── ffplay_audiopreviewer.py
│   │   └── readers.py
│   └── tools/
│       ├── __init__.py
│       └── cuts.py
└── video/
    ├── __init__.py
    ├── VideoClip.py
    ├── compositing/
    │   ├── __init__.py
    │   └── CompositeVideoClip.py
    ├── fx/
    │   ├── __init__.py
    │   ├── AccelDecel.py
    │   ├── BlackAndWhite.py
    │   ├── Blink.py
    │   ├── Crop.py
    │   ├── CrossFadeIn.py
    │   ├── CrossFadeOut.py
    │   ├── EvenSize.py
    │   ├── FadeIn.py
    │   ├── FadeOut.py
    │   ├── Freeze.py
    │   ├── FreezeRegion.py
    │   ├── GammaCorrection.py
    │   ├── HeadBlur.py
    │   ├── InvertColors.py
    │   ├── Loop.py
    │   ├── LumContrast.py
    │   ├── MakeLoopable.py
    │   ├── Margin.py
    │   ├── MaskColor.py
    │   ├── MasksAnd.py
    │   ├── MasksOr.py
    │   ├── MirrorX.py
    │   ├── MirrorY.py
    │   ├── MultiplyColor.py
    │   ├── MultiplySpeed.py
    │   ├── Painting.py
    │   ├── Resize.py
    │   ├── Rotate.py
    │   ├── Scroll.py
    │   ├── SlideIn.py
    │   ├── SlideOut.py
    │   ├── SuperSample.py
    │   ├── TimeMirror.py
    │   └── TimeSymmetrize.py
    ├── io/
    │   ├── __init__.py
    │   ├── display_in_notebook.py
    │   ├── ffmpeg_reader.py
    │   ├── ffmpeg_tools.py
    │   ├── ffmpeg_writer.py
    │   ├── ffplay_previewer.py
    │   ├── gif_writers.py
    │   ├── ImageSequenceClip.py
    │   └── VideoFileClip.py
    └── tools/
        ├── __init__.py
        ├── credits.py
        ├── cuts.py
        ├── drawing.py
        ├── interpolators.py
        └── subtitles.py
```

## Спецификация API
### Основные классы:
- `Clip` - базовый класс для всех медиа-клипов
- `AudioClip` - работа с аудио дорожками
- `VideoClip` - обработка видео
- `CompositeVideoClip` - композиция нескольких клипов

### Ключевые методы:
- `subclip(start, end)` - вырезка фрагмента
- `write_videofile(filename)` - экспорт видео
- `fx()` - применение эффектов
- `set_audio()` - добавление аудио
- `resize()` - изменение размера

### Обработка ошибок:
Модуль использует исключения:
- `MoviePyError` - базовый класс ошибок
- `DurationError` - проблемы с длительностью клипа
- `ParameterError` - неверные параметры


## Основные компоненты
- `Clip.py` - базовый класс для всех клипов
- `AudioClip.py` и `VideoClip.py` - специализированные клипы
- Модули fx - эффекты для аудио и видео
- Модули io - работа с файлами разных форматов

## Примеры использования

### Базовый пример - нарезка видео
```python
from moviepy.editor import *

video = VideoFileClip("my_video.mp4")
short_clip = video.subclip(10, 20)  # Вырезать с 10 по 20 секунду
short_clip.write_videofile("short.mp4")
```

### Добавление текста и эффектов
```python
from moviepy.editor import *

clip = VideoFileClip("video.mp4")
txt_clip = TextClip("Hello World!", fontsize=70, color='white')
txt_clip = txt_clip.set_pos('center').set_duration(5)

video = CompositeVideoClip([clip, txt_clip])
video.fx(vfx.fadein, 1).fx(vfx.fadeout, 1).write_videofile("result.mp4")
```

### Склейка нескольких видео
```python
from moviepy.editor import *

clip1 = VideoFileClip("video1.mp4")
clip2 = VideoFileClip("video2.mp4")
final_clip = concatenate_videoclips([clip1, clip2])
final_clip.write_videofile("combined.mp4")
```

### Работа с аудио
```python
from moviepy.editor import *

video = VideoFileClip("video.mp4")
audio = AudioFileClip("music.mp3").subclip(0, video.duration)
video = video.set_audio(audio)
video.write_videofile("video_with_music.mp4")
```

### Создание слайд-шоу из изображений
```python
from moviepy.editor import *

images = ["img1.jpg", "img2.jpg", "img3.jpg"]
clips = [ImageClip(m).set_duration(3) for m in images]
video = concatenate_videoclips(clips, method="compose")
video.write_videofile("slideshow.mp4", fps=24)
```

## Управление зависимостями
Требования зафиксированы в файле `requirements.txt`:
```
numpy>=1.21.0
decorator>=5.0.0
imageio>=2.9.0
proglog>=0.1.9
ffmpeg-python>=0.2.0
requests>=2.25.1
```

## Организация тестов
Модуль содержит папку `tests/` с тестами, написанными на pytest:
```
tests/
├── __init__.py
├── test_audio.py
└── test_video.py
```

## Конфигурация
Файл `config.json` в корне модуля содержит настройки:
```json
{
    "module_rules": {
        "require_init": true,
        "test_coverage": 80,
        "style_check": true
    },
    "logging": {
        "level": "INFO",
        "format": "%(asctime)s - %(levelname)s - %(message)s"
    },
    "performance": {
        "cache_size": 1000,
        "timeout": 60
    }
}
```

## Покрытие тестами
Модуль имеет покрытие тестами более 80%, что проверяется с помощью:
```bash
pytest --cov=moviepy --cov-report=term-missing
```

## Логирование
Используется встроенная система логирования с настройками:
- Уровень логирования: INFO
- Формат сообщений: "%(asctime)s - %(levelname)s - %(message)s"
- Обработчики: FileHandler, StreamHandler
