from setuptools import setup
from glob import glob
import os

package_name = 'tihu_2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/meshes', [
        'meshes/A.STL',
        'meshes/B.STL',
        'meshes/C.STL',
        'meshes/D.STL',
        'meshes/E.STL',
        'meshes/F.STL',
        'meshes/base_link.STL',
    ]),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/**')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zx',
    maintainer_email='2290787180@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
