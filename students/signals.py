import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


from .models import Student, Professor, Group, Exams

# @receiver(post_save, sender=Student)
# def log_student_updated_added_event(sender, **kwargs):
#     """
#     Writes info about newly added or updated student into log file
#     """
#
#     logger = logging.getLogger(__name__)
#
#
#     student = kwargs['instance']
#     if kwargs['created']:
#         logger.info("Student added: %s %s (ID: %d)", student.first_name, student.last_name, student.username)
#     else:
#         logger.info("Student updated: %s %s (ID: %d)", student.first_name, student.last_name, student.username)
#
#
#
# @receiver(post_delete, sender=Student)
# def log_student_deleted_event(sender, **kwargs):
#     """
#     Writes to log about deleting students
#     """
#
#     logger = logging.getLogger(__name__)
#
#     student = kwargs['instance']
#     logger.info("Student deleted: %s %s (ID: %d)", student.first_name, student.last_name, student.id)
#
#
# @receiver(post_save, sender=Professor)
# def log_professor_updated_added_event(sender, **kwargs):
#     """
#     Writes to log info about adding/updating professors
#     """
#     logger = logging.getLogger(__name__)
#
#     proffesor = kwargs['instance']
#     if kwargs['created']:
#         logger.info("Professor added: %s %s (ID: %d)", proffesor.first_name,  proffesor.last_name, proffesor.id)
#     else:
#         logger.info("Professor updated: %s %s (ID: %d)", proffesor.first_name, proffesor.last_name, proffesor.id)
#
#
#
# @receiver(post_delete, sender=Professor)
# def log_professor_deleted_event(sender, **kwargs):
#     """
#     Writes to log about deleting professor events
#     """
#
#     logger = logging.getLogger(__name__)
#
#     professor = kwargs['instance']
#     logger.info("Professor deleted: %s %s (ID: %d)", professor.first_name, professor.last_name, professor.id)
#
#
# @receiver(post_save, sender=Exams)
# def log_exams_updated_added_event(sender, **kwargs):
#     """
#     Writes to log info about adding/updating exames
#     """
#     logger = logging.getLogger(__name__)
#
#     exam = kwargs['instance']
#     if kwargs['created']:
#         logger.info("Exam added: ID%d,  %s %s on %s ", exam.id, exam.exam_title, exam.exam_group, exam.date_time)
#     else:
#         logger.info("Exam updated: ID%d,  %s %s on %s ", exam.id, exam.exam_title, exam.exam_group, exam.date_time)
#
#
#
# @receiver(post_delete, sender=Exams)
# def log_professor_deleted_event(sender, **kwargs):
#     """
#     Writes to log about deleting exams events
#     """
#
#     logger = logging.getLogger(__name__)
#
#     exam = kwargs['instance']
#     logger.info("Exam deleted: ID%d,  %s %s on %s ", exam.id, exam.exam_title, exam.exam_group, exam.date_time)
#
#
# @receiver(post_save, sender=Group)
# def log_exams_updated_added_event(sender, **kwargs):
#     """
#     Writes to log info about adding/updating groups
#     """
#     logger = logging.getLogger(__name__)
#
#     group = kwargs['instance']
#     if kwargs['created']:
#         logger.info("Group added: ID%d,  %s", group.id, group.title)
#     else:
#         logger.info("Group updated: ID%d,  %s", group.id, group.title)
#
#
#
# @receiver(post_delete, sender=Group)
# def log_professor_deleted_event(sender, **kwargs):
#     """
#     Writes to log about deleting group events
#     """
#
#     logger = logging.getLogger(__name__)
#
#     group = kwargs['instance']
#     logger.info("Group deleted: ID%d,  %s", group.id, group.title)
