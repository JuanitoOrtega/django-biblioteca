# Exportar datos
python manage.py dumpdata --indent 2 author.author book.category book.book reader.reader reader.lend > data.json

# Importar datos
python manage.py loaddata data.json