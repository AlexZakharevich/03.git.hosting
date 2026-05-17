# СТАДИЯ 1: Сборка (build stage)
FROM python:3.11-slim AS builder

WORKDIR /build

# Копируем исходный код
COPY app.py .

# Проверяем синтаксис (имитация сборки)
RUN python -m py_compile app.py && \
    echo "Сборка завершена успешно"

# СТАДИЯ 2: Выполнение (runtime stage)
FROM python:3.11-slim AS runtime

WORKDIR /app

# Копируем только скомпилированный файл со стадии сборки
COPY --from=builder /build/__pycache__/app.cpython-311.pyc /app/app.pyc

# Создаём скрипт для запуска
RUN echo '#!/bin/bash\npython3 -c "import app; print(app.factorial(10))"' > /app/run.sh && \
    chmod +x /app/run.sh

# Запускаем приложение
CMD ["/app/run.sh"]