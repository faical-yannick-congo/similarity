from ..features import hellofeature
import pkg_resources

class TestHello:

    def test_hello(self):
        assert hellofeature.helloworld() == "hello world!"
