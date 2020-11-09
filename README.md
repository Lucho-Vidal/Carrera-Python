# Carrera-Python
Juego donde se debe esquivar otros autos 

PlanCarrera
Aplicacion web para asistir a la planificacion de la carrera, proyecto para Seminario de lenguajes, UNLa, 2014

Antes de trabajar:

git pull https://github.com/Atixx/PlanCarrera
git branch (para ver si estas en la rama correcta)
git checkout <nombre de rama para trabajar>
trabajar....

git status (para ver que cambio)
git add archivo1.py ... (los archivos que cambiaron)
git checkout archivo2.html ... (los archivos que cambiaron pero son parte de la actualizacion)
git commit -m "este mensaje explica que hice"
git push https://github.com/<USER>/PlanCarrera
Sync DB:

python manage.py dumpdata <your_app> > temp_data.json
python manage.py sqlclear <your_app> | python manage.py dbshell
python manage.py syncdb
python manage.py loaddata temp_data.json
LPPG! :) (get or 404)
