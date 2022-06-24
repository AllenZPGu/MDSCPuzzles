CALL mdscenv/Scripts/activate
CALL set DEVMODE=True
CALL set SECRET_KEY="ubfxhi$qrj&9$s&^g5lmru3l03h5azq&w@mfso0+*beq71x!8t"
python MDSCProj/manage.py makemigrations
pause
python MDSCProj/manage.py migrate
pause