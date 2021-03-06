# TheGameOfLife

"Игра жизнь" по модели Джона Конвея, воспроизведенная на python с помощью библиотек random и turtle.

## Запуск

На Windows

```powershell
py -3.8 .\thegame.py
```

На *nix-системах

```bash
python3 thegame.py 
```

* Для запуска рекомендуется использовать Python 3, совместимость с Python 2 не гарантируется. Проверено на версиях Python 3.7 и 3.8.
* Доп. зависимостей нет, все пакеты входят в состав стандартной библиотеки Python, но необходимо, чтобы был установлен модуль `tkinter` для отрисовки GUI.

## Разработка

Для разработки рекомендуется создавать виртуальное python-окружение, устанавливая туда зависимости `dev-requirements.txt`:

Windows:

```powershell
PS > py -3.8 -m venv .\venv
PS > .\venv\Scripts\activate
(venv) PS > python -m pip install --upgrade pip
(venv) PS > python -m pip install -r .\dev-requirements.txt
```

После чего можно будет запускать комплексный линтер [flake8](https://pypi.org/project/flake8/), подключив его либо в среду разработки, либо запуская через командную строку:

```powershell
> flake8 .
```

При этом на сервере через механизм [GitHub Actions](https://github.com/features/actions) запускается автоматический прогон линтера при каждом push.

В VS Code для интерактивной работы линтера необходимо (через команды `CTRL + SHIFT + P`):

1. `Python: Select interpreter` выбрать тот, что в созданном `.\venv`;
2. `Python: Select linter`, выбрать `flake8`.

Конфигурирование `flake8` производится в файле `.flake8`.

Для более строгой проверки кода можно дополнительно установить [wemake-python-styleguide](https://wemake-python-stylegui.de/en/latest/pages/usage/configuration.html), который расширяет возможности `flake8`.
