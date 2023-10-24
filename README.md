# Chatbot-healthy-care
Chatbot-healthy-care

This project only works for python 3.7
Follow step for install:
1. Open terminal in project and install lastest pip
python -m pip install pip
2. Install requirements.txt
python -m pip install -r requirements.txt
3. To run the project, follow these steps:
First, run train.py.
Then run main.py.
Open a terminal and execute the following command to run FastAPI app using uvicorn:
python -m uvicorn main:app
4. Open your browset at http://127.0.0.1:8000.
The API endpoint for get response chat messages is http://127.0.0.1:8000/api/get/?msg=hello.
5. Finally, to run this in my react native project, make sure change the host and port (local IP address)
python -m uvicorn main:app --host=0.0.0.0 --port=8000
The API endpoint for get response chat messages is http://192.168.9.10:8000/api/get/?msg=hello.
