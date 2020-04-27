It is a Demo file.
a = zipfile.ZipFile("MyZip.Zip",mode='w')
a.write("Demo.txt",compress_type=zipfile.ZIP_DEFLATED)
a.close()