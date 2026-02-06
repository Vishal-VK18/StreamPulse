# Web Series Survey Application

A complete Flask-based web application for conducting a web series popularity and preference survey with CSV storage and real-time analytics charts.

## 🎯 Features

- **21 Comprehensive Fields**: Personal demographics (6 fields) + demographic preferences (3 questions) + web series survey (12 questions)
- **Demographic Collection**: Name, DOB, department, college, region/state, and city
- **Cultural Insights**: Language preference and regional influence on viewing habits
- **Mobile-Friendly UI**: Responsive design that works on all devices
- **CSV Storage**: All responses saved to a CSV file for easy data analysis
- **Analytics Charts**: Automatic generation of 3 insightful charts:
  - Most Favorite Web Series (Bar Chart)
  - Average Rating Per Series (Bar Chart)
  - Genre Preference Distribution (Pie Chart)
- **Render-Ready**: Pre-configured for deployment on Render's free tier

## 🎬 Web Series Included

- Game of Thrones
- Breaking Bad
- Better Call Saul
- The Sopranos
- Dark
- House of the Dragon
- A Knight of the Seven Kingdoms

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip

### Installation

1. Clone or navigate to the project directory:
   ```bash
   cd "D:\WebSeries Survey"
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and go to:
   ```
   http://localhost:5000
   ```

## 📊 Usage

1. **Fill Survey**: Navigate to the home page and complete the 12-question survey
2. **Submit**: Click the "Submit Survey" button
3. **View Analytics**: Click "View Analytics" to see charts generated from all responses
4. **Submit More**: Multiple responses can be submitted

## 🌐 Deployment to Render

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Deploy on Render**:
   - Sign up/login at [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Set:
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
   - Click "Create Web Service"

3. **Access**: Your app will be live at `https://your-app-name.onrender.com`

> **Note**: Free tier services spin down after 15 minutes of inactivity. First request may take 30+ seconds.

## 📁 Project Structure

```
D:\WebSeries Survey\
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── data.csv              # Survey responses
├── templates/
│   └── index.html        # Survey form
└── static/
    └── charts/           # Generated charts
```

## 🛠️ Technologies Used

- **Backend**: Flask 3.0.0
- **Data Processing**: pandas 2.1.4
- **Visualization**: matplotlib 3.8.2
- **Production Server**: gunicorn 21.2.0
- **Storage**: CSV files

## 📝 Survey Fields (21 Total)

### Personal Information (6 fields)
1. Name
2. Date of Birth
3. Department (dropdown)
4. College Name
5. Region/State (dropdown)
6. City

### Demographic Preferences (3 questions)
1. Does your region/state influence the type of web series you prefer?
2. Do you mostly watch web series in: (English/Regional/Both)
3. Do you think your college environment or department affects your web-series choices?

### Web Series Preferences (12 questions)
1. How often do you watch web series?
2. Which streaming platform do you use MOST?
3. Which series have you watched? (Multiple selection)
4. Which series is your MOST favorite?
5-8. Rate each series (1-5 scale): Game of Thrones, Breaking Bad, Better Call Saul, Dark
9. Which genre do you MOST enjoy?
10. Which series has the BEST storytelling?
11. Which series would you MOST recommend?
12. What factor matters MOST to you?

## 📈 Analytics

The application generates three types of charts:

1. **Favorite Series**: Bar chart showing vote distribution
2. **Average Ratings**: Bar chart comparing average ratings across series
3. **Genre Preferences**: Pie chart showing genre distribution

Charts are regenerated dynamically each time the `/charts` endpoint is accessed.

## 🔒 Data Storage

- All responses stored in `data.csv`
- UTF-8 encoding for international character support
- Proper CSV headers matching all 21 fields:
  - 6 personal/demographic fields
  - 3 demographic preference questions
  - 12 web series preference questions
- Safe for 100+ concurrent submissions

## 🎨 UI/UX Features

- Modern gradient background (purple theme)
- Smooth hover animations
- Clear question numbering
- Required field validation
- Success confirmation page
- Responsive design for mobile devices

## 📦 Dependencies

```
Flask==3.0.0
matplotlib==3.8.2
pandas==2.1.4
gunicorn==21.2.0
```

## 🤝 Contributing

This is a complete project ready for deployment. Feel free to:
- Add more series to the survey
- Customize the color scheme
- Add additional chart types
- Implement user authentication

## 📄 License

Open source - feel free to use and modify as needed.

## 👤 Author

Built with Flask and Python

## 🐛 Known Issues

- On Render's free tier, CSV data resets when the service restarts
- For persistent storage, consider using a database or upgrading to a paid plan

## 💡 Future Enhancements

- Database integration (PostgreSQL/MongoDB)
- User authentication
- Export CSV functionality
- Admin dashboard
- Email notifications
- Advanced filtering options

---

**Ready to deploy!** Follow the deployment instructions above to get your survey live on the web.
