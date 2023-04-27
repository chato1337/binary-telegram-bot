import os

bot_settings = {
    'telegram_token': os.getenv('TELEGRAM_TOKEN', 'not found telegram token'),
    'api_frames': os.getenv('API', 'not api frames found')
}