import pytest
import os
import shutil
from PIL import Image

@pytest.fixture
def setup_test_environment():
    # Создаем временные папки для тестирования
    png_folder = "test_png"
    webp_folder = "test_webp"

    os.makedirs(png_folder, exist_ok=True)
    os.makedirs(webp_folder, exist_ok=True)

    # Создаем тестовое изображение
    img = Image.new('RGB', (1000, 1000), color='red')
    img.save(os.path.join(png_folder, 'test.png'))

    yield png_folder, webp_folder

    # Удаляем временные файлы и папки
    if os.path.exists(png_folder):
        os.remove(os.path.join(png_folder, 'test.png'))
    if os.path.exists(webp_folder):
        shutil.rmtree(webp_folder)  # Рекурсивно удаляем содержимое и саму папку webp_folder

def test_convert_images(setup_test_environment):
    png_folder, webp_folder = setup_test_environment

    # Выполняем конвертацию
    convert_images(png_folder, webp_folder)

    # Проверяем, что изображения были созданы
    assert os.path.exists(os.path.join(webp_folder, '100px/test100px.webp'))
