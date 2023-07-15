FROM python:3.11.4-bullseye
WORKDIR /app
RUN pip install flask requests numpy pandas flasgger scikit-learn
COPY . .
EXPOSE 5000
CMD python flasks.py