import cv2

# 이미지 파일 읽기
image = cv2.imread('qr.png')
if image is None:
    pass
else:
    # QR 코드 검출기 초기화
    detector = cv2.QRCodeDetector()

    # QR 코드 검출
    data, bbox, _ = detector.detectAndDecode(image)

    # 검출된 데이터 출력
    if data:
        print("QR 코드 내용:", data)
        # QR 코드의 경계 상자 그리기
        if bbox is not None:
            for i in range(len(bbox)):
                cv2.polylines(image, [bbox[i].astype(int)], isClosed=True, color=(0, 255, 0), thickness=2)

    # 결과 이미지 표시
    cv2.imshow('QR Code Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
