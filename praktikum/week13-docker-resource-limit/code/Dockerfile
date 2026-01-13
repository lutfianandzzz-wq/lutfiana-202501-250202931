FROM python:3.11-slim
# Set working directory di dalam container
WORKDIR /app

# Install dependencies yang diperlukan
# psutil untuk monitoring resource sistem
RUN pip install --no-cache-dir psutil

# Copy file aplikasi ke dalam container
COPY app.py /app/

# Berikan permission execute pada file
RUN chmod +x /app/app.py

# Set environment variable (opsional)
ENV PYTHONUNBUFFERED=1

# Command default saat container dijalankan
CMD ["python", "app.py"]