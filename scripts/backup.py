"""Database backup utility."""
import subprocess
from config.settings import settings

def backup_db():
    cmd = [
        "pg_dump",
        "-h", settings.POSTGRES_HOST,
        "-U", settings.POSTGRES_USER,
        "-d", settings.POSTGRES_DB,
        "-F", "c",
        "-b",
        "-v",
        "-f", "backup.dump"
    ]
    subprocess.run(cmd)

if __name__ == "__main__":
    backup_db()