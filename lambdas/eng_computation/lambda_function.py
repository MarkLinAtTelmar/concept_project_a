import json
from share_module_x.log_utils import EngineLog

engine_logger = EngineLog("concep_project_a")

def lambda_handler(event, context):

    engine_logger.print_debug_log('init concep_project_a')
    return {
        "success": True
    }

if __name__ == "__main__":

    lambda_handler(None, None)