import json

from sqlalchemy import select, or_, and_
from src.db.database import get_db
from src.models.episode import Episode
from src.models.patient import Patient
from src.models.patient_id import Identifier
from src.cache.redis import RedisClient


class Controller:

    def __init__(self):
        self.__cache: RedisClient = RedisClient()

    async def get_patient_by_code(self, code: int) -> Patient | None:
        await self.__get_cache_config()
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

    async def get_patient_by_string(self, text: str) -> list[Patient] | None:
        await self.__get_cache_config()
        db_gen = get_db()
        session = next(db_gen)
        try:
            stmt = (
                select(Patient)
                .join(Identifier, Patient.icode == Identifier.iicode)
                .where(
                    or_(
                        Identifier.iipid == text,
                        Identifier.iipid.like(f"{text}-%")
                    )
                )
                .order_by(Identifier.iipid.asc(), Patient.icode.asc())
                .limit(20)
            )
            result = session.execute(stmt)
            records: list[Patient] = result.scalars().all()
            for patient in records:
                stmt = (
                    select(Episode)
                    .where(
                        and_(
                            Episode.eppatcode == patient.icode,
                            Episode.epclosedate == 0,
                            Episode.eptype.in_([1, 2, 3, 4, 12])
                        )
                    )
                    .order_by(Episode.epnumber.desc())
                )
                result = session.execute(stmt)
                episode: Episode = result.scalars().first()

        except Exception as e:
            print(f"Exception")
        finally:
            try:
                next(db_gen)

            except StopIteration:
                pass
            finally:
                return records

    async def __get_cache_config(self):
        print("Getting cache from REDIS")
        await self.__cache.ping()

        value = await self.__cache.get("FILTER_BY_PATIENT_SITE")
        if value:
            print(value)
        value = await self.__cache.get("CHECKSUM_SEPERATOR_FOR_SAVE")
        if value:
            print(value)
        value = await self.__cache.get("USE_SENDER_EPISODE_FOR_PATIENT")
        if value:
            print(value)
        value = await self.__cache.get("SEARCH_PATIENT_BY_HOSPITALIZATION")
        if value:
            print(value)
        value = await self.__cache.get("SEARCH_PATIENT_BY_HAS_ORDERS_DAYS_BACK")
        if value:
            print(value)
        value = await self.__cache.get("SEARCH_PATIENTS_BY_VIEW")
        if value:
            print(value)
        value = await self.__cache.get("EXECUTE_DEMOG_WITH_EPISODE")
        if value:
            print(value)
        value = await self.__cache.get("EXECUTE_DEMOG_POLICY")
        if value:
            print(value)
        value = await self.__cache.get("PATIENT_CHECKSUM_IDTYPE_SEARCH_LOGIC")
        if value:
            print(value)
