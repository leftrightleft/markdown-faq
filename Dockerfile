# Container image that runs your code
FROM python:3.10

COPY markdown-faq/main.py /tmp/

CMD ["python", "/tmp/main.py"]
