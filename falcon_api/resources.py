
import json
import falcon
from analytics import utils, logic

class InchWorm(object):

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')

    def on_post(self, req, resp):
        """Handles POST requests"""
#         data = req.media
#         resp.media = {
#             'text': 'POST POST BABY!',
#             'data': data
#         }
#         print(type(resp.media), resp.media)
#         resp.status = falcon.HTTP_200

		input_df = utils.transform_keypoint_payload(req.media)
		resp.media = {
            'text': 'POST POST BABY!',
            'left-wrist-left-shoulder-angle': input_df.apply(
                lambda row: logic.angle_between_joints(
                    row, 
                    'leftWrist', 
                    'leftShoulder'
                )
            ), axis=1).mean(),
            'left-arm-perpendicular': input_df.apply(
                lambda row: logic.bodypart_is_vertical(
                    row, 
                    'leftWrist', 
                    'leftShoulder'
                )
            ), axis=1).max(),
            'left-knee-angle': input_df.apply(
                lambda row: logic.diff_between_joint_angles(
                    row, 
                    'leftAnkle', 
                    'leftKnee', 
                    'leftKnee', 
                    'leftHip'
                )
            ), axis=1).mean(),
            'left-knee-straight': input_df.apply(
                lambda row: inch_worm.knees_straight(
                    row, 
                    'leftAnkle', 
                    'leftKnee', 
                    'leftKnee', 
                    'leftHip'
                )
            ), axis=1).mean(),
            'exercise-start-position': inch_worm.is_inchworm_start_position(input_df)
        }
        print(resp.media)
        resp.status = falcon.HTTP_200

