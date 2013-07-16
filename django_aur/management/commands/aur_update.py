import os
import shutil
import subprocess

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django_aur.models import Update

class Command(BaseCommand):
    args = '<package_file package_file ...>'
    help = 'Updates the specified package files'

    def handle(self, *args, **options):
        for package_file in args:
            if not os.path.exists(package_file):
                raise CommandError("Package file '{}' does not exist"
                                   .format(package_file))
            extension = '.pkg.tar.xz'
            repo_file = '{}.db.tar.gz'.format(settings.AUR_REPOSITORY)
            if not package_file.endswith(extension):
                raise CommandError("Package file '{}' unknown extension"
                                   .format(package_file))
            base_file = package_file[:len(package_file)-len(extension)]
            package, ver, rel, arch = base_file.rsplit('-', 3)
            version = '{}-{}'.format(ver, rel)
            if Update.objects.filter(package=package, version=version,
                                     arch=arch).exists():
                raise CommandError("Package file '{}' update already exists"
                                   .format(package_file))

            dirname = os.path.join(settings.AUR_ROOT, arch)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            path = os.path.join(dirname, package_file)
            if not os.path.exists(path):
                shutil.copy(package_file, path)

            try:
                previous = Update.objects.filter(package=package,
                                                 arch=arch).latest('time')
                previous_file = '{}-{}-{}{}'.format(previous.package,
                                                    previous.version,
                                                    arch,
                                                    extension)
                previous_dirname = os.path.join(settings.AUR_ROOT, arch)
                previous_path = os.path.join(previous_dirname, previous_file)
                if arch == 'any':
                    for link_arch in settings.AUR_ANY:
                        link_dirname = os.path.join(settings.AUR_ROOT, link_arch)
                        link_path = os.path.join(link_dirname, previous_file)
                        if os.path.exists(link_path):
                            self.stdout.write(link_path)
                            subprocess.check_call(['repo-remove', os.path.join(
                                link_dirname, repo_file), previous.package])
                            os.unlink(link_path)
                if os.path.exists(previous_path):
                    if arch != 'any':
                        subprocess.check_call(['repo-remove', os.path.join(
                            previous_dirname, repo_file), previous.package])
                    os.remove(previous_path)
            except Update.DoesNotExist:
                pass

            if arch == 'any':
                for link_arch in settings.AUR_ANY:
                    link_dirname = os.path.join(settings.AUR_ROOT, link_arch)
                    if not os.path.exists(link_dirname):
                        os.makedirs(link_dirname)
                    link_path = os.path.join(link_dirname, package_file)
                    if not os.path.exists(link_path):
                        os.symlink(path, link_path)
                    subprocess.check_call(['repo-add', os.path.join(
                        link_dirname, repo_file), link_path])
            else:
                subprocess.check_call(['repo-add', os.path.join(
                    dirname, repo_file), path])

            Update.objects.create(package=package, version=version, arch=arch)
            self.stdout.write("Successfully updated package file '{}'"
                              .format(package_file))
