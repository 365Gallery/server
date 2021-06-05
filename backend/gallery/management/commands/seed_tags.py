from django.core.management.base import BaseCommand
from gallery.models import Tag


class Command(BaseCommand):
    help = "This command creates tags"

    def handle(self, *args, **options):
        Tag.objects.create(idx=0, name="William Turner", color="5e8b7e")
        Tag.objects.create(idx=2, name="Seurat", color="fff5eb")
        Tag.objects.create(idx=3, name="Claude Monet", color="deedf0")
        Tag.objects.create(idx=4, name="Leonid Afremov", color="f4c7ab")
        Tag.objects.create(idx=5, name="Katsushika Hokusai", color="b2b8a3")
        Tag.objects.create(idx=6, name="Henri Matisse", color="f9b208")
        Tag.objects.create(idx=7, name="André Derain", color="f98404")
        Tag.objects.create(idx=8, name="Pablo Picasso", color="f55c47")
        Tag.objects.create(idx=9, name="Fernand Léger", color="9fe6a0")
        Tag.objects.create(idx=10, name="Francis Picabia", color="4aa96c")
        Tag.objects.create(idx=11, name="Robert Delaunay", color="564a4a")
        Tag.objects.create(idx=12, name="Pieter Mondrian", color="8e9775")
        Tag.objects.create(idx=13, name="Edvard Munch", color="e28f83")
        Tag.objects.create(idx=14, name="Gustav Klimt", color="7b6079")
        Tag.objects.create(idx=15, name="Umberto Boccioni", color="325288")
        Tag.objects.create(idx=16, name="Giacomo Balla", color="dbf6e9")
        Tag.objects.create(idx=17, name="Joan Miro", color="cdc733")
        Tag.objects.create(idx=18, name="Marc Chagall", color="966c3b")
        Tag.objects.create(idx=19, name="Roy Lichtenstein", color="e7d9ea")
        Tag.objects.create(idx=20, name="Keith Haring", color="6f9eaf")
        self.stdout.write(self.style.SUCCESS(f'tag created!'))