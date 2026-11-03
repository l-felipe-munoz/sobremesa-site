#!/usr/bin/env python3
"""Copia y optimiza los assets de marca desde el sistema Sobremesa. Uso: python3 sync-brand.py"""
import shutil, os
from PIL import Image, ImageOps
M="/workspace/negocio-info/ceo-autonomo/marca/sobremesa"; O="assets/img"; os.makedirs(O,exist_ok=True)
for f in ["sobremesa-horizontal-claro","sobremesa-horizontal-lema-claro","producto-sazon-endorsed-claro","sobremesa-icono-claro","sobremesa-horizontal-oscuro"]:
    shutil.copy(f"{M}/logo/svg/{f}.svg",O)
for f in ["favicon.ico","favicon-claro.svg","favicon-claro-32.png","favicon-claro-192.png","favicon-claro-512.png","apple-touch-icon.png"]:
    shutil.copy(f"{M}/favicons/{f}",O)
for src,n in [("framer-portada-1600x1200","sazon-portada"),("muestra-01-1600x1200","sazon-muestra-01"),("muestra-02-1600x1200","sazon-muestra-02"),("muestra-03-1600x1200","sazon-muestra-03")]:
    im=Image.open(f"{M}/ventas/{src}.png").convert("RGB"); im.thumbnail((1400,1050))
    for ext in ["webp","jpg"]:
        p=f"{O}/{n}.{ext}"; q=82; im.save(p,quality=q,optimize=True)
        while os.path.getsize(p)>290000: q-=8; im.save(p,quality=q,optimize=True)
ImageOps.fit(Image.open(f"{M}/ventas/lemon-portada-1200x900.png").convert("RGB"),(1200,630)).save(f"{O}/og-sazon.jpg",quality=84,optimize=True)
ImageOps.fit(Image.open(f"{M}/lamina-resumen.png").convert("RGB"),(1200,630)).save(f"{O}/og-home.jpg",quality=84,optimize=True)
shutil.copy(f"{M}/tokens/tokens.css","assets/css/tokens.css")
print("ok")
