from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel

class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8080
    reload: bool = True

class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    users: str = "/users"
    fipers: str = "/fipers"
    jupers: str = "/jupers"
    project: str = "/project"
    invoice: str = "/invoice"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()

class EncryptionConfig(BaseModel):
    """Configuration for data encryption (GDPR compliance)."""
    key: str = ""  # Base64-encoded Fernet key (set via DECONT_CONFIG__ENCRYPTION__KEY)

class CORSConfig(BaseModel):
    """Configuration for CORS middleware."""
    allow_origins: str = "http://localhost:3000,http://localhost:3001,http://127.0.0.1:3000,http://127.0.0.1:3001"  # Comma-separated list of allowed origins (set via DECONT_CONFIG__CORS__ALLOW_ORIGINS)
    allow_credentials: bool = True
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]
    
    def get_origins_list(self) -> list[str]:
        """Parse comma-separated origins string into list."""
        if not self.allow_origins:
            return []
        return [origin.strip() for origin in self.allow_origins.split(",") if origin.strip()]

class DatabaseConfig(BaseModel):
    host: str = "localhost"
    port: int = 3306
    user: str = ""
    password: str = ""
    database: str = ""
    
    echo: bool = True
    echo_pool: bool = False
    pool_size: int = 5
    max_overflow: int = 10

    naming_convention: dict[str,str]  = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(column_0_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.prod", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="DECONT_CONFIG__",
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig = DatabaseConfig()
    encryption: EncryptionConfig = EncryptionConfig()
    cors: CORSConfig = CORSConfig()


settings = Settings()