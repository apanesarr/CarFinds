from django.core.management.base import BaseCommand
from carfinds.models import Car
class Command(BaseCommand):
    help = 'populates db with cars'

    def _create_tags(self):
        car1 = Car(name="Supra", vendor="Toyota", price=60000, img = "https://www.topgear.com/sites/default/files/styles/fit_1960x1102/public/images/news-article/carousel/2019/01/6bb7a65acd31f46e9197dcc7edd94d02/supra_edit_2.jpg?itok=dD8aNfIH") 
        car1.save()
        car2 =  Car(name="Accord", vendor="Honda", price=60000, img = "https://www.topgear.com/sites/default/files/styles/fit_1960x1102/public/images/news-article/carousel/2019/01/6bb7a65acd31f46e9197dcc7edd94d02/supra_edit_2.jpg?itok=dD8aNfIH") 
        car2.save()
        car3 =  Car(name="86", vendor="Toyota", price=60000, img = "https://www.topgear.com/sites/default/files/styles/fit_1960x1102/public/images/news-article/carousel/2019/01/6bb7a65acd31f46e9197dcc7edd94d02/supra_edit_2.jpg?itok=dD8aNfIH") 
        car3.save()
    def handle(self, *args, **options):
        self._create_tags()