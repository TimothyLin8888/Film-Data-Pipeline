# Film-Data-Pipeline
<h2>Overview</h2>
This project allows you to interact with Google Sheets to input and output data, with a specific focus on tracking and analyzing movies. You can use it to manage your movie data, such as titles, release years, ratings, etc., and perform various data analytics tasks like generating insights, running analysis, and automating reports. While the core of this project focuses on movie data, it can be easily adapted to work with other types of data stored in Google Sheets.

<h2>Features</h2>

- **Input Data**: Easily add new data entries to your Google Sheets (movies or other data).

- **Read Data**: Retrieve and analyze existing data from Google Sheets.

- **Update Data**: Modify or update existing entries in the sheet.
  
- **Data Analytics**: Perform basic analysis on movie data (or other types of data).
  
- **Customizable**: Easily adapt the tool to handle other types of data by changing sheet names or structures.

<h2>Requirements</h2>

- **Google Sheets API Access**
- **gspread**: Python library for Google Sheets API
- **google-auth**: for authentication with Google Sheets

<h2>Google Sheets API Setup</h2>

To interact with Google Sheets from Python, you need to set up Google Sheets API credentials. Follow these steps:

### 1. Create a Project on Google Cloud Console
1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.

### 2. Enable the Google Sheets API
1. Navigate to **API & Services > Library**.
2. Search for **Google Sheets API** and enable it for your project.

### 3. Create Service Account Credentials
1. Go to **API & Services > Credentials**.
2. Click **Create Credentials** → **Service Account**.
3. Fill in the required information and create the service account.
4. Once created, go to the service account and generate a **JSON key file**.
5. Download the JSON key and rename it to `credentials.json`.
6. Place `credentials.json` in the root directory of your project.

### 4. Share Your Google Sheet with the Service Account
1. Open the Google Sheet you want to access.
2. Click **Share**.
3. Add the **service account email** (found in `credentials.json` under `client_email`) and give it **Editor** access.

### 5. Get Your Google Sheet ID
1. Open the Google Sheet in your browser.
2. Copy the ID from the URL. For example, in:

```
https://docs.google.com/spreadsheet/d/<sheet_id>/edit
```
<sheet_id> is what you need, after /d/ and before /edit
3. Use this ID in your Python script to access the sheet:
  ```workbook = client.open_by_key("<sheet-id>")```

<h2>Future Features</h2>

- **Automatic Data Updates**: Schedule automatic updates to Google Sheets at set intervals (e.g., daily movie ratings updates).

- **Machine Learning Integration**: Use machine learning models to predict movie ratings or suggest similar movies.

- **User Interface**: Build a simple web interface using Flask or Streamlit to allow for easy input/output without needing to run scripts manually.
