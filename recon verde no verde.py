from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='c8cd22d155ce4e6f95c8f2090cfd9b83')
model = app.models.get('verde y noverde')
from clarifai.rest import Image as ClImage

archivo = input("Ingresa una imagen: ")
#uso la linea siguiente para probar con alguna imagen guardada 
image = ClImage(file_obj=open(archivo, 'rb'))

#uso la linea siguiente si quiero probar con alguna imagen de internet
#image = ClImage(url=archivo)

result = {}
result=model.predict([image])

resumen = result['outputs'][0]['data']['concepts']


for x in resumen:
    if x['value'] > 0.1:# imprimo los resultados con probab. mayor a 10%
        print (x['name'], x['value'])
