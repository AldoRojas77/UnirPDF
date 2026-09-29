import fitz


PDF_1 = "pdf1.pdf"
PDF_2 = "pdf2.pdf"
PDF_SALIDA = "resultado.pdf"


# Abrir los dos PDF
pdf1 = fitz.open(PDF_1)
pdf2 = fitz.open(PDF_2)

# Crear PDF nuevo
resultado = fitz.open()


# Comprobar que tengan la misma cantidad de páginas
if len(pdf1) != len(pdf2):
    print("Error: los PDF no tienen la misma cantidad de páginas.")
    print(f"PDF 1: {len(pdf1)} páginas")
    print(f"PDF 2: {len(pdf2)} páginas")
    exit()


# Combinar página por página
for i in range(len(pdf1)):

    pagina1 = pdf1[i]
    pagina2 = pdf2[i]

    # Tamaño de la primera página
    ancho = pagina1.rect.width
    alto = pagina1.rect.height

    # Crear una hoja con el doble de altura
    nueva_pagina = resultado.new_page(
        width=ancho * 2,
        height=alto 
    )

    # Primera página arriba
    nueva_pagina.show_pdf_page(
        fitz.Rect(
            0,
            0,
            ancho,
            alto
        ),
        pdf1,
        i
    )

    # Segunda página abajo
    nueva_pagina.show_pdf_page(
        fitz.Rect(
            ancho,
            0,
            ancho * 2,
            alto
        ),
        pdf2,
        i
    )


# Guardar resultado
resultado.save(PDF_SALIDA)

# Cerrar archivos
pdf1.close()
pdf2.close()
resultado.close()


print("PDF creado correctamente.")
print(f"Archivo: {PDF_SALIDA}")