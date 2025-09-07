# השלב הראשון: בסיס האימג' הוא Python 3.8.3
FROM python:3.8.3-slim-buster

# הגדרת סביבת עבודה בתוך הקונטיינר
WORKDIR /app

# העתקת קובץ הדרישות והתקנתן
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# העתקת כל קוד הפרויקט
COPY . .

# הרצת בדיקות אוטומטיות כחלק מתהליך הבנייה
RUN python -m unittest test_app.py

# הגדרת משתני סביבה ל-Flask
ENV FLASK_APP=app.py

# חשיפת פורט 5000, הפורט בו Flask רץ
EXPOSE 5000

# הגדרת פקודת ההפעלה של היישום
CMD ["flask", "run", "--host=0.0.0.0"]