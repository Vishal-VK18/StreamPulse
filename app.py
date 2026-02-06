from flask import Flask, render_template, request, redirect, url_for
import csv
import os
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for server environments
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

app = Flask(__name__)

# Configuration - Use absolute paths for Render compatibility
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, 'data.csv')
CHARTS_DIR = os.path.join(BASE_DIR, 'static', 'charts')

# Ensure directories exist
os.makedirs(os.path.join(BASE_DIR, 'templates'), exist_ok=True)
os.makedirs(CHARTS_DIR, exist_ok=True)

# CSV header definition
CSV_HEADERS = [
    'name',
    'dob',
    'department',
    'college_name',
    'region',
    'city',
    'regional_influence',
    'language_preference',
    'college_influence',
    'watch_frequency',
    'streaming_platform',
    'series_watched',
    'favorite_series',
    'rating_got',
    'rating_bb',
    'rating_bcs',
    'rating_dark',
    'rating_sopranos',
    'rating_hotd',
    'rating_knight',
    'genre_preference',
    'best_storytelling',
    'most_recommended',
    'important_factor'
]

def ensure_csv_exists():
    """Create CSV with headers if it doesn't exist (called on every submission)"""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)

@app.route('/')
def index():
    """Render the survey form"""
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    """Handle form submission and save to CSV"""
    try:
        # Ensure CSV file exists with headers before writing
        ensure_csv_exists()
        
        # Extract form data with explicit int conversion for ratings
        data = [
            request.form.get('name', ''),
            request.form.get('dob', ''),
            request.form.get('department', ''),
            request.form.get('college_name', ''),
            request.form.get('region', ''),
            request.form.get('city', ''),
            request.form.get('regional_influence', ''),
            request.form.get('language_preference', ''),
            request.form.get('college_influence', ''),
            request.form.get('watch_frequency', ''),
            request.form.get('streaming_platform', ''),
            ', '.join(request.form.getlist('series_watched')),  # Multiple checkboxes
            request.form.get('favorite_series', ''),
            # Convert ratings to pure integers (1-5) for Excel compatibility
            int(request.form.get('rating_got', 0)) if request.form.get('rating_got') else '',
            int(request.form.get('rating_bb', 0)) if request.form.get('rating_bb') else '',
            int(request.form.get('rating_bcs', 0)) if request.form.get('rating_bcs') else '',
            int(request.form.get('rating_dark', 0)) if request.form.get('rating_dark') else '',
            int(request.form.get('rating_sopranos', 0)) if request.form.get('rating_sopranos') else '',
            int(request.form.get('rating_hotd', 0)) if request.form.get('rating_hotd') else '',
            int(request.form.get('rating_knight', 0)) if request.form.get('rating_knight') else '',
            request.form.get('genre_preference', ''),
            request.form.get('best_storytelling', ''),
            request.form.get('most_recommended', ''),
            request.form.get('important_factor', '')
        ]
        
        # Append data to CSV (headers already exist from ensure_csv_exists)
        with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(data)
        
        return redirect(url_for('success'))
    
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/success')
def success():
    """Display success message after submission"""
    return """
    <!DOCTYPE html>
    <html class="dark" lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Response Recorded - StreamPulse Survey</title>
        <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
        <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Spline+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <script>
            tailwind.config = {
                darkMode: "class",
                theme: {
                    extend: {
                        colors: {
                            "primary": "#ec1313",
                            "background-dark": "#0a0a0a",
                        },
                        fontFamily: {
                            "display": ["Spline Sans", "sans-serif"]
                        },
                    },
                },
            }
        </script>
        <style>
            body {
                font-family: "Spline Sans", sans-serif;
                background-color: #0a0a0a;
            }
            .glass-container {
                background: rgba(20, 15, 15, 0.75);
                backdrop-filter: blur(24px);
                border: 1px solid rgba(255, 255, 255, 0.08);
            }
            .bg-overlay-gradient {
                background: radial-gradient(circle at center, rgba(10, 10, 10, 0.4) 0%, rgba(10, 10, 10, 0.9) 60%, #1a0505 100%);
                position: fixed;
                inset: 0;
                z-index: -5;
                pointer-events: none;
            }
        </style>
    </head>
    <body class="bg-background-dark text-white min-h-screen selection:bg-primary selection:text-white">
        
        <div class="bg-overlay-gradient"></div>
        
        <div class="relative flex min-h-screen flex-col items-center justify-center p-4 md:p-8">
            
            <!-- Header -->
            <header class="w-full max-w-[600px] flex items-center justify-center mb-8 px-4">
                <div class="flex items-center gap-3">
                    <div class="size-8 bg-primary rounded-lg flex items-center justify-center">
                        <span class="material-symbols-outlined text-white text-xl">movie_filter</span>
                    </div>
                    <h2 class="text-xl font-bold tracking-tight">StreamPulse</h2>
                </div>
            </header>
            
            <!-- Success Container -->
            <main class="w-full max-w-[600px]">
                <div class="glass-container rounded-xl p-8 md:p-12 shadow-2xl relative z-10">
                    
                    <!-- Success Icon -->
                    <div class="flex justify-center mb-6">
                        <div class="size-20 bg-primary/20 rounded-full flex items-center justify-center border-2 border-primary/40">
                            <span class="material-symbols-outlined text-primary" style="font-size: 48px;">check_circle</span>
                        </div>
                    </div>
                    
                    <!-- Title -->
                    <h1 class="text-3xl md:text-4xl font-bold mb-4 tracking-tight text-center">Response Recorded Successfully</h1>
                    
                    <!-- Message -->
                    <p class="text-zinc-400 text-base md:text-lg text-center mb-8 leading-relaxed">
                        Thank you for your participation. Your feedback helps us understand web series preferences and trends.
                    </p>
                    
                    <!-- Buttons -->
                    <div class="flex flex-col sm:flex-row gap-4 justify-center">
                        <a href="/" 
                           class="flex items-center justify-center gap-2 px-6 py-3 bg-gradient-to-r from-primary to-[#8b0000] hover:from-[#ff1a1a] hover:to-primary text-white font-semibold rounded-lg shadow-lg transition-all transform hover:scale-[1.02] active:scale-[0.98]">
                            <span class="material-symbols-outlined text-sm">add</span>
                            Submit Another Response
                        </a>
                        <a href="/charts" 
                           class="flex items-center justify-center gap-2 px-6 py-3 bg-black/40 border border-zinc-700/50 hover:border-primary/50 text-white font-semibold rounded-lg transition-all transform hover:scale-[1.02] active:scale-[0.98]">
                            <span class="material-symbols-outlined text-sm">bar_chart</span>
                            View Analytics
                        </a>
                    </div>
                    
                </div>
            </main>
            
            <!-- Footer -->
            <footer class="w-full max-w-[600px] flex items-center justify-center mt-8 px-4 text-zinc-500 text-xs border-t border-white/5 pt-6">
                <p>© 2026 StreamPulse Analytics. All rights reserved.</p>
            </footer>
            
        </div>
        
    </body>
    </html>
    """

@app.route('/charts')
def charts():
    """Generate and display charts from CSV data"""
    try:
        # Check if CSV exists and has data
        if not os.path.exists(CSV_FILE):
            return "No data available yet. Please submit the survey first.", 404
        
        # Check file size to ensure it's not just headers
        if os.path.getsize(CSV_FILE) < 100:  # File too small (likely just headers)
            return "No data available yet. Please submit the survey first.", 404
        
        # Read CSV data with explicit path
        df = pd.read_csv(CSV_FILE)
        
        # Verify DataFrame has actual data rows
        if len(df) == 0:
            return "No data available yet. Please submit the survey first.", 404
        
        # Clear previous charts
        for file in os.listdir(CHARTS_DIR):
            if file.endswith('.png'):
                os.remove(os.path.join(CHARTS_DIR, file))
        
        # Chart 1: Most Favorite Web Series (Bar Chart)
        plt.figure(figsize=(10, 6))
        favorite_counts = df['favorite_series'].value_counts()
        plt.bar(range(len(favorite_counts)), favorite_counts.values, color='#667eea')
        plt.xlabel('Web Series', fontsize=12, fontweight='bold')
        plt.ylabel('Number of Votes', fontsize=12, fontweight='bold')
        plt.title('Most Favorite Web Series', fontsize=14, fontweight='bold')
        plt.xticks(range(len(favorite_counts)), favorite_counts.index, rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(os.path.join(CHARTS_DIR, 'favorite_series.png'), dpi=100)
        plt.close()
        
        # Chart 2: Average Rating Per Series (Bar Chart)
        plt.figure(figsize=(12, 6))
        # Convert ratings to numeric, replacing errors with NaN for accurate averages
        series_ratings = {
            'Game of Thrones': pd.to_numeric(df['rating_got'], errors='coerce').mean(),
            'Breaking Bad': pd.to_numeric(df['rating_bb'], errors='coerce').mean(),
            'Better Call Saul': pd.to_numeric(df['rating_bcs'], errors='coerce').mean(),
            'Dark': pd.to_numeric(df['rating_dark'], errors='coerce').mean(),
            'The Sopranos': pd.to_numeric(df['rating_sopranos'], errors='coerce').mean(),
            'House of the Dragon': pd.to_numeric(df['rating_hotd'], errors='coerce').mean(),
            'A Knight of the Seven Kingdoms': pd.to_numeric(df['rating_knight'], errors='coerce').mean()
        }
        plt.bar(series_ratings.keys(), series_ratings.values(), color='#764ba2')
        plt.xlabel('Web Series', fontsize=12, fontweight='bold')
        plt.ylabel('Average Rating (1-5)', fontsize=12, fontweight='bold')
        plt.title('Average Rating Per Web Series', fontsize=14, fontweight='bold')
        plt.xticks(rotation=45, ha='right')
        plt.ylim(0, 5)
        plt.tight_layout()
        plt.savefig(os.path.join(CHARTS_DIR, 'average_ratings.png'), dpi=100)
        plt.close()
        
        # Chart 3: Genre Preference Distribution (Pie Chart)
        plt.figure(figsize=(8, 8))
        genre_counts = df['genre_preference'].value_counts()
        colors = ['#667eea', '#764ba2', '#f093fb', '#4facfe', '#43e97b']
        plt.pie(genre_counts.values, labels=genre_counts.index, autopct='%1.1f%%', 
                startangle=90, colors=colors)
        plt.title('Genre Preference Distribution', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig(os.path.join(CHARTS_DIR, 'genre_distribution.png'), dpi=100)
        plt.close()
        
        # Generate HTML to display charts
        html = """
        <!DOCTYPE html>
        <html class="dark" lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Survey Analytics - StreamPulse</title>
            <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
            <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Spline+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
            <script>
                tailwind.config = {
                    darkMode: "class",
                    theme: {
                        extend: {
                            colors: {
                                "primary": "#ec1313",
                                "background-dark": "#0a0a0a",
                            },
                            fontFamily: {
                                "display": ["Spline Sans", "sans-serif"]
                            },
                        },
                    },
                }
            </script>
            <style>
                body {
                    font-family: "Spline Sans", sans-serif;
                    background-color: #0a0a0a;
                }
                .glass-container {
                    background: rgba(20, 15, 15, 0.75);
                    backdrop-filter: blur(24px);
                    border: 1px solid rgba(255, 255, 255, 0.08);
                }
                .bg-overlay-gradient {
                    background: radial-gradient(circle at center, rgba(10, 10, 10, 0.4) 0%, rgba(10, 10, 10, 0.9) 60%, #1a0505 100%);
                    position: fixed;
                    inset: 0;
                    z-index: -5;
                    pointer-events: none;
                }
                .chart-panel {
                    background: rgba(10, 10, 10, 0.6);
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    border-radius: 1rem;
                    padding: 1.5rem;
                    backdrop-filter: blur(8px);
                }
            </style>
        </head>
        <body class="bg-background-dark text-white min-h-screen selection:bg-primary selection:text-white">
            
            <div class="bg-overlay-gradient"></div>
            
            <div class="relative flex min-h-screen flex-col items-center p-4 md:p-8 py-12">
                
                <!-- Header -->
                <header class="w-full max-w-[1200px] flex items-center justify-center mb-8 px-4">
                    <div class="flex items-center gap-3">
                        <div class="size-8 bg-primary rounded-lg flex items-center justify-center">
                            <span class="material-symbols-outlined text-white text-xl">movie_filter</span>
                        </div>
                        <h2 class="text-xl font-bold tracking-tight">StreamPulse</h2>
                    </div>
                </header>
                
                <!-- Main Container -->
                <main class="w-full max-w-[1200px]">
                    <div class="glass-container rounded-xl p-6 md:p-10 shadow-2xl relative z-10">
                        
                        <!-- Page Header -->
                        <div class="mb-8 text-center">
                            <h1 class="text-3xl md:text-4xl font-bold mb-3 tracking-tight">Survey Analytics Dashboard</h1>
                            <div class="flex items-center justify-center gap-2 text-zinc-400">
                                <span class="material-symbols-outlined text-primary">analytics</span>
                                <p class="text-lg">
                                    <strong class="text-white">Total Responses:</strong> """ + str(len(df)) + """
                                </p>
                            </div>
                        </div>
                        
                        <!-- Charts Grid -->
                        <div class="space-y-8">
                            
                            <!-- Chart 1: Favorite Series -->
                            <div class="chart-panel">
                                <h3 class="text-xl font-semibold mb-4 text-zinc-200 flex items-center gap-2">
                                    <span class="material-symbols-outlined text-primary">bar_chart</span>
                                    Most Favorite Web Series
                                </h3>
                                <div class="flex justify-center">
                                    <img src="/static/charts/favorite_series.png" alt="Favorite Series" class="max-w-full h-auto rounded-lg">
                                </div>
                            </div>
                            
                            <!-- Chart 2: Average Ratings -->
                            <div class="chart-panel">
                                <h3 class="text-xl font-semibold mb-4 text-zinc-200 flex items-center gap-2">
                                    <span class="material-symbols-outlined text-primary">star</span>
                                    Average Rating Per Web Series
                                </h3>
                                <div class="flex justify-center">
                                    <img src="/static/charts/average_ratings.png" alt="Average Ratings" class="max-w-full h-auto rounded-lg">
                                </div>
                            </div>
                            
                            <!-- Chart 3: Genre Distribution -->
                            <div class="chart-panel">
                                <h3 class="text-xl font-semibold mb-4 text-zinc-200 flex items-center gap-2">
                                    <span class="material-symbols-outlined text-primary">donut_large</span>
                                    Genre Preference Distribution
                                </h3>
                                <div class="flex justify-center">
                                    <img src="/static/charts/genre_distribution.png" alt="Genre Distribution" class="max-w-full h-auto rounded-lg">
                                </div>
                            </div>
                            
                        </div>
                        
                        <!-- Action Buttons -->
                        <div class="flex flex-col sm:flex-row gap-4 justify-center mt-10">
                            <a href="/" 
                               class="flex items-center justify-center gap-2 px-6 py-3 bg-gradient-to-r from-primary to-[#8b0000] hover:from-[#ff1a1a] hover:to-primary text-white font-semibold rounded-lg shadow-lg transition-all transform hover:scale-[1.02] active:scale-[0.98]">
                                <span class="material-symbols-outlined text-sm">arrow_back</span>
                                Back to Survey
                            </a>
                            <a href="/charts" 
                               class="flex items-center justify-center gap-2 px-6 py-3 bg-black/40 border border-zinc-700/50 hover:border-primary/50 text-white font-semibold rounded-lg transition-all transform hover:scale-[1.02] active:scale-[0.98]">
                                <span class="material-symbols-outlined text-sm">refresh</span>
                                Refresh Charts
                            </a>
                        </div>
                        
                    </div>
                </main>
                
                <!-- Footer -->
                <footer class="w-full max-w-[1200px] flex items-center justify-center mt-8 px-4 text-zinc-500 text-xs border-t border-white/5 pt-6">
                    <p>© 2026 StreamPulse Analytics. All rights reserved.</p>
                </footer>
                
            </div>
            
        </body>
        </html>
        """
        
        return html
    
    except Exception as e:
        return f"Error generating charts: {str(e)}", 500

if __name__ == '__main__':
    # Get port from environment variable (for Render deployment) or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Run the app
    # Use 0.0.0.0 to make it accessible externally (required for Render)
    # Note: CSV initialization happens on first form submission via ensure_csv_exists()
    app.run(host='0.0.0.0', port=port, debug=False)
