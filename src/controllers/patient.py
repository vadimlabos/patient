import asyncio

from sqlalchemy import select, or_, and_
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.database import get_db, async_session_maker
from src.models.episode import Episode
from src.models.patient import Patient
from src.models.patient_id import Identifier
from src.cache.redis import RedisClient
from src.cache.redis_async import RedisClientAsync


class PatientController:

    def __init__(self):
        self.__cache: RedisClient = RedisClient()
        self.__cache_async: RedisClientAsync = RedisClientAsync()

    def get_patient_by_code(self, code: int) -> Patient | None:
        self.__get_cache_config()
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

    async def get_patient_by_code_async(self, code: int) -> Patient | None:
        await self.__get_cache_config_async()
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

    def get_patient_by_string(self, text: str) -> list[Patient] | None:
        self.__get_cache_config()
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

    async def get_patient_by_string_async(self, text: str) -> list[Patient]:
        await self.__get_cache_config_async()

        async with async_session_maker() as session:  # <- preferred async session
            try:
                stmt = (
                    select(Patient)
                    .join(Identifier, Patient.icode == Identifier.iicode)
                    .order_by(Identifier.iipid.asc(), Patient.icode.asc())
                    .limit(20)
                )
                result = await session.execute(stmt)
                patients = result.scalars().all()

                for patient in patients:
                    patient.icode = 0

                return None

            except Exception as e:
                print(f"Exception occurred: {e}")
                return []

    def __get_cache_config(self):
        self.__cache.ping()

        self.__cache.get("FILTER_BY_PATIENT_SITE")
        self.__cache.get("CHECKSUM_SEPERATOR_FOR_SAVE")
        self.__cache.get("USE_SENDER_EPISODE_FOR_PATIENT")
        self.__cache.get("SEARCH_PATIENT_BY_HOSPITALIZATION")
        self.__cache.get("SEARCH_PATIENT_BY_HAS_ORDERS_DAYS_BACK")
        self.__cache.get("SEARCH_PATIENTS_BY_VIEW")
        self.__cache.get("EXECUTE_DEMOG_WITH_EPISODE")
        self.__cache.get("EXECUTE_DEMOG_POLICY")
        self.__cache.get("PATIENT_CHECKSUM_IDTYPE_SEARCH_LOGIC")

    async def __get_cache_config_async(self):
        await self.__cache_async.ping()

        keys = [
            "FILTER_BY_PATIENT_SITE",
            "CHECKSUM_SEPERATOR_FOR_SAVE",
            "USE_SENDER_EPISODE_FOR_PATIENT",
            "SEARCH_PATIENT_BY_HOSPITALIZATION",
            "SEARCH_PATIENT_BY_HAS_ORDERS_DAYS_BACK",
            "SEARCH_PATIENTS_BY_VIEW",
            "EXECUTE_DEMOG_WITH_EPISODE",
            "EXECUTE_DEMOG_POLICY",
            "PATIENT_CHECKSUM_IDTYPE_SEARCH_LOGIC",
        ]

        # Launch all cache.get calls concurrently
        tasks = [self.__cache_async.get(key) for key in keys]
        results = await asyncio.gather(*tasks)
