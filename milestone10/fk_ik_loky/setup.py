from setuptools import find_packages, setup

package_name = 'fk_ik_loky'

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
    maintainer='veevry',
    maintainer_email='rafifraihanbahrulalam@mail.ugm.ac.id',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'forward_kinematics = fk_ik_loky.forward_kinematics:main',
            'inverse_kinematics = fk_ik_loky.inverse_kinematics:main',
            'fk_all_legs = fk_ik_loky.all_leg_forward_kinematics:main',
            'ik_all_legs = fk_ik_loky.ik_for_all_leg:main',
        ],
    },
)
