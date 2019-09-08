import requests as request
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import cv2

user_name = ''
password = ''
courses = [
    {'st_reg_courseid': '3103053', 'st_reg_groupno': '1'}
]
login_page = request.get('https://portal.aut.ac.ir/aportal/')
cookies = {'JSESSIONID': login_page.cookies.get('JSESSIONID')}


def getting_captcha():
    global image, captcha, home_page
    image = request.get('https://portal.aut.ac.ir/aportal/PassImageServlet', cookies=cookies)
    open('captcha.jpeg', 'wb').write(image.content)
    # img = Image.open('captcha.png').convert('LA')
    # img.save('captcha.png')
    img = mpimg.imread('captcha.jpeg')
    imgplot = plt.imshow(img)
    plt.show()
    image = cv2.imread('captcha.jpeg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # gray = cv2.copyMakeBorder(gray, 8, 8, 8, 8, cv2.BORDER_REPLICATE)
    # thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    # contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #
    # contours = contours[1]
    #
    # letter_image_regions = []
    #
    # for contour in contours:
    #     print(cv2.boundingRect(contour))
    #     x, y, w, h = cv2.boundingRect(contour)
    #     if w / h > 1.25:
    #         half_width = int(w / 2)
    #         letter_image_regions.append((x, y, half_width, h))
    #         letter_image_regions.append((x + half_width, y, half_width, h))
    #     else:
    #         letter_image_regions.append((x, y, w, h))
    #
    # if len(letter_image_regions) != 5:
    #     print("elor")

    # for i in range(letter_image_regions.__len__()):
    #     x, y, w, h = letter_image_regions[i]
    #     letter_image = gray[y - 2:y + h + 2, x - 2:x + w + 2]
    #     save = i.__str__() + '.png'
    #     cv2.imwrite(save, letter_image)
    cv2.imwrite('test1.jpeg', gray[0:40, 0:30])
    cv2.imwrite('test2.jpeg', gray[0:40, 30:60])
    cv2.imwrite('test3.jpeg', gray[0:40, 60:90])
    cv2.imwrite('test4.jpeg', gray[0:40, 90:120])
    cv2.imwrite('test5.jpeg', gray[0:40, 120:150])
    print('here')
    input()
    print('Enter Captcha:')
    captcha = input()
    return captcha


while True:
    captcha = getting_captcha()
    home_page = request.post('https://portal.aut.ac.ir/aportal/login.jsp', cookies=cookies, allow_redirects=True,
                             data={'username': user_name, 'password': password, 'passline': captcha})
    soup = BeautifulSoup(home_page.text, 'html5lib')
    title = soup.find('title')
    if title.text == 'Login':
        print('Unable to login trying again')
        time.sleep(0.5)
        cookies = {'JSESSIONID': home_page.cookies.get('JSESSIONID')}
    else:
        print('------------------')
        print('LOGGED IN')
        print('------------------')
        break

for course in courses:
    request.get(
        'https://portal.aut.ac.ir/aportal/regadm/student.portal/student.portal.jsp?action=edit&st_info=register&st_sub_info=0',
        cookies=cookies)
    captcha = getting_captcha()
    token_course = request.post(
        'https://portal.aut.ac.ir/aportal/regadm/student.portal/student.portal.jsp?action=apply_reg&st_info=drop',
        cookies=cookies, allow_redirects=True,
        data={'st_reg_courseid': course.get('st_reg_courseid'), 'st_reg_groupno': course.get('st_reg_groupno'),
              'addpassline': captcha})
    soup = BeautifulSoup(token_course.text, 'html5lib')
    print(soup.find('td', {'class': 'frmtrc'}).text)
# cookies = login_page.cookies._cookies.get('portal.aut.ac.ir').get('/aportal').get('JSESSIONID')
# print(type(cookies))
