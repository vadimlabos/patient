from src.controllers.compute import ComputeController
from src.controllers.patient import PatientController
from src.db.database import get_db
from src.dependences.singletons import patient_controller_singleton, compute_controller_singleton


def get_patient_controller() -> PatientController:
    return patient_controller_singleton


def get_compute_controller() -> ComputeController:
    return compute_controller_singleton


def get_db_session():
    db_gen = get_db()
    return next(db_gen)
