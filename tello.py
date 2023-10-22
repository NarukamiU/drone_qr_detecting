import cv2
from pyzbar.pyzbar import decode

# QRコードを読むためのカメラを初期化
cap = cv2.VideoCapture(0)  # カメラデバイスの番号を指定

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # QRコードを読み取り
    decoded_objects = decode(frame)
    
    # 画面に表示するテキスト
    display_text = []

    for obj in decoded_objects:
        data = obj.data.decode('utf-8')
        print(f"QR Code Data: {data}")

        # QRコードデータをコンマで分割
        qr_data = data.split(',')

        # 各QRコマンドごとに画面情報を初期化
        display_text = []

        for qr_command in qr_data:
            # 各QRコマンドの形式は "コマンド=値" とする
            command, value = qr_command.split(':')

            # 新しいコマンド情報を画面に表示
            display_text.append(f"{command}:{value}")

            # QRコードのバウンディングボックスの座標を取得
            rect_points = obj.polygon

            if len(rect_points) == 4:
                # 矩形を描画
                for j in range(4):
                    cv2.line(frame, tuple(rect_points[j]), tuple(rect_points[(j+1) % 4]), (0, 255, 0), 3)

    # 画面にテキストを表示
    text_to_display = ", ".join(display_text)
    cv2.putText(frame, text_to_display, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 画面に映像を表示
    cv2.imshow('QR Code Detection', frame)

    # 'q' キーを押すとプログラムが終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
