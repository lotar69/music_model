FROM python:3.9-slim
COPY music_model /music_model
COPY api /api
COPY requirements.txt /requirements.txt
COPY README.md /README.md
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["uvicorn", "api.predict:app", "--host", "0.0.0.0", "--port", "80"]