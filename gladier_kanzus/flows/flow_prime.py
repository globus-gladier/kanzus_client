from gladier import GladierBaseClient, generate_flow_definition, utils
from gladier_kanzus.flows.base_flow import BaseClient

from gladier_kanzus.tools.dials_prime import dials_prime


@generate_flow_definition
class PrimeFlow(BaseClient):
    globus_group = 'e31ed13f-e9e0-11e9-bbd0-0a8c64af9bb2'

    containers = {
            utils.name_generation.get_funcx_function_name(dials_prime): {
                'container_type': 'singularity',
                'location': '/eagle/APSDataAnalysis/SSX/containers/dials_v4.simg',
        }
    }
    
    gladier_tools = [
        'gladier_kanzus.tools.DialsPrime',
        'gladier_kanzus.tools.TransferPrime',
    ]
    
