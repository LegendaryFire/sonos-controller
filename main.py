from config import Config
from players import Players
from worker import Worker

if __name__ == '__main__':
    config = Config('config.xml')
    player = Players(config)

    worker = Worker(config, player)
    worker.start_listening()
