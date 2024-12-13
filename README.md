# Photo Organizer

Dieses Projekt organisiert Fotos und Videos aus einem Quellverzeichnis in ein Zielverzeichnis basierend auf dem Datum, an dem die Fotos / Videos aufgenommen wurden.

## Installation

Um die erforderlichen Abhängigkeiten zu installieren, führen Sie den folgenden Befehl aus:

```bash
pip install -r requirements.txt
```

## Verwendung

Das Programm erwartet zwei Parameter:

1. Quellverzeichnis: Der Ordner mit den zu sortierenden Fotos
2. Zielverzeichnis: Der Ordner, in dem die sortierte Struktur erstellt werden soll

Beispiel:

```bash
python src/photo_organizer.py /pfad/zum/quellordner /pfad/zum/zielordner
```

oder mit der exe-Datei:

```bash
photo_organizer.exe /pfad/zum/quellordner /pfad/zum/zielordner
```

Passen Sie die `source_directory` und `target_directory` Variablen im Skript an oder modifizieren Sie das Skript, um die Verzeichnisse über Befehlszeilenparameter zu akzeptieren.

## Erstellen einer ausführbaren Datei

Um eine ausführbare Datei zu erstellen, verwenden Sie `PyInstaller`. Fügen Sie die folgenden Zeilen zu Ihrer `setup.py` hinzu:

```python
from setuptools import setup

setup(
    name='Photo-Organizer',
    version='1.0.0',
    author='pdhsoft',
    install_requires=[
        'Pillow',
        'pyinstaller',
    ],
)
```

Führen Sie dann den folgenden Befehl aus, um die ausführbare Datei zu erstellen:

```bash
pyinstaller --onefile src/photo_organizer.py
```
