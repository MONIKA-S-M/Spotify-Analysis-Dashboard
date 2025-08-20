el# Spotify Track Data and Dashboard Project

## 📌 Overview
This project demonstrates how to:
1. Fetch track data from **Spotify API** using the `Spotipy` library.
2. Save and organize the data into **CSV** and **MySQL database**.
3. Build an **Excel Dashboard** for interactive visualization and insights.

The project includes multiple scripts to handle different stages:
- `spotify.py` → Fetch a single track’s metadata, save to CSV, and visualize using Matplotlib.
- `spotify_mysql.py` → Insert single track metadata into MySQL database.
- `spotify_mysql_url.py` → Fetch multiple tracks from a playlist and store them into MySQL.
- `spotify_db_tracks_dashboard.xml` → Pre-built Excel Dashboard for data analysis.

---

## 🛠️ Technologies Used
- **Python** (Spotipy, Pandas, Matplotlib, MySQL Connector)
- **MySQL** (Database to store Spotify tracks)
- **Excel Dashboard** (Pivot Tables, Slicers for interactive analytics)

---

## 🚀 Features
- Extracts track name, artist, album, popularity, and duration.
- Saves Spotify track details into CSV and MySQL.
- Visualizes track popularity and duration using Matplotlib.
- Provides an Excel-based dashboard for insights:
  - Popularity categories (Hit, Popular, Normal, No Rating)
  - Duration categories (<2 min, 2-3 min, 3-4 min, 4-5 min, >5 min)
  - Filtering and analysis using slicers.

---

## 📂 Project Structure
```
├── spotify.py                   # Fetch single track metadata and save to CSV
├── spotify_mysql.py              # Insert single track metadata into MySQL
├── spotify_mysql_url.py          # Fetch playlist tracks and insert into MySQL
├── spotify_db_tracks_dashboard.xml # Excel Dashboard (pivot tables & slicers)
├── SPOTIFY DASHBOARD.png         # Dashboard Screenshot
```

---

## 📊 Dashboard Preview
Here is the **Excel Dashboard** generated from Spotify Top Tracks data:
<img width="1512" height="568" alt="SPOTIFY DASHBOARD" src="https://github.com/user-attachments/assets/976606cd-669a-4732-b44e-17a9fb1661f9" />


## ⚙️ Setup Instructions

1. **Install Dependencies**
   ```bash
   pip install spotipy pandas matplotlib mysql-connector-python
   ```

2. **Set Up MySQL Database**
   ```sql
   CREATE DATABASE spotify_db;
   USE spotify_db;

   CREATE TABLE spotify_tracks (
       id INT AUTO_INCREMENT PRIMARY KEY,
       track_name VARCHAR(255),
       artist VARCHAR(255),
       album VARCHAR(255),
       popularity INT,
       duration_minutes FLOAT
   );
   ```

3. **Run Scripts**
     python spotify.py
     ```
   - Insert track into MySQL:
     ```bash
     python spotify_mysql.py
     ```
   - Insert playlist tracks into MySQL:
     ```bash
     python spotify_mysql_url.py
     ```

---

## 📊 Example Insights
- Which tracks are marked as **Hits** (popularity >= 70).
- Distribution of track durations (2-3 min, 3-4 min, etc.).
- Popular artists based on track count and ratings.

---

## 📌 Future Enhancements
- Automate dashboard updates directly from MySQL.
- Integrate MS-Excel for advanced analytics.

---
