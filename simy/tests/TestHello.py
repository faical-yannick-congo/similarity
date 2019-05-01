from ..features import hellofeature
import pkg_resources

class TestHello:

    def test_hello(self):
        """The helloworld feature tester.
        """
        assert hellofeature.helloworld() == "hello world!"
