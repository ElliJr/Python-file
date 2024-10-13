import cv2
import mediapipe as mp

# Inicializando a captura de vídeo
cap = cv2.VideoCapture(0)

# Inicializando MediaPipe para detecção de rosto e olhos
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True)

# Função para detectar se os olhos estão olhando diretamente
def eyes_looking_forward(landmarks):
    # Pega os pontos dos olhos (landmarks)
    left_eye = [landmarks[33], landmarks[133]]  # Índices dos pontos da MediaPipe para olho esquerdo
    right_eye = [landmarks[362], landmarks[263]]  # Índices para olho direito

    # Calcula a distância entre os dois pontos para verificar o alinhamento
    left_dist = abs(left_eye[0].x - left_eye[1].x)
    right_dist = abs(right_eye[0].x - right_eye[1].x)

    # Se a distância horizontal dos olhos for pequena, o rosto está diretamente de frente
    return left_dist < 0.015 and right_dist < 0.015

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Falha ao capturar imagem")
        break

    # Converte a imagem para RGB (necessário pelo MediaPipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Faz a detecção dos rostos e marcas faciais
    result = face_mesh.process(rgb_frame)

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:
            # Verifica se os olhos estão olhando para frente
            if eyes_looking_forward(face_landmarks.landmark):
                print("Olhos olhando diretamente para a câmera. Desligando...")
                cap.release()  # Desliga a câmera
                cv2.destroyAllWindows()
                break

    # Exibe a imagem na janela
    cv2.imshow('Camera', frame)

    # Tecla 'q' para sair manualmente
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Finaliza a captura e fecha as janelas
cap.release()
cv2.destroyAllWindows()
