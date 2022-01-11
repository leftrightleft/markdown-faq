# Container image that runs your code
FROM python:3.10

COPY markdown-faq/ /src/
WORKDIR /src/
CMD ["python", "/src/main.py"]
