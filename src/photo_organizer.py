import os
import shutil
import argparse
from datetime import datetime
from PIL import Image
import PIL.ExifTags

def get_date_taken(file_path):
    # Dateierweiterung prüfen
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext in ('.jpg', '.jpeg', '.png', '.gif', '.bmp'):
        try:
            image = Image.open(file_path)
            exif = {
                PIL.ExifTags.TAGS[k]: v
                for k, v in image._getexif().items()
                if k in PIL.ExifTags.TAGS
            } if image._getexif() else {}
            
            if 'DateTimeOriginal' in exif:
                return datetime.strptime(exif['DateTimeOriginal'], '%Y:%m:%d %H:%M:%S')
        except:
            pass
    
    # Fallback auf Dateiänderungsdatum für Videos und Bilder ohne EXIF
    return datetime.fromtimestamp(os.path.getmtime(file_path))

def organize_media(source_dir, target_dir):
    # Unterstützte Medienformate
    media_extensions = (
        # Bilder
        '.jpg', '.jpeg', '.png', '.gif', '.bmp',
        # Videos
        '.mp4', '.mov', '.avi', '.mkv', '.wmv'
    )
    
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(media_extensions):
            source_path = os.path.join(source_dir, filename)
            
            # Datum ermitteln
            date = get_date_taken(source_path)
            
            # Zielordner erstellen
            year_month = os.path.join(target_dir, str(date.year), f"{date.month:02d}")
            os.makedirs(year_month, exist_ok=True)
            
            # Datei verschieben
            target_path = os.path.join(year_month, filename)
            shutil.move(source_path, target_path)
            print(f"Verschoben: {filename} -> {target_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Organisiert Fotos und Videos nach Aufnahmedatum')
    parser.add_argument('source', help='Quellverzeichnis mit den Medien')
    parser.add_argument('target', help='Zielverzeichnis für die sortierte Struktur')
    
    args = parser.parse_args()
    organize_media(args.source, args.target)