### How to install required packages

App is built using Python 3.9.1 and FastAPI. check the requirements.txt file for the list of packages required to run the app.

1. Clone the repository using the following command:

    ```bash
    git clone https://github.com/odinthuder/flask-qrcode.git

2. Install the required packages using the following command:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the flask application using the following command:

    ```bash
    uvicorn main:app --reload
    ```
    ```
### Usage of the API :

1. To generate a QR code, send a GET request to the following address:

    ```bash
    http://localhost:5000/qr?link=www.google.com
    ```

2. To generate a QR code with a custom size, send a GET request to the following address:

    [ ] : Note: The size of the QR code is in pixels. - to be added later

    ```bash
    http://localhost:5000/qr?link=www.google.com&size=500
    ```
