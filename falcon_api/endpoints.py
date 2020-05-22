import falcon
from falcon_cors import CORS

from api import resources

cors = CORS(
    allow_all_origins=True,
    allow_all_headers=True,
    allow_all_methods=True,
    )
routes = falcon.API(middleware=[cors.middleware])

inch_worm = resources.InchWorm()
routes.add_route('/inchworm', inch_worm)
