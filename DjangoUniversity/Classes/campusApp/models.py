from django.db import models

    # Create model of Cases
class UniversityCampus(models.Model):
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=60, default="", blank=True, null=False)
    campus = models.CharField(max_length=60, default="", blank=True, null=False)

    #Creates model manager
    object = models.Manager()

    #Displays the object output values in the form of a string
    def __str__(self):
        # Returns the input value of the title and the instructor name
        # field as a tuple to display in the browser instedof the default titles
        display_course = '{0.campus}: {0.state}'
        return display_course.format(self)
    # Remove added 's' that django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campuses"

