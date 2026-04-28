import logging
import os
import sys

# Define a raiz do projeto (voltando de execution/utils para a raiz)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOGS_DIR = os.path.join(PROJECT_ROOT, "logs")

def get_logger(name):
    """
    Retorna um logger configurado para imprimir no console e salvar no arquivo logs/automation.log.
    """
    if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR)

    logger = logging.getLogger(name)
    
    # Previne a adição de múltiplos handlers (duplicação de logs)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        formatter = logging.Formatter(
            '%(asctime)s [%(name)s] [%(levelname)s] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # File Handler (anexa ao arquivo)
        log_file = os.path.join(LOGS_DIR, "automation.log")
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console Handler (imprime no terminal)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
