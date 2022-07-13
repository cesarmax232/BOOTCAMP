#MIT Licence

#importamos librerias ncesarias
import tflite_runtime.interpreter as tflite
import cv2
import numpy as np
import urllib.request
import paho.mqtt.client as mqtt

#importamos el modelo tflite
interpreter = tflite.Interpreter('model_lite.tflite')
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

#constantes, variables e instancias necesarias
clases = ["papel_carton", "plastico"] #categorias
url = 'http://localhost:8080/action=snapshot'
value = 30 # valor luminosidad
lim = 255 - value
clasify = 0
mask = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=200, detectShadows=True)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
filter_window=0
motions=0
detection=0
start_sensor=1

#funcion para obtener frame procesada
def getFrame():
  imgResponse = urllib.request.urlopen(url) #obtiene imagen raw response
  imgNp = np.array(bytearray(imgResponse.read()),dtype=np.uint8) #covierte a numpy
  image = cv2.imdecode(imgNp, -1) #decodifica imagen
  lab = cv2.cvtColor(image, cv2.COLOR_RGB2LAB) #convierte a LAB
  lab_chanels = cv2.split(lab) # Divide lso canales a L, A, B
  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)) #crea clahe
  lab_chanels[0] = clahe.apply(lab_chanels[0]) += value #aumenta brillo
  lab = cv2.merge(lab_chanels) #vuelve a juntar los canales LAB
  rgb = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB) #convierte a RGB
  rgb = cv2.resize(rgb, (224, 224)) #resize a 224 pixeles
  client.publish("clahe", rgb) # muestra imagen en web
  rgb = rgb.reshape(1, rgb.shape[0], rgb.shape[1], rgb.shape[2]) #expande dimension para el modelo
  rgb = rgb.astype(np.float32)/255.0 #normaliza imagen de 0 a 1
  return rgb

#funcion que recibe ordenes de la web
def on_message(client, userdata, msg):
  global clasify, start_sensor, detection
  #muestra informacion del mensaje
  print("message received " ,str(msg.payload.decode("utf-8")))
  print("message topic=",msg.topic)
  print("message qos=",msg.qos)
  print("message retain flag=",msg.retain)
  #recibe la orden respectiva
  if (str(msg.topic) == "clasify"):
    clasify = 1
  if (str(msg.topic) == "motion"):
    start_sensor = 1
  if (str(msg.topic) == "detection"):
    flag = str(msg.payload.decode("utf-8"))
    if flag == "1":
      detection = 1
    elif flag == "0":
      detection = 0

#establece comunicacion con el broker
client = mqtt.Client("T1")
client.on_message = on_message
client.connect("localhost", 1883)
client.subscribe("clasify")
client.subscribe("motion")
client.subscribe("detection")
client.loop_start()

print("start!")
while True:
  imgResponse = urllib.request.urlopen(url) #obtiene imagen raw response
  imgNp = np.array(bytearray(imgResponse.read()),dtype=np.uint8) #covierte a numpy
  image = cv2.imdecode(imgNp, -1) #decodifica imagen
  client.publish("image", image) # muestra imagen en web
  binary = mask.apply(image, learningRate=0.04) #aplica sustraccion de fondo
  binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel) #aplica filtro opening
  binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel) #aplica filtro closing
  binary = cv2.dilate(binary, None, iterations=5) #aplica dilatacion 5 veces
  binary[binary==127]=0 #elimina sombras
  contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #encuentra contornos
  cv2.fillPoly(binary, pts=contours, color=(255,255,255)) #aplica region filling
  client.publish("binary", binary) # muestra imagen en web

  if start_sensor == 1 and detection == 1: #si la web permite la detecion de movimiento
    cnts = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] #encuentra contornos
    for cnt in cnts: #itera en los contornos
      if cv2.contourArea(cnt) > 200: #umbral para el area
        filter_window = filter_window+1 #incrementa contador
      if filter_window >= 20: #movimiento detectado
        motions = 1
    if len(cnts)==0 and motions==1: #reinicia contadores y variables
      print("motion detection!!")
      filter_window = 0
      motions = 0
      start_sensor = 0
      clasify = 1

  if clasify == 1: #si la web permite la clasificacion
    clasify=0 #reinicia variable
    interpreter.set_tensor(input_details[0]['index'], getFrame()) #pasa frame al modelo
    interpreter.invoke() #realiza la inferencia
    raw_out=np.squeeze(interpreter.get_tensor(output_details[0]['index'])) #obtiene la salida
    index=np.argmax(raw_out) #obtiene probabilidad mas alta
    print(clases[index], max(raw_out))
    if max(raw_out) < 0.92: #si la probabilidad no supera umbral se manda el residuo al contenedor general
      client.publish("general", "1")
    else:
      if clases[index] == "papel_carton":#si la prob es alta y es de categoria papel carton
        client.publish("papel_carton", "1")
      elif clases[index] == "plastico": #si la prob es alta y es de categoria plastico
        client.publish("plastico", "1")
