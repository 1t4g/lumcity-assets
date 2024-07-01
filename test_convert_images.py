import os
import pytest
from convert_images import convert_images

@pytest.fixture
def setup_test_environment():
    # Создайте временные папки для тестирования
    png_folder = "test_png"
    webp_folder = "test_webp"
    
    os.makedirs(png_folder, exist_ok=True)
    os.makedirs(webp_folder, exist_ok=True)

    # Создайте тестовое изображение
    from PIL import Image
    img = Image.new('RGB', (1000, 1000), color = 'red')
    img.save(os.path.join(png_folder, 'test.png'))

    yield png_folder, webp_folder

    # Удалите временные файлы и папки
    os.remove(os.path.join(png_folder, 'test.png'))
    os.remove(os.path.join(webp_folder, '100px/test100px.webp'))
    os.remove(os.path.join(webp_folder, '512px/test512px.webp'))
    os.rmdir(os.path.join(webp_folder, '100px'))
    os.rmdir(os.path.join(webp_folder, '512px'))
    os.rmdir(png_folder)
    os.rmdir(webp_folder)

def test_convert_images(setup_test_environment):
    png_folder, webp_folder = setup_test_environment

    # Выполните конвертацию
    convert_images(png_folder, webp_folder)

    # Проверьте, что изображения были созданы
    assert os.path.exists(os.path.join(webp_folder, '100px/test100px.webp'))
    assert os.path.exists(os.path.join(webp_folder, '512px/test512px.webp'))
