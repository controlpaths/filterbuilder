
def log (text, severity, verbose):
    if severity == 'info' and verbose >= 2:
      print("[INFO] " + text)
    
    if severity == "warning" and verbose >= 1:
      print("[WARNING] " + text)

    if severity == "error":
      print("[ERROR] " + text)
      exit()