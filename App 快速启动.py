# author:CC
# email:yangdeyi1201@foxmail.com

from appium.webdriver import Remote

caps = {'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'app': r'H:\Dropbox\APK\Future-release-2018.apk'}

# 初始化客户端
driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities=caps)
