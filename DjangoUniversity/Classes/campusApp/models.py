from django.db import models

    # Create model of Cases
class Cases(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    Lawer_name = models.CharField(max_length=60, default="", blank=True, null=False)
    case_num = models.IntegerField(default="", blank=True, null=False)
    case_duration = models.FloatField(null=True, blank=True, default=None)
    case_cost = models.FloatField(null=True, blank=True, default=None)
    Def_name = models.CharField(max_length=60, default="", blank=True, null=False)


    #Creates model manager
    object = models.Manager()

    #Displays the object output values in the form of a string
    def __str__(self):
        # Returns the input value of the title and the instructor name
        # field as a tuple to display in the browser instedof the default titles
        display_course = '{0.title}: {0.case_num}'
        return display_course.format(self)
    # Remove added 's' that django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "Cases"

