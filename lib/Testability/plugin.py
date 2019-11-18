from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary.keywords.javascript import JavaScriptKeywords
from os.path import abspath, dirname
from .listener import TestabilityListener
from robot.utils import is_truthy, timestr_to_secs, secs_to_timestr
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException



class SeleniumTestability(LibraryComponent):

    def __init__(self, ctx, automatic_wait=True, timeout="30 seconds", error_on_timeout=True, automatic_injection=True):
        LibraryComponent.__init__(self, ctx)
        self.js = JavaScriptKeywords(ctx)
        self.CWD = abspath(dirname(__file__))
        self.ctx.event_firing_webdriver = TestabilityListener
        self.ctx.testability_settings = {"testability": self}
        self.automatic_wait = automatic_wait
        self.automatic_injection = automatic_injection
        self.error_on_timeout = error_on_timeout
        self.timeout = timeout

    @keyword
    def inject_testability(self):
        with open(self.api_file, 'r') as f:
            buf = f.read()
            self.js.execute_javascript("{}; window.testability = testability;".format(buf))

        with open(self.bindings_file, 'r') as f:
            buf = f.read()
            self.js.execute_javascript("{}; window.instrumentBrowser = instrumentBrowser;".format(buf))

    @keyword
    def is_testability_installed(self):
        return self.js.execute_javascript(JS_LOOKUP["is_installed"])

    @keyword
    def instrument_browser(self):
        if not self.is_testability_installed():
            self.inject_testability()
            self.js.execute_javascript(JS_LOOKUP["instrument_browser"])
            
    @keyword
    def wait_for_document_ready(self):
        self.js.execute_async_javascript(JS_LOOKUP["wait_for_document_ready"])