import os

def check_file_content(filepath, search_strings, missing_strings=[]):
    if not os.path.exists(filepath):
        print(f"❌ File not found: {filepath}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    all_present = True
    for s in search_strings:
        if s not in content:
            print(f"❌ Missing in {os.path.basename(filepath)}: {s}")
            all_present = False
        else:
            print(f"✅ Found in {os.path.basename(filepath)}: {s}")

    for s in missing_strings:
        if s in content:
            print(f"❌ Should be removed from {os.path.basename(filepath)}: {s}")
            all_present = False
        else:
            print(f"✅ Correctly removed from {os.path.basename(filepath)}: {s}")
            
    return all_present

print("Verifying Backend (app.py)...")
backend_checks = [
    "'rating_dexter'",
    "'rating_vikings'",
    "'rating_twinpeaks'",
    "request.form.get('rating_dexter', 0)",
    "request.form.get('rating_vikings', 0)",
    "request.form.get('rating_twinpeaks', 0)",
    "'Dexter': pd.to_numeric(df['rating_dexter']",
    "'Vikings': pd.to_numeric(df['rating_vikings']",
    "'Twin Peaks': pd.to_numeric(df['rating_twinpeaks']"
]
backend_missing = [
    "'rating_knight'",
    "request.form.get('rating_knight', 0)",
    "'A Knight of the Seven Kingdoms': pd.to_numeric"
]
check_file_content('app.py', backend_checks, backend_missing)

print("\nVerifying Frontend (templates/index.html)...")
frontend_checks = [
    'value="Dexter"',
    'value="Vikings"',
    'value="Twin Peaks"',
    'name="rating_dexter"',
    'name="rating_vikings"',
    'name="rating_twinpeaks"'
]
frontend_missing = [
    'value="A Knight of the Seven Kingdoms"',
    'name="rating_knight"'
]
check_file_content('templates/index.html', frontend_checks, frontend_missing)
