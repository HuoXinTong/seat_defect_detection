import cv2
import os

# 图像去噪、阈值分割、轮廓提取和跟踪函数
def preprocess_image(path, image, cnt):
    # 图像灰度化
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 图像去噪
    denoised = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)
    
    # 阈值分割
    _, threshold = cv2.threshold(denoised, 200, 255, cv2.THRESH_BINARY)
    
    # 轮廓提取
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 跟踪轮廓，并绘制外接矩形
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cropped_img = image[y:y+50, x:x+50]
        cropped_img = cv2.resize(cropped_img, (50, 50))
        cv2.imwrite(path + str(cnt) + '.jpg', cropped_img)
        cnt += 1
    return image, cnt


# 处理正样本
# pos_path = os.getcwd() + "\\positive_sample\\"
# pos_train_path = os.getcwd() + "\\pos_train\\"
# cnt = 1
# for file in os.listdir(pos_path):
#     img = cv2.imread(pos_path + file)
#     if img is None:
#         print("Failed to read image file:", pos_path + file)
#         continue
    
#     # 图像预处理
#     processed_img, cnt = preprocess_image(pos_train_path, img, cnt)
    
#     # 保存处理后的图像
#     # cv2.imwrite(pos_train_path + str(cnt) + '.jpg', processed_img)
#     # cnt += 1

# 处理正样本
pos_path = os.getcwd() + "\\pos_sample\\"
pos_train_path = os.getcwd() + "\\pos_train\\"
cnt = 1
for file in os.listdir(pos_path):
    img = cv2.imread(pos_path + file)
    if img is None:
        print("Failed to read image file:", pos_path + file)
        continue
    
    # 图像预处理
    # processed_img, cnt = preprocess_image(pos_train_path, img, cnt)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (20, 20))
    
    # 保存处理后的图像
    cv2.imwrite(pos_train_path + str(cnt) + '.jpg', gray)
    cnt += 1


# 处理负样本
impos_path = os.getcwd() + "\\impositive_sample\\"
impos_train_path = os.getcwd() + "\\impos_train\\"
cnt = 1
for file in os.listdir(impos_path):
    img = cv2.imread(impos_path + file)
    if img is None:
        print("Failed to read image file:", pos_path + file)
        continue
    
    # 图像预处理
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 灰度化
    img = cv2.resize(img, (300, 300)) # 大小改为300*300
    cv2.imwrite(impos_train_path + str(cnt) + '.jpg', img)
    cnt += 1