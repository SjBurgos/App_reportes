from django.shortcuts import render,HttpResponse
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from reportlab.lib.colors import HexColor
from datetime import datetime

class ReportePersonasPDF(View):
    def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/imagenes/espol.png'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 740, 190, 90,preserveAspectRatio=True)
        #Se dibuja una linea horizontal
        pdf.line(260,740,35,740)
        # Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Times-Roman", 10)
        # Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(400, 790, u" PERFIL DE EMPRESAS")
        pdf.drawString(426, 770, u"CÓDIGO EVENTO ")
        pdf.drawString(466, 750, u"########")
        pdf.drawString(35, 720, u"Programa:") ; pdf.drawString(260, 720, u"Duración:")
        pdf.drawString(35, 705, u"Promoción:") ; pdf.drawString(260, 705, u"Fecha Inicio:")
        pdf.drawString(35, 690, u"Curso:") ; pdf.drawString(260, 690, u"Fecha Final:")
        pdf.drawString(35, 675, u"Instructor:") ; pdf.drawString(260, 675, u"Tipo de Capacitación:")
    def pie_pagina(self,pdf):
        pdf.setFillColor(HexColor(308011))
        pdf.drawString(10, 60, u" /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        pdf.setFillColor(HexColor(000000))
        page_num = pdf.getPageNumber()
        text = "Pag %s" % page_num
        pdf.drawString(500, 30, text)
        pdf.drawString(35,50 ,u'CEC ESPOL, Campus Gustavo Galindo Velasco | Teléf:042269763 | 0960507588 ')
        now = datetime.now()
        pdf.drawString(35,35, u"Fecha impresión:"+str(now.day)+'/'+str(now.month)+'/'+str(now.year))
        pdf.drawString(260, 35,u'Usuario')

    def tabla(sef,pdf):
            pdf.setFont("Times-Roman", 17)
            pdf.drawString(240, 650, u'REPORTE DE ?')
            pass
    def get(self, request, *args, **kwargs):
            #Indicamos el tipo de contenido a devolver, en este caso un pdf
            response = HttpResponse(content_type='application/pdf')
            #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
            buffer = BytesIO()
            #Canvas nos permite hacer el reporte con coordenadas X y Y
            pdf = canvas.Canvas(buffer)
            #Llamo al método donde están definidos los datos que aparecen en el reporte.
            self.cabecera(pdf)
            self.pie_pagina(pdf)
            self.tabla(pdf)
            #Con show page hacemos un corte de página para pasar a la siguiente
            pdf.showPage()
            pdf.save()
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response