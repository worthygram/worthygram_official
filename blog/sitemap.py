from django.contrib.sitemaps import Sitemap

# import the model that has the posts that you want to be on the sitemap
from .models import Post,Story


class PostSitemap(Sitemap):
    # define how often your website will change, the priority, and the protocol used to access your site
    changefreq = 'weekly' # can be weekly daily always monthly yearly or never
    priority = 1.0   # on a scale of 0.0 to 1.0
    protocol = 'https'  # use https when you deploy your website and are using a secure connection

    # define the posts you want in your sitemap here
    def items(self):
        return Post.objects.all()

    
    
    # returns the URL of the article object
    def location(self, obj):
        return f'/{obj.slug}'

class StorySitemap(Sitemap):
    # define how often your website will change, the priority, and the protocol used to access your site
    changefreq = 'weekly' # can be weekly daily always monthly yearly or never
    priority = 1.0   # on a scale of 0.0 to 1.0
    protocol = 'https'  # use https when you deploy your website and are using a secure connection

    # define the posts you want in your sitemap here
    def items(self):
        return Story.objects.all()

    
    
    # returns the URL of the article object
    def location(self, obj):
        return f'/{obj.id}'