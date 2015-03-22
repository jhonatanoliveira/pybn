from distutils.core import setup
 
setup(name = "pydag",
      version = "0.1",
      description = "A Simple BN package",
      author = "Jhonatan Oliveira",
      author_email = "jhonatanoliveira@gmail.com",
      url = "www2.cs.uregina.ca/~desouzjh/",
      packages=["pydag","pydag.core","pydag.utilities","pydag.inference"]
      )