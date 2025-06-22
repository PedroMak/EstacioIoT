import face_recognition
import serial
import time

# Carrega a primeira imagem e extrai a codificação da face
image1 = face_recognition.load_image_file("foto1.bmp")
encodings1 = face_recognition.face_encodings(image1)

if len(encodings1) > 0:
    encoding1 = encodings1[0]
else:
    print("Nenhuma face detectada na foto1")
    exit()

# Carrega a segunda imagem e extrai a codificação da face
image2 = face_recognition.load_image_file("foto2.jpg")
encodings2 = face_recognition.face_encodings(image2)

if len(encodings2) > 0:
    encoding2 = encodings2[0]
else:
    print("Nenhuma face detectada na foto2")
    exit()

# Compara as duas codificações para verificar se são da mesma pessoa
result = face_recognition.compare_faces([encoding1], encoding2)

print("As faces são iguais?", result[0])

# Se forem iguais, envia o comando ao Arduino para abrir a "porta"
if result[0]:
    try:
        arduino = serial.Serial('COM3', 9600, timeout=1)
        time.sleep(2)
        arduino.write(b'1')
        print("Comando enviado ao Arduino: abrir porta")
        time.sleep(1)
        arduino.close()
    except Exception as e:
        print("Erro ao comunicar com o Arduino:", e)
