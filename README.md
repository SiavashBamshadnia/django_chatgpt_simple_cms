# Django ChatGPT Simple CMS

This package provides a simple CMS (Content Management System) built with Django framework that uses ChatGPT to generate
post titles, summaries, and contents.

To use this package, follow the steps below:

1. Clone the project to your computer using the following command:

    ```shell
    git clone https://github.com/SiavashBamshadnia/Django-ChatGPT-Simple-CMS
    ```

2. Install the required packages using the following command:

    ```shell
    pip install -r requirements.txt
    ```

3. Migrate the project using the following command:

    ```shell
    python3 manage.py migrate
    ```

4. In the settings.py file, set the OPENAI_API_KEY to your openai's API key.

   **Note:** To run tests, you will need to download the Chrome driver from https://chromedriver.chromium.org/ and set
   the SELENIUM_CHROME_EXECUTABLE_PATH to the Chrome driver's path.

5. Run your server on your localhost using the following command:

    ```shell
    python3 manage.py runserver
    ```

Now you can access the CMS through your web browser at `http://localhost:8000/`.
