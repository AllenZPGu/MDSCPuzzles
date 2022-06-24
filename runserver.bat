CALL mdscenv/Scripts/activate
CALL set DEVELOPMENT_MODE=True
CALL set DEBUG=False
CALL set SECRET_KEY="ubfxhi$qrj&9$s&^g5lmru3l03h5azq&w@mfso0+*beq71x!8t"
CALL set DBNAME=
CALL set DBUSER=
CALL set DBPASS=
CALL set LOCALHOST=
python MDSCProj/manage.py runserver 0.0.0.0:8000