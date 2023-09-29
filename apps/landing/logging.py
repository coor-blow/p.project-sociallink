from enum import Enum
from .utils import MetaSingleton


class LevelEnum(Enum):
    info = "INFO"
    critical = "CRITICAL"
    warning = "WARNING"
    error = "ERROR"


class Logging(metaclass=MetaSingleton):
    def __init__(self, file_name: str) -> None:
        self.file_name: str = file_name

    def _write_log(self, level: LevelEnum, msg: str) -> None:

        with open(self.file_name, "a") as log_file:
            log_file.write(f"[{level.name}] {msg}\n")

    def info(self, msg):
        self._write_log(LevelEnum.info, msg)

    def critical(self, msg):
        self._write_log(LevelEnum.critical, msg)

    def warning(self, msg):
        self._write_log(LevelEnum.warning, msg)

    def error(self, msg):
        self._write_log(LevelEnum.error, msg)



