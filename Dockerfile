# Container image that runs your code
FROM python:3.10

COPY markdown-faq/ /markdown-faq/

CMD ["python", "/markdown-faq/main.py"]
