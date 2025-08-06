from src.controllers.patient import PatientController
from src.controllers.compute import ComputeController

patient_controller_singleton: PatientController = PatientController()
compute_controller_singleton: ComputeController = ComputeController()
