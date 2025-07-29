from sqlalchemy import select
from src.db.database import get_db
from src.models.patient import Patient


class Controller:

    @staticmethod
    def get_patient_by_code(code: int) -> Patient | None:
        db_gen = get_db()
        session = next(db_gen)
        try:
            stmt = select(Patient).where(Patient.icode == code)
            result = session.execute(stmt)
            return result.scalar_one_or_none()
        finally:
            try:
                next(db_gen)
            except StopIteration:
                pass
