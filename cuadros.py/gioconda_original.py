from obra_arte import ObraArte
from lugar import Lugar

Louvre= Lugar("Museo del Louvre", "París", "Francia")
Gioconda= ObraArte(
    titulo="La Gioconda",
    ac=1503-1516,
    tecnica='Oleo',
    subtecnica='Sfumato',
    soporte='Madera de alamo',
    autor='Leonardo da Vinci',
    estado_conservacion='Regular'
)
Gioconda.asignar_lugar(Louvre)