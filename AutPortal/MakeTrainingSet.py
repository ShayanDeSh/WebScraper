import requests as request
import cv2
import matplotlib.image as mpimg
import os
import glob


def get_cap():
    for i in range(1000):
        login_page = request.get('https://portal.aut.ac.ir/aportal/')
        cookies = {'JSESSIONID': login_page.cookies.get('JSESSIONID')}
        image = request.get('https://portal.aut.ac.ir/aportal/PassImageServlet', cookies=cookies)
        saveCap = 'cap\\' + i.__str__() + '.jpeg'
        open(saveCap, 'wb').write(image.content)
        image = cv2.imread(saveCap)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        t = i * 5
        cv2.imwrite('let\\' + t.__str__() + '.jpeg', gray[0:40, 0:30])
        cv2.imwrite('let\\' + (t + 1).__str__() + '.jpeg', gray[0:40, 30:60])
        cv2.imwrite('let\\' + (t + 2).__str__() + '.jpeg', gray[0:40, 60:90])
        cv2.imwrite('let\\' + (t + 3).__str__() + '.jpeg', gray[0:40, 90:120])
        cv2.imwrite('let\\' + (t + 4).__str__() + '.jpeg', gray[0:40, 120:150])


def split_labeled():
    captcha_image_files = glob.glob(os.path.join('labeled', "*"))
    for i in range(captcha_image_files.__len__()):
        image = cv2.imread(captcha_image_files[i])
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if not os.path.exists('let\\' + captcha_image_files[i][8]):
            os.makedirs('let\\' + captcha_image_files[i][8])
        if not os.path.exists('let\\' + captcha_image_files[i][9]):
            os.makedirs('let\\' + captcha_image_files[i][9])
        if not os.path.exists('let\\' + captcha_image_files[i][10]):
            os.makedirs('let\\' + captcha_image_files[i][10])
        if not os.path.exists('let\\' + captcha_image_files[i][11]):
            os.makedirs('let\\' + captcha_image_files[i][11])
        if not os.path.exists('let\\' + captcha_image_files[i][12]):
            os.makedirs('let\\' + captcha_image_files[i][12])
        t = i * 5
        cv2.imwrite('let\\' + captcha_image_files[i][8] + '\\' + t.__str__() + '.jpeg', gray[0:40, 0:30])
        cv2.imwrite('let\\' + captcha_image_files[i][9] + '\\' + (t + 1).__str__() + '.jpeg', gray[0:40, 30:60])
        cv2.imwrite('let\\' + captcha_image_files[i][10] + '\\' + (t + 2).__str__() + '.jpeg', gray[0:40, 60:90])
        cv2.imwrite('let\\' + captcha_image_files[i][11] + '\\' + (t + 3).__str__() + '.jpeg', gray[0:40, 90:120])
        cv2.imwrite('let\\' + captcha_image_files[i][12] + '\\' + (t + 4).__str__() + '.jpeg', gray[0:40, 120:150])


split_labeled()
