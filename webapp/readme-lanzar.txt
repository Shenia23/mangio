# serve with hot reload at localhost:8080
cd frontend
npm run dev

# serve back-end at localhost:5000
cd ../backend
source venv/bin/activate ##para mi es venv/Scripts/activate 
cd ..
FLASK_APP=run.py flask run
