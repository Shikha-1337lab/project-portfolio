from django.db import models

#Create A Blog models
#title
#pub_date
#body
#image

#Add the blog app to the settings

#Create a migration

#Migrate

#Add to the admin

class Blog(models.Model):
    title = models.CharField(max_length=255)
    blog_image = models.ImageField(upload_to='images/')
    body = models.TextField()
    pub_date = models.DateTimeField()
