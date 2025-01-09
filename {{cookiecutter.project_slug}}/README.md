# {{ cookiecutter.project_name }}

Репозиторий для проектов компьютерного зрения, использующий:
- **Python** `{{ cookiecutter.python_version }}`
- **Poetry** версии `{{ cookiecutter.poetry_version }}`
- **Docker** и **docker-compose**
- **pre-commit** для автопроверок кода
- **Tox** для тестирования

## Начало работы

1. Установите [Poetry](https://python-poetry.org/) нужной версии ({{ cookiecutter.poetry_version }}):

    ```bash
    # Пример установки конкретной версии (локально):
    curl -sSL https://install.python-poetry.org | python3 - --version {{ cookiecutter.poetry_version }}
    ```

2. Настройте Poetry так, чтобы виртуальное окружение создавалось в корне проекта (в папке .venv):
    ```bash
    poetry config virtualenvs.in-project true
    ```

3. Установите зависимости:
    ```bash
    poetry install
    ```

4. Активируйте окружение
    ```bash
    poetry shell
    ```
   
## Структура проекта

```bash
{{ cookiecutter.project_slug }}/
├── data/                         # Данные проекта, разбитые по стадиям обработки
│   ├── 0_raw/                    # Сырые, необработанные данные
│   ├── 1_prelabelled/            # Предварительно размеченные данные
│   ├── 2_labelled/               # Данные с финальной разметкой
│   └── 3_processed/              # Обработанные данные, готовые к использованию
├── docs/                         # Документация (Sphinx, инструкции, отчёты)
│   ├── Makefile                  # Makefile для сборки документации (sphinx-build)
│   ├── conf.py                   # Основной конфигурационный файл Sphinx
│   └── index.rst                 # Главная точка входа для документации
├── models/                       # Сохранённые модели (weights, checkpoints)
├── notebooks/                    # Jupyter-ноутбуки для исследования и прототипирования
├── references/                   # Ссылочные материалы, статьи, библиография
├── reports/                      # Итоговые отчёты, презентации
│   └── figures/                  # Иллюстрации, графики, изображения для отчётов
├── src/                          # Исходный код проекта
│   ├── __init__.py               
│   ├── config/                   # Конфигурации, настройки
│   │   └── __init__.py           
│   ├── data/                     # Логика чтения/записи данных, загрузчики
│   │   └── __init__.py           
│   ├── models/                   # Код моделей, архитектуры, тренировка
│   │   └── __init__.py           
│   ├── tools/                    # Утилиты и вспомогательные скрипты
│   │   └── __init__.py           
│   └── visualization/            # Визуализация данных и результатов
│       └── __init__.py           
├── Dockerfile                    # Сборка Docker-образа
├── docker-compose.yml            # Оркестрация нескольких контейнеров (если нужно)
├── Makefile                      # Шорткаты для типовых команд (install, test, lint и т.д.)
├── pyproject.toml                # Конфигурация Poetry (зависимости, метаданные проекта)
├── setup.py                      # Минимальный setup.py для совместимости с некоторыми инструментами
├── test_environment.py           # Скрипт для проверки установленного окружения
├── tox.ini                       # Настройки для тестирования и линтинга в разных окружениях
└── ci.yml                        # Конфигурация CI/CD
```

## Некоторые полезные команды

```bash
# Установка зависимостей
poetry install

# Запуск тестов
poetry run pytest

# Запуск линтера/форматирования кода
poetry run flake8 src
poetry run black src

# Запуск проверок pre-commit на всех файлах
poetry run pre-commit run --all-files

# Сборка Docker-образа и поднятие сервиса
docker-compose up --build
```
