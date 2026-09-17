# Snake Neon — versión móvil

Esta versión está preparada para ejecutarse en **teléfonos Android en orientación horizontal**.

## Controles táctiles
- ▲ arriba
- ◀ izquierda
- ▼ abajo
- ▶ derecha
- PAUSA
- También puedes deslizar el dedo sobre el tablero.

Los eventos táctiles de Android se convierten automáticamente a los controles del juego,
por lo que el menú, ajustes, pausa y demás botones también responden al toque.

## Crear la APK

Necesitas **Linux o WSL2**, Python 3, Buildozer, Java/OpenJDK y las herramientas de Android.

Desde la carpeta `snake_game`:

```bash
buildozer android debug
```

La APK quedará normalmente en la carpeta `bin/`.

Para instalarla en un teléfono conectado por USB:

```bash
buildozer android deploy run
```

## Importante

- El juego está pensado para **modo horizontal (landscape)** para conservar el tablero
  y los controles grandes.
- La conexión a Internet del modo multijugador requiere permiso de `INTERNET`.
- En Windows puro, Buildozer normalmente se ejecuta mediante **WSL2**.

## Mejora móvil 2.0

- Controles táctiles más grandes y separados para facilitar el uso con los dedos.
- Botón de pausa más grande.
- D-pad con diseño visual tipo juego móvil.
- Las coordenadas de los controles están centralizadas en `snake_game/config.py` para evitar desajustes entre dibujo y toque.
- Se mantiene el gesto de deslizar para cambiar de dirección.
- Se añade soporte para el botón Atrás de Android durante una partida.
- Se conserva el lienzo lógico 1000x700 y la orientación horizontal para no modificar la lógica, tablero, modos, puntuaciones ni multijugador.


## Interfaz móvil responsive

La versión 3.0 conserva el lienzo lógico del juego para no alterar la lógica de la
serpiente, pero mejora la presentación en teléfonos de distintos tamaños:

- Pantalla completa real en Android.
- Escalado automático con `pygame.SCALED`.
- Orientación horizontal (`landscape`) para mantener el tablero completo.
- Botones con zona de toque ligeramente mayor que su borde visual.
- Controles y textos conservan sus proporciones al cambiar la resolución física.
- El botón Atrás de Android funciona durante la partida y desde las pantallas
  de pausa/finalización.

No es necesario modificar las reglas, puntuaciones, modos, guardado ni el
multijugador para utilizar esta adaptación.
