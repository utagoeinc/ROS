from setuptools import setup

package_name = 'sphero_driving'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kazunari Takasaki',
    maintainer_email='utagoeinc@gmail.com',
    description='Sphero Driver',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'subtest = sphero_driving.subtest:main',
            'drive = sphero_driving.drive:main',
            'sensors_pub = sphero_driving.sensors_pub:main',
            'test_sensors_pub = sphero_driving.test_sensors_pub:main',
        ],
    },
)
