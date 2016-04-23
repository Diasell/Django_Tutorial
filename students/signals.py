import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


from .models import Student, Professor

@receiver(post_save, sender=Student)
def log_student_updated_added_event(sender, **kwargs):
    """
    Writes info about newly added or updated student into log file
    """

    logger = logging.getLogger(__name__)


    student = kwargs['instance']
    if kwargs['created']:
        logger.info("Student added: %s %s (ID: %d)", student.first_name, student.last_name, student.id)
    else:
        logger.info("Student updated: %s %s (ID: %d)", student.first_name, student.last_name, student.id)



@receiver(post_delete, sender=Student)
def log_student_deleted_event(sender, **kwargs):
    """
    Writes to log about deleting students
    """

    logger = logging.getLogger(__name__)

    student = kwargs['instance']
    logger.info("Student deleted: %s %s (ID: %d)", student.first_name, student.last_name, student.id)


@receiver(post_save, sender=Professor)
def log_professor_updated_added_event(sender, **kwargs):
    """
    Writes to log info about adding/updating professors
    """
    logger = logging.getLogger(__name__)

    proffesor = kwargs['instance']
    if kwargs['created']:
        logger.info("Professor added: %s %s (ID: %d)", proffesor.first_name,  proffesor.last_name, proffesor.id)
    else:
        logger.info("Professor updated: %s %s (ID: %d)", proffesor.first_name, proffesor.last_name, proffesor.id)



@receiver(post_delete, sender=Professor)
def log_professor_deleted_event(sender, **kwargs):
    """
    Writes to log about deleting professor events
    """

    logger = logging.getLogger(__name__)

    professor = kwargs['instance']
    logger.info("Professor deleted: %s %s (ID: %d)", professor.first_name, professor.last_name, professor.id)

