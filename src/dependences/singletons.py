from src.controllers.patient import PatientController
from src.controllers.compute import ComputeController
from src.controllers.request import RequestController

patient_controller_singleton: PatientController = PatientController()
compute_controller_singleton: ComputeController = ComputeController()
request_controller_singleton: RequestController = RequestController()
