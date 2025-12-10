
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64
import os
from typing import Optional


class EncryptionManager:
    
    def __init__(self, key: Optional[str] = None):
        if key:
            self.key = key.encode() if isinstance(key, str) else key
        else:
            # Try to get from environment variable
            env_key = os.getenv("DECONT_CONFIG__ENCRYPTION__KEY")
            if env_key:
                self.key = env_key.encode()
            else:
                # Generate a new key (for development only - not for production!)
                # In production, always provide a key via environment variable
                self.key = Fernet.generate_key()
        
        self.fernet = Fernet(self.key)
    
    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt a plaintext string.
        
        Args:
            plaintext: The string to encrypt
            
        Returns:
            Base64-encoded encrypted string
        """
        if plaintext is None:
            return None
        
        if not isinstance(plaintext, str):
            plaintext = str(plaintext)
        
        encrypted_bytes = self.fernet.encrypt(plaintext.encode())
        return base64.b64encode(encrypted_bytes).decode()
    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt an encrypted string.
        
        Args:
            ciphertext: Base64-encoded encrypted string
            
        Returns:
            Decrypted plaintext string
        """
        if ciphertext is None:
            return None
        
        try:
            encrypted_bytes = base64.b64decode(ciphertext.encode())
            decrypted_bytes = self.fernet.decrypt(encrypted_bytes)
            return decrypted_bytes.decode()
        except Exception as e:
            # Log the error in production
            raise ValueError(f"Failed to decrypt data: {str(e)}")
    
    @staticmethod
    def generate_key() -> str:
        """
        Generate a new encryption key.
        
        Returns:
            Base64-encoded Fernet key (safe to store in environment variables)
        """
        return Fernet.generate_key().decode()


# Global encryption manager instance
# Will be initialized with key from config
_encryption_manager: Optional[EncryptionManager] = None


def get_encryption_manager() -> EncryptionManager:
    """
    Get the global encryption manager instance.
    
    Returns:
        EncryptionManager instance
    """
    global _encryption_manager
    if _encryption_manager is None:
        from core.config import settings
        key = settings.encryption.key
        if not key:
            # Generate a key for development (not recommended for production)
            key = EncryptionManager.generate_key()
            import warnings
            warnings.warn(
                "No encryption key provided! Generated a temporary key. "
                "For production, set DECONT_CONFIG__ENCRYPTION__KEY environment variable.",
                UserWarning
            )
        _encryption_manager = EncryptionManager(key)
    return _encryption_manager


if __name__ == "__main__":
    key = EncryptionManager.generate_key()
    print(f"Encryption key: {key}")
