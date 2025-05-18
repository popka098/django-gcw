#!/bin/bash

echo "Starting documentation build..."

cd docs
export PYTHONPATH=..
make html
cd ..

echo "Documentation built, checking directories..."

# Создаем директорию public если её нет
mkdir -p public

echo "Created public directory"

if [ -d "docs/build/html" ]; then
    echo "Found docs/build/html directory"
    ls -la docs/build/html/

    # Перемещаем всё (включая скрытые файлы) с помощью rsync
    rsync -a docs/build/html/ public/documentation/

    echo "Moved files to public directory"
    ls -la public/
else
    echo "Error: docs/build/html directory not found!"
    ls -la docs/build/
fi