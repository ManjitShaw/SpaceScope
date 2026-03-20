# SpaceScope

#### Video Demo: [<VIDEO_URL_HERE>](https://youtu.be/Ys-NfcHyFq8?si=lKzl1J9f32fco5YP)

#### Description:
SpaceScope is a Python program that fetches and displays near-Earth asteroid information from NASA’s NeoWs (Near Earth Object Web Service) API. The program allows users to quickly view details about asteroids approaching Earth on the current date. It also saves the top 5 asteroid entries in a simple JSON log (`activity.json`) for tracking and review.

Users interact with SpaceScope via the command line, where they are prompted to press Enter to fetch asteroid data. The program then displays each asteroid’s name, estimated diameter in kilometers, relative speed in km/h, and miss distance in million kilometers.

#### Features:
- Fetches real-time near-Earth asteroid data from NASA’s API.
- Displays key asteroid metrics: name, diameter, speed, and miss distance.
- Saves the top 5 asteroids of the day in a JSON log file (`activity.json`) with a timestamp.
- Simple command-line interface for easy usage.
- Modular code structure with functions: `fetch_asteroids()`, `get_top_asteroids()`, `save_asteroid_log()`.

#### Project Files:
- `project.py` – Main program and all functions.
- `test_project.py` – Manual tests for core functions (can be run with `pytest`).
- `.env` – Stores the `NASA_API_KEY`.
- `requirements.txt` – Lists pip-installable libraries (`requests`, `python-dotenv`).
- `activity.json` – JSON log of top 5 asteroids.

#### How to Run:
1. Make sure Python 3.x is installed.
2. Install required packages:  
3. Add your NASA API key in a `.env` file:  
4. Run the program:  
5. Press Enter to fetch and display the top 5 near-Earth asteroids.

#### Notes:
- Only the first 5 asteroids of the day are displayed and logged for brevity.
- The program handles API errors gracefully and informs the user if the data cannot be fetched.
- The JSON log includes the timestamp and asteroid details for each fetch.

#### Author:
- Name: Manjit Shaw
- GitHub: [ManjitShaw](https://github.com/ManjitShaw)
- edX: MS_2508_6C7F
- Location: Kolkata, India
- Date: 20 December 2025
