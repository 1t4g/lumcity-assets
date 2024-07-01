# lumcity-assets
Этот репозиторий предназначен для автоматической конвертации изображений формата PNG в формат WebP с двумя разрешениями: 100x100 и 512x512 пикселей.



## Структура репозитория

- `png/` - Папка для исходных изображений в формате PNG.
- `webp/` - Папка для конвертированных изображений в формате WebP.
  - `100px/` - Папка дл0я изображений размером 100x100 пикселей.
  - `512px/` - Папка для изображений размером 512x512 пикселей.
- `other/` - Дополнительные файлы.
- `convert_images.py` - Скрипт для конвертации изображений.
- `requirements.txt` - Файл для установки необходимых зависимостей.
- `.github/workflows/image_conversion.yml` - Конфигурация GitHub Actions для автоматической конвертации изображений.

## Вклад

Контрибьюторы могут вносить изменения только в папку `png`. Пожалуйста, следуйте этим шагам для внесения изменений:

1. Форкните этот репозиторий.
2. Создайте новую ветку для своих изменений (`git checkout -b add-new-images`).
3. Добавьте свои изображения в папку `png`.
4. Сделайте коммит своих изменений (`git commit -m 'Add new images'`).
5. Запушьте свою ветку (`git push origin add-new-images`).
6. Откройте Pull Request.

### Пример

```bash
# Форкните репозиторий и клонируйте его локально
git clone <URL вашего форка>
cd my_image_repo

# Создайте новую ветку
git checkout -b add-new-images

# Добавьте свои изображения в папку png
cp /path/to/your/image.png png/

# Сделайте коммит
git add png/
git commit -m 'Add new images'

# Запушьте изменения
git push origin add-new-images

# Откройте Pull Request через веб-интерфейс GitHub
