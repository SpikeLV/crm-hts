"""
SQLAlchemy custom types for encrypted fields.
"""

from sqlalchemy import TypeDecorator, String
from core.encryption import get_encryption_manager


class EncryptedString(TypeDecorator):
    """
    SQLAlchemy TypeDecorator for automatically encrypting/decrypting string fields.
    
    This type automatically encrypts data before storing it in the database
    and decrypts it when reading from the database.
    
    Usage:
        class MyModel(Base):
            sensitive_field: Mapped[str] = mapped_column(EncryptedString(255))
    """
    
    impl = String
    cache_ok = True
    
    def __init__(self, length: int = 255, *args, **kwargs):
        super().__init__(length, *args, **kwargs)
        self.length = length
    
    def process_bind_param(self, value, dialect):
        """Encrypt the value before storing in the database."""
        if value is None:
            return None
        
        encryption_manager = get_encryption_manager()
        return encryption_manager.encrypt(value)
    
    def process_result_value(self, value, dialect):
        """Decrypt the value when reading from the database."""
        if value is None:
            return None
        
        encryption_manager = get_encryption_manager()
        return encryption_manager.decrypt(value)


