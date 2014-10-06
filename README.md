#Simple Image Uploading App


This app allows users to upload images to an AWS3 bucket; images are
validated using pHash to determine whether they are duplicates of
existing images.

##References used while preparing this project:

* Setting up celery/SQS:
    - http://www.caktusgroup.com/blog/2011/12/19/using-django-and-celery-amazon-sqs/
    - http://lovelltroy.org/deploying-celery-with-sqs.html
    - http://www.caktusgroup.com/blog/2014/06/23/scheduling-tasks-celery/
    - http://michal.karzynski.pl/blog/2014/05/18/setting-up-an-asynchronous-task-queue-for-django-using-celery-redis/

* Setting up file storage on S3:
    - http://djangotricks.blogspot.com/2013/12/how-to-store-your-media-files-in-amazon.html
