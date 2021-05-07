from dataiku.doctor.plugins.custom_prediction_algorithm import BaseCustomPredictionAlgorithm
from sklearn.ensemble import AdaBoostRegressor
from dku_utils import cast_parameters

class CustomPredictionAlgorithm(BaseCustomPredictionAlgorithm):    
    def __init__(self, prediction_type=None, params=None):    
        formatted_parameters = cast_parameters(params)
        self.clf = AdaBoostRegressor(random_state=formatted_parameters.get('random_state', None))
        super(CustomPredictionAlgorithm, self).__init__(prediction_type, formatted_parameters)
    
    def get_clf(self):
        return self.clf
