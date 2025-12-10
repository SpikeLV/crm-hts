from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, AsyncEngine
from core.config import DatabaseConfig
from typing import AsyncGenerator
from urllib.parse import quote_plus
from core.config import settings

class DatabaseHelper:
    def __init__(
        self, 
        config: DatabaseConfig
    ) -> None:
        # URL encode user and password to handle special characters
        user = quote_plus(config.user)
        password = quote_plus(config.password)
        
        self.engine: AsyncEngine = create_async_engine(
            f"mysql+aiomysql://{user}:{password}@{config.host}:{config.port}/{config.database}",
            echo=config.echo,
            echo_pool=config.echo_pool,
            pool_size=config.pool_size,
            max_overflow=config.max_overflow,
        )
        self.session_factory = async_sessionmaker(
            self.engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )
    async def session_generator(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        """FastAPI dependency for getting database session."""
        async with self.session_factory() as session:
            yield session

    async def dispose(self) -> None:
        await self.engine.dispose()


db_helper = DatabaseHelper(
    config=settings.db
)