FROM python
WORKDIR /app
COPY . .
RUN pip install -r requirment.txt
CMD ["python","app.py"]