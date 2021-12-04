import csv
from django.core.management import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = "Loads CSV data"
    
    def add_arguments(self, parser):
        parser.add_argument("file_path",type=str)
    
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        start_time = timezone.now()
        file_path = options["file_path"]
        with open(file_path,"r") as csv_file:
            data = list(csv.reader(csv_file,delimiter=","))
            for row in data[1:]:
                location_code = 