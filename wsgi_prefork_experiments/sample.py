from time import sleep
import os
import falcon


class StatelessResources:
    def __init__(self):
        self.loaded = False
        self.state = None

    def load(self):
        self.loaded = True
        self.state = os.getpid()
        print(f"loaded Stateless in {os.getppid()} > {os.getpid()}")


class StatefulResources:
    def __init__(self):
        self.loaded = False
        self.state = None

    def load(self):
        self.loaded = True
        self.state = os.getpid()
        print(f"loaded Stateful in {os.getppid()} > {os.getpid()}")


class SagemakerEndpoints:
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2

    def on_get(self, req, resp):
        assert self.r1.loaded and self.r2.loaded

        resp.content_type = falcon.MEDIA_JSON
        resp.media = self.response()

    def on_post(self, req, resp):
        resp.content_type = falcon.MEDIA_JSON
        resp.media = self.response()
        sleep(10)

    def response(self):
        return {'r1': self.r1.state, 'r2': self.r2.state}

    def load_shared(self):
        r1.load()

    def load_local(self):
        r2.load()


r1 = StatelessResources()
r2 = StatefulResources()
endpoints = SagemakerEndpoints(r1, r2)

app = falcon.App()
app.add_route('/ping', endpoints)
app.add_route('/invocations', endpoints)
