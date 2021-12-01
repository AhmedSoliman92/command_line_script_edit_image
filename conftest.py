from platform import platform
import pytest
import os, sys
@pytest.fixture
def image_input():
    return [
        'input.jpg',
        'my_folder/input.jpg',
        'python.png'
            ]
        



@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    config.option.htmlpath = 'report.html'


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    file = session.config.option.htmlpath

    if sys.platform == 'darwin':
        os.system('open -a "Google Chrome" ' + file)
    elif sys.platform == 'win32':
        os.system('start ' + file)
    elif sys.platform == 'linux' or sys.platform == 'linux2':
        os.system('firefox ' + file)