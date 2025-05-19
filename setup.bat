@echo off
echo Instalando entorno virtual...
python -m venv venv

echo Activando entorno virtual...
call venv\Scripts\activate.bat

echo Instalando dependencias...
pip install -r requirements.txt

echo Iniciando aplicación...
streamlit run app.py

pause 