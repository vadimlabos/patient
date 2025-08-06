
class ComputeController:

    @staticmethod
    async def compute():
        sum(1 for _ in range(100000000))
