
import dataiku
from dataiku.runnables import Runnable


class MyRunnable(Runnable):
    def __init__(self, project_key, config, plugin_config):
        self.project_key = project_key
        self.config = config
        self.plugin_config = plugin_config
        self.client = dataiku.api_client()

    def get_progress_target(self):
        return None

    def run(self, progress_callback):
        code_env = self.client.create_code_env('PYTHON', 'AdaBoostClassifier-CLASSIFICATION-macro', 'DESIGN_MANAGED', {'pythonInterpreter': 'PYTHON36'})

        definition = code_env.get_definition()
        definition['desc']['installCorePackages'] = True
        definition['desc']['installJupyterSupport'] = True

        definition['specPackageList'] = 'scikit-learn>=0.20,<0.21\nscipy>=1.2,<1.3\nxgboost==0.82\nstatsmodels>=0.10,<0.11\njinja2>=2.10,<2.11\nflask>=1.0,<1.1\ncloudpickle>=1.3,<1.6\nsklearn==0.0'
        # Save the new settings
        code_env.set_definition(definition)

        # Actually perform the installation
        code_env.update_packages()
        code_env.set_jupyter_support(True)
        return '<span>DONE</span>'
