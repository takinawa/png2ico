from PIL.Image import open
def png2ico(file: str) -> None:
  assert file.rpartition(".")[-1] == "png", "File is not a png file"
  img = open(file)
  min_length = min(img.size)
  img.resize((min_length, min_length)).save(file.rpartition(".")[0] + ".ico", format="ICO")
