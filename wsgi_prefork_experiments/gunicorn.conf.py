from sample import endpoints

preload_app = True

# effectively have (2 + 1) clients connect at a time, rest will try to connect till connect timeout
workers = 2
backlog = 1
timeout = 20


def pre_fork(server, worker):
    endpoints.load_shared()

def post_worker_init(worker):
    endpoints.load_local()
