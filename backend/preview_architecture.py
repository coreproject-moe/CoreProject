import docutils.core
  
docutils.core.publish_file(
    source_path ="ARCHITECTURE.rst",
    destination_path ="Output.html",
    writer_name ="html")