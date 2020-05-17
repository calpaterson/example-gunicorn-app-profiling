# The gunicorn "configuration" file

import cProfile

profile = cProfile.Profile()

def pre_request(worker, req):
    print("enabling profile for the request")
    profile.enable()

def post_request(worker, req, *args):
    profile.disable()
    print("request done, profile disabled now")

def worker_exit(server, worker):
    profile.dump_stats("latest.pstats")
    print("process exiting, dumping stats to file")
