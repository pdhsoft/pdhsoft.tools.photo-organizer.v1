import os
import shutil
import argparse
from datetime import datetime
from PIL import Image
import PIL.ExifTags

def get_date_taken(image_path):
    try:
        image = Image.open(image_path)
        exif = {
            PIL.ExifTags.TAGS[k]: v
            for k, v in image._getexif().items()
            if k in PIL.ExifTags.TAGS
        } if image._getexif() else {}
        
        if 'DateTimeOriginal' in exif:
            return datetime.strptime(exif['DateTimeOriginal'], '%Y:%m:%d %H:%M:%S')
    except:
        pass
    
    # Fallback auf Dateiänderungsdatum
    return datetime.fromtimestamp(os.path.getmtime(image_path))

def organize_photos(source_dir, target_dir):
    # Unterstützte Bildformate
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(image_extensions):
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
    # Kommandozeilenparameter definieren
    parser = argparse.ArgumentParser(description='Organisiert Fotos nach Aufnahmedatum')
    parser.add_argument('source', help='Quellverzeichnis mit den Fotos')
    parser.add_argument('target', help='Zielverzeichnis für die sortierte Struktur')
    
    # Parameter auswerten
    args = parser.parse_args()
    
    # Fotos organisieren
    organize_photos(args.source, args.target)