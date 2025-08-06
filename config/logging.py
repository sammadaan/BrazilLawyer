"""Structured logging configuration using structlog."""
import structlog
import logging

def setup_logging():
    logging.basicConfig(
        format="%(message)s",
        stream=None,
        level=logging.INFO,
    )
    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer(),
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )