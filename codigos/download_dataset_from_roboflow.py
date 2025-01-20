from roboflow import Roboflow
rf = Roboflow(api_key="3ky4agwNennrYm6hr0FC")
project = rf.workspace("valescka-barros").project("detect_clickable_icons")
version = project.version(16)
dataset = version.download("yolov8")          