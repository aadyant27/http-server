from enum import Enum


class LogLevel(Enum):
    INFO = "INFO"
    ERROR = "ERROR"
    WARN = "WARN"
    DEBUG = "DEBUG"


class Logger:
    def __init__(self, name: str):
        self.name = name

    def log(self, level: LogLevel, message: str):
        if self.level == LogLevel.INFO:
            self.info(message)
        elif self.level == LogLevel.ERROR:
            self.error(message)
        elif self.level == LogLevel.WARN:
            self.warn(message)
        elif self.level == LogLevel.DEBUG:
            self.debug(message)
        else:
            raise ValueError(f"Unknown log level: {self.level}")

    def info(self, message):
        print(f"[ {self.name} ] INFO ✅: {message}")

    def error(self, message):
        print(f"[ {self.name} ] ERROR ❌: {message}")

    def warn(self, message):
        print(f"[ {self.name} ] WARN ⚠️ : {message}")

    def debug(self, message):
        print(f"[ {self.name} ] DEBUG 🚨: {message}")
