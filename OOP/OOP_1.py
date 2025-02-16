from abc import ABC, abstractmethod
from datetime import datetime


# Базовый класс для всех медиафайлов
class MediaFile(ABC):
    def __init__(self, name, size, owner, created_at=None):
        self.name = name
        self.size = size
        self.owner = owner
        self.created_at = created_at or datetime.now()

    @abstractmethod
    def save(self):
        """Сохранение файла"""
        pass

    @abstractmethod
    def delete(self):
        """Удаление файла"""
        pass

    def rename(self, new_name):
        """Переименование файла"""
        self.name = new_name


# Классы для конкретных типов медиа-файлов
class AudioFile(MediaFile):
    def __init__(self, name, size, owner, duration, format):
        super().__init__(name, size, owner)
        self.duration = duration
        self.format = format

    def save(self):
        # Логика сохранения аудиофайла
        pass

    def delete(self):
        # Логика удаления аудиофайла
        pass

    def convert(self, new_format):
        """Конвертация аудио в другой формат"""
        pass


class VideoFile(MediaFile):
    def __init__(self, name, size, owner, resolution, format):
        super().__init__(name, size, owner)
        self.resolution = resolution
        self.format = format

    def save(self):
        pass

    def delete(self):
        pass

    def extract_frames(self):
        """Извлечение кадров из видео"""
        pass


class PhotoFile(MediaFile):
    def __init__(self, name, size, owner, resolution, format):
        super().__init__(name, size, owner)
        self.resolution = resolution
        self.format = format

    def save(self):
        pass

    def delete(self):
        pass

    def resize(self, new_resolution):
        """Изменение размера изображения"""
        pass


# Расширение для работы с удаленным хранилищем
class RemoteMediaFile(MediaFile):
    def __init__(self, name, size, owner, storage_url):
        super().__init__(name, size, owner)
        self.storage_url = storage_url

    def save(self):
        """Загрузка файла в удаленное хранилище"""
        pass

    def delete(self):
        """Удаление файла из удаленного хранилища"""
        pass

    def download(self):
        """Загрузка файла на локальный диск"""
        pass


# Пример использования
if __name__ == "__main__":
    audio = AudioFile("song.mp3", 5000, "User1", 180, "mp3")
    video = VideoFile("movie.mp4", 2000000, "User2", "1080p", "mp4")
    photo = PhotoFile("image.jpg", 3000, "User3", "1920x1080", "jpg")
    remote = RemoteMediaFile("backup.zip", 500000, "Admin", "https://cloud.storage/backup.zip")

    print(f"Аудиофайл: {audio.name}, формат: {audio.format}, длительность: {audio.duration} сек")
    print(f"Видеофайл: {video.name}, разрешение: {video.resolution}")
    print(f"Фотография: {photo.name}, размер: {photo.resolution}")
    print(f"Удалённый файл: {remote.name}, ссылка: {remote.storage_url}")

    # Действия с файлами
    audio.convert("wav")
    video.extract_frames()
    photo.resize("1280x720")
    remote.download()
