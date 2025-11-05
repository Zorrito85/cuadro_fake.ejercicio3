from obra_arte import ObraArte
from lugar import Lugar

prado=Lugar("Museo del Prado", "Madrid", "España")

Gioconda_fake= ObraArte(
    titulo="La Gioconda de El Prado",
    ac=1503-1516,
    tecnica='Oleo',
    subtecnica='Pincelada simple',
    soporte='Madera Nogal',
    autor='Desconocido',
    estado_conservacion='Buena'
)

Gioconda_fake.asignar_lugar(prado)