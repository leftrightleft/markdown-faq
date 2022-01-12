# Container image that runs your code
FROM python:3.10

COPY markdown-faq/ /markdown-faq/

# RUN pip install --no-cache-dir --upgrade pip && \
#     pip install --no-cache-dir -r /markdown-faq/requirements.txt
RUN pip install pyyaml

CMD ["python", "/markdown-faq/main.py"]
