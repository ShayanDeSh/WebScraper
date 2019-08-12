import requests as request
from bs4 import BeautifulSoup
import time

user_name = ''
password = ''
courses = [

]
login_page = request.get('https://portal.aut.ac.ir/aportal/')
cookies = {'JSESSIONID': login_page.cookies.get('JSESSIONID')}


def getting_captcha():
    global image, captcha, home_page
    image = request.get('https://portal.aut.ac.ir/aportal/PassImageServlet', cookies=cookies)
    open('captcha.jpeg', 'wb').write(image.content)
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
