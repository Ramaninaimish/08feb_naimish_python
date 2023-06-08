#What is a QuerySet?
 #queryset is a collection of objects from your database.

#Write program to create a new Post object in database.
"""...
class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField()
    content = models.TextField()
    """ 
"""def index(request):
    if request.method=='POST':
        newuser=userForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Record inserted!")
        else:
            print(newuser.errors)
    return render(request,'index.html')"""