from setuptools import setup
import setup_translate

pkg = 'Extensions.SimpleUmount'
setup(name='enigma2-plugin-extensions-simpleumount',
       version='0.10',
       description='Simple umounter mass storage device',
       package_dir={pkg: 'SimpleUmount'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
