# 🎬 Flixgo Movie Blog

Flixgo Movie Blog is a web application for listing and showcasing movies and TV shows.  
It is built with Django as the backend and uses a static HTML/CSS/JS template for the frontend, inspired by streaming platforms.

---

## ✨ Features

- Browse movies and TV shows
- View details of each movie or series
- Categories and genres
- Responsive design for different devices
- Easily extendable for:
  - User authentication (login/signup)
  - Ratings and reviews
  - Watchlists or favorites

---

## 🛠 Tech Stack

- **Backend:** Django  
- **Frontend:** Static HTML, CSS, JavaScript  
- **Database:** SQLite (default Django) 

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/alimotamed-py/Flixgo-Movie-Blog.git
cd Flixgo-Movie-Blog
2. Setup Python environment
bash
Copy code
# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
3. Run the project
bash
Copy code
python manage.py migrate
python manage.py runserver
Visit http://127.0.0.1:8000 in your browser.

📁 Project Structure
bash
Copy code
.
├── backend/           # Django backend code
├── templates/         # HTML templates for frontend
├── static/            # CSS, JS, images
├── README.md
└── LICENSE
🙏 Template Source / Credits
The UI of this project is based on the template from:

ybnthicco/flixgo

Thanks to the template creator for making it available as open-source ❤️

📄 License
This project is licensed under the MIT License.
See the LICENSE file for more details.

📬 Contact
For issues, suggestions, or contributions, feel free to reach out:

GitHub: @alimotamed-py

Email: alimotamed.py@gmail.com