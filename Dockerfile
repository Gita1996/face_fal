#FROM python:3.10
FROM fal_hafez2

RUN apt-get update 
RUN apt-get install -y python3-opencv

WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

#RUN ln -s /usr/lib/x86_64-linux-gnu/mesa/libGL.so.1 /usr/lib/libGL.so.1


RUN pip install --upgrade pip

RUN pip install python-multipart

#RUN pip install opencv-python


# 
RUN pip install -r /code/requirements.txt


# 
COPY ./app /code

# 
CMD ["uvicorn", "fal_Hafez2:app", "--host", "0.0.0.0", "--port", "8000"]