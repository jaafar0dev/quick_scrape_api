# Quick-Scrape API & Word Frequency Analyzer

A simple backend-focused project that scrapes a target webpage, analyzes the word frequency of its content, stores the results in a database, and provides API endpoints to trigger the scrape and view the data.

This project was built as a rapid refresher of core backend development skills.

---

## 🚀 Features

* **Web Scraping:** Uses BeautifulSoup to fetch and parse HTML from a static webpage.
* **Text Analysis:** Calculates the frequency of all words on the scraped page.
* **REST API:** Built with Flask, providing simple endpoints to trigger scraping and data retrieval.
* **Database Storage:** Uses SQLAlchemy and SQLite to persist the scraped data (e.g., word, count).
* **Dynamic Frontend:** A simple Jinja2 template displays the data stored in the database.

---

## 🛠️ Tech Stack

This project utilizes the following technologies:

* **Languages:** Python, SQL
* **Frameworks & Libraries:**
    * Flask: For the web server and API.
    * SQLAlchemy: For the ORM and database interaction.
    * BeautifulSoup: For web scraping.
    * Jinja2: For server-side template rendering.
* **Database:**
    * SQLite: For simple, local database storage.

---

## 🏁 Getting Started

Follow these instructions to get a local copy up and running.

### Prerequisites

* Python 3.8+
* `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/your-project-name.git](https://github.com/your-username/your-project-name.git)
    cd your-project-name
    ```

2.  **Create and activate a virtual environment:**
    * **macOS/Linux:**
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **Windows:**
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required packages:**
    (You may need to create this file first by running `pip freeze > requirements.txt`)
    ```sh
    pip install -r requirements.txt
    ```

4.  **Initialize the database:**
    (If you have an init script. If not, SQLAlchemy `db.create_all()` will do it on the first run).
    ```sh
    # This command depends on how you set up your app
    python app.py
    ```

### Running the Application

To start the local development server:

```sh
flask run
