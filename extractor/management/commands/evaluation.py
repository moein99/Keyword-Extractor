from django.core.management import BaseCommand
from extractor.evaluation.compute import compute_metrics, read_data, store_results
import multiprocessing


NUM_OF_PROCESS = 50


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('limit', type=int)

    def handle(self, *args, **options):
        limit = options["limit"] if options["limit"] else -1
        d = read_data("extractor/evaluation/data.test")[:limit]
        data = []
        step = int(len(d) / NUM_OF_PROCESS)
        for i in range(0, len(d), step):
            data.append(d[i:i + step])

        processes = []
        for i in range(NUM_OF_PROCESS):
            p = multiprocessing.Process(target=compute_metrics, args=(data[i],))
            processes.append(p)
            p.start()

        for process in processes:
            process.join()

        store_results()
