# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from cariomail.tasks import send_email_to
# from user.models import User
#
#
# @receiver(post_save, sender=User)
# def send_mail_on_create(sender, instance, created=False, **kwargs):
#     if created:
#         send_email_to(instance.email, "Created an account on Cario - car selling service", "Good Evening!\nThank you"
#                                                                                            "for believing in Cario")
