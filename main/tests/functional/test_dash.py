from dashbored.tests import *

class TestDashController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='dash', action='index'))
        # Test response...
