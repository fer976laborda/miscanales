# Mis Canales

Landing page estática con acceso a los canales de YouTube de Fernando y 3 vídeos destacados embebidos por cada canal.

## Uso

Abre `index.html` en cualquier navegador para ver los canales y reproducir los vídeos desde la misma página.

## Verificación

Ejecuta:

```bash
python -m unittest discover -s tests -v
```

para validar que el HTML mantiene:
- 4 enlaces de canal,
- atributos de seguridad en enlaces externos,
- 12 vídeos embebidos con formato de URL correcto.
