from django.conf import settings
from django.contrib.auth.models import User, Group
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.management import call_command
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestChangePostAdmin(StaticLiveServerTestCase):
    def setUp(self):
        # to prevent deleting writer group
        call_command('migrate', 'posts', 'zero')
        call_command('migrate', 'posts')

        writer = User.objects.create_user(username='writer', password='writer', is_staff=True)
        writer.groups.add(Group.objects.get(name='writer'))

        options = Options()
        options.headless = True
        self.browser = webdriver.Chrome(settings.SELENIUM_CHROME_EXECUTABLE_PATH, chrome_options=options)
        self.wait = WebDriverWait(self.browser, 100)

        url = f'{self.live_server_url}/admin/'

        # login
        self.browser.get(url)
        self.browser.find_element(By.CSS_SELECTOR, 'input[name=username]').send_keys('writer')
        self.browser.find_element(By.CSS_SELECTOR, 'input[name=password]').send_keys('writer')
        self.browser.find_element(By.CSS_SELECTOR, 'input[value="Log in"]').click()

        self.browser.find_element(By.LINK_TEXT, 'Posts').click()

        self.browser.find_element(By.LINK_TEXT, 'ADD POST').click()

    def tearDown(self):
        self.browser.close()

    def text_present_in_text_input(self, css_selector):
        element = self.browser.find_element(By.CSS_SELECTOR, css_selector)
        value = element.get_attribute('value')
        if value:
            return value
        else:
            return False

    def test_generate_buttons(self):
        self.browser.find_element(By.CSS_SELECTOR, 'input[name=title]').send_keys('Django web framework')

        self.browser.find_element(By.CSS_SELECTOR, '#generate-content-from-title').click()
        content = self.wait.until(lambda driver: self.text_present_in_text_input('textarea[name=content]'))

        self.assertGreater(len(content), 0)

        self.browser.find_element(By.CSS_SELECTOR, '#generate-summary-from-content').click()
        summary = self.wait.until(lambda driver: self.text_present_in_text_input('textarea[name=summary]'))

        self.assertGreater(len(summary), 0)

        self.browser.find_element(By.CSS_SELECTOR, 'textarea[name=content]').clear()
        self.browser.find_element(By.CSS_SELECTOR, '#generate-content-from-summary').click()
        content = self.wait.until(lambda driver: self.text_present_in_text_input('textarea[name=content]'))

        self.assertGreater(len(content), 0)

        self.browser.find_element(By.CSS_SELECTOR, 'input[name=title]').clear()
        self.browser.find_element(By.CSS_SELECTOR, '#generate-title-from-content').click()
        title = self.wait.until(lambda driver: self.text_present_in_text_input('input[name=title]'))

        self.assertGreater(len(title), 0)

    def test_generate_title_from_content_without_content(self):
        self.browser.find_element(By.CSS_SELECTOR, '#generate-title-from-content').click()
        alert = self.browser.switch_to.alert
        text = alert.text
        alert.accept()

        self.assertEqual(text, 'Please fill out content field.')

    def test_generate_summary_from_content_without_content(self):
        self.browser.find_element(By.CSS_SELECTOR, '#generate-summary-from-content').click()
        alert = self.browser.switch_to.alert
        text = alert.text
        alert.accept()

        self.assertEqual(text, 'Please fill out content field.')

    def test_generate_content_from_title_without_title(self):
        self.browser.find_element(By.CSS_SELECTOR, '#generate-content-from-title').click()
        alert = self.browser.switch_to.alert
        text = alert.text
        alert.accept()

        self.assertEqual(text, 'Please fill out title field.')

    def test_generate_content_from_summary_without_summary(self):
        self.browser.find_element(By.CSS_SELECTOR, '#generate-content-from-summary').click()
        alert = self.browser.switch_to.alert
        text = alert.text
        alert.accept()

        self.assertEqual(text, 'Please fill out summary field.')


class TestAdmin(StaticLiveServerTestCase):
    def test_receive_access_denied_when_user_has_no_permission(self):
        User.objects.create_user(username='user', password='user', is_staff=True)

        options = Options()
        options.headless = True
        browser = webdriver.Chrome(settings.SELENIUM_CHROME_EXECUTABLE_PATH, chrome_options=options)

        url = f'{self.live_server_url}/admin/'

        # login
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR, 'input[name=username]').send_keys('user')
        browser.find_element(By.CSS_SELECTOR, 'input[name=password]').send_keys('user')
        browser.find_element(By.CSS_SELECTOR, 'input[value="Log in"]').click()

        self.assertTrue('You don’t have permission to view or edit anything.' in browser.page_source)
