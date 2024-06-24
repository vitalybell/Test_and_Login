import requests as rq
import logging

logger = logging.getLogger('RequestsLogger')
logging.basicConfig(level=logging.INFO)

success_logger = logging.getLogger('success_responses')
success_handler = logging.FileHandler('success_responses.log')
success_handler.setLevel(logging.INFO)
success_logger.addHandler(success_handler)
bad_logger = logging.getLogger('bad_responses')
bad_handler = logging.FileHandler('bad_responses.log')
bad_handler.setLevel(logging.INFO)
bad_logger.addHandler(bad_handler)
blocked_logger = logging.getLogger('blocked_responses')
blocked_handler = logging.FileHandler('blocked_responses.log')
blocked_handler.setLevel(logging.INFO)
blocked_logger.addHandler(blocked_handler)


sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            success_logger.info(f'Successful response from {site}')
        else:
            bad_logger.info(f'Bad response from {site}: Status code {response.status_code}')
    except rq.exceptions.RequestException as e:
        blocked_logger.info(f'Blocked or no response from {site}: {e}')
