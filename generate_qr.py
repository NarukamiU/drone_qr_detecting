import qrcode

# 各コマンドに対応するデータを設定
commands = {
    "takeoff": 0,
    "land": 0,
    "left": 30,  # 未定
    "right": 0,  # 未定
    "up": 0,
    "down": 0,
    "rotate_clockwise": 0,
    "flip": ""  # 未定方向
}

# ファイルパスを指定
file_path = "C:\\DATA\\program\\drone\\img_qr\\"

# 各QRコードを生成
for command, value in commands.items():
    # 値が0または空の場合はスキップ
    if not value:
        continue

    # ファイル名を生成
    file_name = f"{command}_{value}.png"

    # QRコードのデータを生成
    data = f"{command}:{value}"

    # QRコードを生成
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # QRコードを保存
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path + file_name)

    print(f"QRコードを {file_path}{file_name} に保存しました.")
