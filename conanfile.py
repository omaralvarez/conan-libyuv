from conans import ConanFile, CMake, tools
from os.path import join

class LibyuvConan(ConanFile):
    name = "libyuv"
    version = "1735"
    #license = "BSD 3-Clause"
    #author = "<Put your name here> <And your email here>"
    url = "https://github.com/omaralvarez/conan-libyuv"
    repo_url = "https://github.com/omaralvarez/libyuv"
    description = "YUV scaling and conversion library"
    topics = ("YUV")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    def source(self):
        self.run("git clone -b 'v%s' --single-branch --depth 1 %s" % (self.version, self.repo_url))
    
    def requirements(self):
        self.requires.add('libjpeg/9c@bincrafters/stable')
    
    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="libyuv")
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
    
    def package_info(self):
        self.cpp_info.libs = ["yuv"]