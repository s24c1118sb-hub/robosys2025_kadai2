from setuptools import find_packages, setup

package_name = 'my_disk_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ryota',
    maintainer_email='whippedcreampeanutflavor@gmail.com',
    description='Disk usage monitor node',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'monitor = my_disk_monitor.monitor:main'
        ],
    },
)
