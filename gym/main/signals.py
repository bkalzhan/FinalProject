# import logging
# import os
# import shutil
#
# from django.dispatch import receiver
# from django.db.models.signals import post_save, pre_save, post_delete
#
# from main.models import GymPhoto
#
#
# logger = logging.getLogger(__name__)
#
#
# @receiver(post_delete, sender=GymPhoto)
# def delete_photo_on_gym_photo_delete(sender, instance, *args, **kwargs):
#     photo = instance.photo
#     if photo:
#         gym_photo_photo_path = os.path.abspath(os.path.join(photo.path, '..'))
#         shutil.rmtree(gym_photo_photo_path)
#         logger.debug(f'Hotel photo deleted ID: {instance}')
#         logger.info(f'Hotel photo deleted ID: {instance}')
#         logger.warning(f'Hotel photo deleted ID: {instance}')
#         logger.error(f'Hotel photo deleted ID: {instance}')
#         logger.critical(f'Hotel photo deleted ID: {instance}')