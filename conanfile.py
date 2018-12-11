#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from conans import ConanFile, CMake, tools, RunEnvironment
import os


class TestPackageConan(ConanFile):
    name = "sourcemaking"
    version = "0.0.0"
    license = "MIT"
    author = "Jimmy M. Gong yssource@163.com"
    url = "https://github.com/yssource/conan-boost-python-test"
    description = "conan-boost-python-test"
    topics = ("conan", "boost_python", "test")
    settings = "os", "compiler", "build_type", "arch"
    # options = {"python_dev_config:python": "/home/jimmy/.pyenv/versions/anaconda3-5.0.1/envs/devel/bin/python", "boost_python:python_version": "3.6"}
    options = {"shared": [True, False], "SIMPLE": [True, False]}
    default_options = {"python_dev_config:python": "/home/jimmy/.pyenv/versions/anaconda3-5.0.1/envs/devel/bin/python", "boost_python:python_version": "3.6"}
    generators = "cmake"

    def requirements(self):
        self.requires("boost_base/1.67.0@{}/{}".format("bincrafters", "stable"))
        self.requires("boost_format/1.67.0@{}/{}".format("bincrafters", "stable"))
        self.requires("boost_python/1.67.0@{}/{}".format("bincrafters", "stable"))
        self.requires("python_dev_config/0.5@{}/{}".format("bincrafters", "stable"))


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def test(self):
        self.run(os.path.join("bin", "test_package"), run_environment=True)
